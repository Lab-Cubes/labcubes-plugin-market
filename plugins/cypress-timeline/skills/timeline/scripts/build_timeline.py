#!/usr/bin/env python3
"""Build offline Web and MP4 progress reports from one validated timeline.

No models, package installation, network access, authentication or publication
occur here. Asset creation belongs to the selected provider; hosting to Sites.
"""
from __future__ import annotations

import argparse
import base64
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def load_timeline(path: Path) -> dict:
    """Validate text, finite timing and caller-owned local image boundaries."""
    path = path.resolve(strict=True)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Timeline must be an object")
    for field in ("title", "subtitle", "disclosure"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"{field} must be nonblank text")
        if len(data[field]) > 2000:
            raise ValueError(f"{field} is too long")
    stages = data.get("stages")
    if not isinstance(stages, list) or not 2 <= len(stages) <= 30:
        raise ValueError("Provide 2 to 30 ordered stages")
    default_seconds = 30.0 / len(stages)
    previous_week = -1.0
    total = 0.0
    for stage in stages:
        if not isinstance(stage, dict):
            raise ValueError("Each stage must be an object")
        for field in ("title", "label", "description", "image"):
            if not isinstance(stage.get(field), str) or not stage[field].strip():
                raise ValueError(f"Stage {field} must be nonblank text")
            if len(stage[field]) > 2000:
                raise ValueError(f"Stage {field} is too long")
        seconds = stage.get("seconds", default_seconds)
        week = stage.get("week")
        for name, value in (("seconds", seconds), ("week", week)):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f"{name} must be a finite number")
        if not 1 <= seconds <= 120 or week < 0 or week < previous_week:
            raise ValueError("Stage duration must be 1–120s and weeks nondecreasing")
        previous_week = week
        image = (path.parent / stage["image"]).resolve(strict=True)
        if not image.is_relative_to(path.parent) or not image.is_file():
            raise ValueError("Stage image must stay within the timeline directory")
        raw = image.read_bytes()
        if len(raw) > 20 * 1024 * 1024:
            raise ValueError("Stage image exceeds 20 MiB")
        if raw.startswith(b"\x89PNG\r\n\x1a\n"):
            mime = "image/png"
        elif raw.startswith(b"\xff\xd8\xff"):
            mime = "image/jpeg"
        elif raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
            mime = "image/webp"
        else:
            raise ValueError("Use PNG, JPEG or WebP images; SVG/HTML are not accepted")
        stage.update(path=str(image), mime=mime, seconds=float(seconds), start=total)
        total += seconds
    if total > 1800:
        raise ValueError("Timeline exceeds 30 minutes")
    # Avoid a 29-second end clock from floating-point summation of a 30s plan.
    data["duration"] = round(total, 9)
    data["image_fit"] = data.get("image_fit", "contain")
    if data["image_fit"] not in ("contain", "cover"):
        raise ValueError("image_fit must be contain or cover")
    return data


def build_web(data: dict, output: Path) -> Path:
    """Embed validated images and escaped data into a dependency-free HTML file."""
    public = {k: data[k] for k in ("title", "subtitle", "disclosure", "duration", "image_fit")}
    public["stages"] = []
    for stage in data["stages"]:
        item = {k: stage[k] for k in ("title", "label", "description", "week", "seconds", "start")}
        item["image"] = "data:" + stage["mime"] + ";base64," + base64.b64encode(Path(stage["path"]).read_bytes()).decode("ascii")
        public["stages"].append(item)
    encoded = json.dumps(public, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    template = (ROOT / "assets/player.html").read_text(encoding="utf-8")
    destination = output / "timeline.html"
    destination.write_text(template.replace("__TIMELINE_DATA__", encoded), encoding="utf-8")
    return destination


def run(command: list[str]) -> None:
    """Run an argument array without a shell and surface any failed subprocess."""
    subprocess.run(command, check=True, stdin=subprocess.DEVNULL)


def filter_path(path: Path) -> str:
    """Escape a local path for FFmpeg's single-quoted filter option grammar."""
    return str(path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "'\\''")


def verify_mp4(path: Path) -> dict:
    """Probe the real encoded file; reject missing video or nonpositive duration."""
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)], check=True, capture_output=True, text=True)
    data = json.loads(probe.stdout)
    if not any(s.get("codec_name") == "h264" for s in data["streams"]) or float(data["format"]["duration"]) <= 0:
        raise ValueError("Output is not a usable H.264 MP4")
    return data


