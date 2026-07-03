from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping, Tuple

from PIL import Image

Color = Tuple[int, int, int]


def count_visible_key_pixels(image_path: Path, key: Color = (255, 0, 255), tolerance: int = 0) -> int:
    image = Image.open(image_path).convert("RGBA")
    kr, kg, kb = key
    count = 0
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            if abs(r - kr) <= tolerance and abs(g - kg) <= tolerance and abs(b - kb) <= tolerance:
                count += 1
    return count


def validate_manifest_rects(image_path: Path, frames: Iterable[Mapping[str, object]]) -> None:
    image = Image.open(image_path)
    width, height = image.size
    image.close()
    for frame in frames:
        rect = frame["rect"]  # type: ignore[index]
        x = int(rect["x"])  # type: ignore[index]
        y = int(rect["y"])  # type: ignore[index]
        w = int(rect["w"])  # type: ignore[index]
        h = int(rect["h"])  # type: ignore[index]
        if x < 0 or y < 0 or w <= 0 or h <= 0:
            raise ValueError(f"Invalid frame rect: {rect}")
        if x + w > width or y + h > height:
            raise ValueError(f"Frame rect outside image bounds: {rect}")
