from __future__ import annotations

from pathlib import Path
from typing import Sequence

from PIL import Image, ImageDraw, ImageFont


def build_contact_sheet(image_paths: Sequence[Path], output_path: Path, columns: int = 4, cell_size: int = 160) -> None:
    if not image_paths:
        raise ValueError("image_paths must not be empty")
    rows = (len(image_paths) + columns - 1) // columns
    pad = 16
    label_h = 24
    sheet = Image.new("RGBA", (columns * cell_size + pad * 2, rows * (cell_size + label_h) + pad * 2), (246, 244, 239, 255))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for idx, path in enumerate(image_paths):
        row, column = divmod(idx, columns)
        x = pad + column * cell_size
        y = pad + row * (cell_size + label_h)
        source = Image.open(path).convert("RGBA")
        source.thumbnail((cell_size - 24, cell_size - 24), Image.Resampling.NEAREST)
        px = x + (cell_size - source.width) // 2
        py = y + (cell_size - source.height) // 2
        sheet.alpha_composite(source, (px, py))
        draw.text((x + 8, y + cell_size), path.stem[:22], fill=(72, 78, 86), font=font)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