def build_mp4(data: dict, output: Path, font: Path) -> Path:
    """Blend only main pictures, then draw stable chrome; output a silent 1080p MP4."""
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise ValueError("MP4 requires FFmpeg and ffprobe; no installation was attempted")
    if not font.is_file():
        raise ValueError("MP4 requires an explicit readable font with the requested language glyphs")
    limits = [(data["title"], 90), (data["subtitle"], 140), (data["disclosure"], 190)]
    for stage in data["stages"]:
        limits.extend([(stage["title"], 28), (stage["label"], 60), (stage["description"], 132)])
    # Approximate full-width glyphs as two columns; reject clipping instead of
    # silently exporting unreadable fixed-layout annotations.
    import unicodedata
    if any("\n" in text or sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text) > limit for text, limit in limits):
        raise ValueError("MP4 text exceeds its fixed layout; shorten text or adapt the composition")
    common = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    with tempfile.TemporaryDirectory(prefix="cypress-timeline-") as work:
        temp = Path(work)
        shutil.copyfile(font, temp / "font.ttf")
        for i, stage in enumerate(data["stages"]):
            if data["image_fit"] == "cover":
                fit = "scale=1800:640:force_original_aspect_ratio=increase,crop=1800:640"
            else:
                fit = "scale=1800:640:force_original_aspect_ratio=decrease,pad=1800:640:(ow-iw)/2:(oh-ih)/2:color=0x10212a"
            run(common + ["-i", stage["path"], "-vf", fit + ",setsar=1", "-frames:v", "1", str(temp / f"photo-{i}.png")])

        def text(value: str, name: str, x: int, y: int, size: int, color: str = "0xf5f0e7") -> str:
            target = temp / f"{name}.txt"
            target.write_text(value, encoding="utf-8")
            return f"drawtext=fontfile='{filter_path(temp / 'font.ttf')}':textfile='{filter_path(target)}':expansion=none:x={x}:y={y}:fontsize={size}:fontcolor={color}"

        for i, stage in enumerate(data["stages"]):
            # Smoothstep mixing never involves frame/title/status layers.
            ratio = "min(T/0.65,1)"
            mix = f"A*(1-({ratio}))+B*({ratio})"
            layers = ["pad=1920:1080:60:150:color=0x10212a",
                      text(data["title"], "header", 60, 38, 40),
                      text(data["subtitle"], "subtitle", 60, 96, 23, "0xa9bdc3"),
                      text(stage["title"], f"title-{i}", 60, 815, 44),
                      text(stage["label"], f"label-{i}", 800, 830, 28, "0x75d6b1"),
                      text(stage["description"], f"description-{i}", 60, 890, 25),
                      text(data["disclosure"], "disclosure", 60, 1030, 18, "0xa9bdc3"),
                      "drawbox=x=60:y=975:w=1800:h=5:color=0x35505a:t=fill",
                      f"drawbox=x=60:y=975:w={1800*(i+1)/len(data['stages'])}:h=5:color=0x75d6b1:t=fill",
                      "format=yuv420p"]
            graph = "[0:v][1:v]blend=all_expr='" + mix + "'[photo];[photo]" + ",".join(layers) + "[out]"
            graphfile = temp / f"filter-{i}.txt"
            graphfile.write_text(graph, encoding="utf-8")
            run(common + ["-loop", "1", "-framerate", "24", "-i", str(temp / f"photo-{max(0,i-1)}.png"), "-loop", "1", "-framerate", "24", "-i", str(temp / f"photo-{i}.png"), "-filter_complex_script", str(graphfile), "-map", "[out]", "-t", str(stage["seconds"]), "-an", "-c:v", "libx264", "-threads", "2", "-filter_complex_threads", "1", "-preset", "fast", "-crf", "20", str(temp / f"stage-{i}.mp4")])
        listing = temp / "concat.txt"
        listing.write_text("".join(f"file '{filter_path(temp / f'stage-{i}.mp4')}'\n" for i in range(len(data["stages"]))), encoding="utf-8")
        destination = output / "timeline.mp4"
        run(common + ["-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", "-movflags", "+faststart", str(destination)])
        verified = verify_mp4(destination)
        actual = float(verified["format"]["duration"])
        if abs(actual - data["duration"]) > len(data["stages"]) / 24 + .1:
            raise ValueError("Encoded duration does not match the planned timeline")
        return destination


def main() -> None:
    """Expose explicit output choices without silently dropping a requested format."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("--format", choices=("web", "mp4", "both"), default="both")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font", type=Path)
    args = parser.parse_args()
    data = load_timeline(args.spec)
    args.output.mkdir(parents=True, exist_ok=True)
    written = []
    if args.format in ("web", "both"):
        written.append(str(build_web(data, args.output)))
    if args.format in ("mp4", "both"):
        if args.font is None:
            parser.error("--font is required for MP4; any completed Web output remains available")
        written.append(str(build_mp4(data, args.output, args.font)))
    print(json.dumps({"outputs": written, "duration_seconds": data["duration"]}))


if __name__ == "__main__":
    main()
