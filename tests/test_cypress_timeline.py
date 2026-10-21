"""Exercise untrusted timeline boundaries and real stable-shell media export."""
import importlib.util
import json
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins/cypress-timeline/skills/timeline/scripts/build_timeline.py"
spec = importlib.util.spec_from_file_location("cypress_builder", SOURCE)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def png(red: int, green: int, blue: int) -> bytes:
    """Produce a tiny solid-color test fixture without a graphics dependency."""
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    pixels = (b"\0" + bytes([red, green, blue]) * 32) * 24
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 32, 24, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(pixels)) + chunk(b"IEND", b"")


class TimelineTests(unittest.TestCase):
    """Test user-visible exports and rejected unsafe or nonsensical inputs."""
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="cypress-test-")
        self.root = Path(self.temp.name)
        (self.root / "one.png").write_bytes(png(150, 50, 30))
        (self.root / "two.png").write_bytes(png(30, 130, 90))
        self.data = {"title": "Project report", "subtitle": "Estimated milestones", "disclosure": "Concept imagery, not actual footage", "stages": [
            {"title": "Start", "label": "Week 0", "week": 0, "seconds": 1, "description": "Initial state", "image": "one.png"},
            {"title": "Finish", "label": "Week 6", "week": 6, "seconds": 1, "description": "Final state", "image": "two.png"}]}

    def tearDown(self):
        self.temp.cleanup()

    def load(self):
        target = self.root / "timeline.json"
        target.write_text(json.dumps(self.data))
        return builder.load_timeline(target)

    def test_web_embeds_assets_and_preserves_start_finish(self):
        timeline = self.load()
        path = builder.build_web(timeline, self.root)
        html = path.read_text()
        self.assertEqual(html.count("data:image/png;base64,"), 2)
        self.assertNotIn(str(self.root), html)
        self.assertEqual([s["start"] for s in timeline["stages"]], [0, 1])
        self.assertIn("prefers-reduced-motion", html)
        self.assertIn("requestFullscreen", html)

    def test_script_injection_and_unknown_data_are_not_exported(self):
        self.data["title"] = "</script><script>alert(1)</script>"
        self.data["secret"] = "do-not-copy-private-metadata"
        self.data["stages"][0]["private"] = "do-not-copy-stage-metadata"
        html = builder.build_web(self.load(), self.root).read_text()
        self.assertNotIn("</script><script>alert", html)
        self.assertIn("\\u003c/script>", html)
        self.assertNotIn("do-not-copy", html)

    def test_reject_external_asset_and_symlink(self):
        self.data["stages"][0]["image"] = "../outside.png"
        with self.assertRaises((ValueError, FileNotFoundError)):
            self.load()
        link = self.root / "link.png"
        link.symlink_to(SOURCE)
        self.data["stages"][0]["image"] = "link.png"
        with self.assertRaises(ValueError):
            self.load()

    def test_reject_nonfinite_duration_negative_and_reversed_weeks(self):
        for value in (float("nan"), float("inf"), -1, True):
            self.data["stages"][0]["seconds"] = value
            with self.assertRaises(ValueError):
                self.load()
        self.data["stages"][0]["seconds"] = 1
        self.data["stages"][1]["week"] = -1
        with self.assertRaises(ValueError):
            self.load()

    def test_reject_html_disguised_as_image(self):
        (self.root / "one.png").write_text("<html>untrusted</html>")
        with self.assertRaises(ValueError):
            self.load()

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg integration unavailable")
    def test_real_mp4_keeps_outer_frame_visible_during_crossfade(self):
        font = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        if not font.exists():
            self.skipTest("Integration font unavailable")
        path = builder.build_mp4(self.load(), self.root, font)
        info = builder.verify_mp4(path)
        self.assertAlmostEqual(float(info["format"]["duration"]), 2, places=1)
        # Shell is drawn after blending. Its top-left background must retain its
        # brightness at the exact stage boundary and mid-crossfade.
        for second in (.9, 1.0, 1.3, 1.7):
            frame = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(second), "-i", str(path), "-vf", "crop=16:16:0:0,format=rgb24", "-frames:v", "1", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
            self.assertEqual(len(frame), 16 * 16 * 3)
            self.assertGreater(sum(frame) / len(frame), 20)


if __name__ == "__main__":
    unittest.main()
