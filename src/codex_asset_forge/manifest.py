from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from PIL import Image

from .grid import grid_rects


def build_grid_manifest(
    image_path: Path,
    columns: int,
    rows: int,
    layer: str = "base",
    prefix: str = "frame",
) -> Dict[str, Any]:
    with Image.open(image_path) as image:
        rects = grid_rects(image.width, image.height, columns, rows, prefix=prefix)
    return {
        "schemaVersion": 1,
        "image": str(image_path),
        "atlasGrid": {"columns": columns, "rows": rows},
        "frameSize": {"width": rects[0].w, "height": rects[0].h},
        "frames": [
            {
                "id": rect.id,
                "rect": {"x": rect.x, "y": rect.y, "w": rect.w, "h": rect.h},
                "anchor": {"x": rect.w // 2, "y": rect.h},
                "layer": layer,
            }
            for rect in rects
        ],
    }


def write_manifest(manifest: Dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
