from __future__ import annotations

from pathlib import Path
from typing import Tuple

from PIL import Image

Color = Tuple[int, int, int]


def parse_hex_color(value: str) -> Color:
    text = value.strip().lstrip("#")
    if len(text) != 6:
        raise ValueError(f"Expected 6-digit hex color, got {value!r}")
    return int(text[0:2], 16), int(text[2:4], 16), int(text[4:6], 16)


def chroma_key_image(image: Image.Image, key: Color = (255, 0, 255), tolerance: int = 24) -> Image.Image:
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    kr, kg, kb = key
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = pixels[x, y]
            if abs(r - kr) <= tolerance and abs(g - kg) <= tolerance and abs(b - kb) <= tolerance:
                pixels[x, y] = (r, g, b, 0)
    return rgba


def chroma_key_file(input_path: Path, output_path: Path, key: Color = (255, 0, 255), tolerance: int = 24) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = chroma_key_image(Image.open(input_path), key=key, tolerance=tolerance)
    result.save(output_path)
