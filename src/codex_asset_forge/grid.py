from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from PIL import Image


@dataclass(frozen=True)
class FrameRect:
    id: str
    x: int
    y: int
    w: int
    h: int


def grid_rects(width: int, height: int, columns: int, rows: int, prefix: str = "frame") -> List[FrameRect]:
    if columns <= 0 or rows <= 0:
        raise ValueError("columns and rows must be positive")
    frame_w = width // columns
    frame_h = height // rows
    if frame_w * columns != width or frame_h * rows != height:
        raise ValueError("image dimensions must divide evenly by columns and rows")
    rects: List[FrameRect] = []
    for row in range(rows):
        for column in range(columns):
            rects.append(
                FrameRect(
                    id=f"{prefix}_{row}_{column}",
                    x=column * frame_w,
                    y=row * frame_h,
                    w=frame_w,
                    h=frame_h,
                )
            )
    return rects


def slice_grid_file(input_path: Path, output_dir: Path, columns: int, rows: int, prefix: str = "frame") -> List[FrameRect]:
    image = Image.open(input_path).convert("RGBA")
    rects = grid_rects(image.width, image.height, columns, rows, prefix=prefix)
    output_dir.mkdir(parents=True, exist_ok=True)
    for rect in rects:
        frame = image.crop((rect.x, rect.y, rect.x + rect.w, rect.y + rect.h))
        frame.save(output_dir / f"{rect.id}.png")
    return rects
