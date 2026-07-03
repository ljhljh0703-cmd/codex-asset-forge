from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from codex_asset_forge.chroma import chroma_key_file
from codex_asset_forge.grid import grid_rects, slice_grid_file
from codex_asset_forge.manifest import build_grid_manifest
from codex_asset_forge.qa import count_visible_key_pixels, validate_manifest_rects


class PipelineTests(unittest.TestCase):
    def test_chroma_key_makes_magenta_transparent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "raw.png"
            output = root / "keyed.png"
            image = Image.new("RGBA", (4, 4), (255, 0, 255, 255))
            image.putpixel((1, 1), (20, 40, 60, 255))
            image.save(source)

            chroma_key_file(source, output, tolerance=0)

            result = Image.open(output).convert("RGBA")
            self.assertEqual(result.getpixel((0, 0))[3], 0)
            self.assertEqual(result.getpixel((1, 1)), (20, 40, 60, 255))
            self.assertEqual(count_visible_key_pixels(output), 0)

    def test_grid_slice_and_manifest_rects(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "atlas.png"
            image = Image.new("RGBA", (8, 4), (0, 0, 0, 0))
            image.save(source)

            rects = slice_grid_file(source, root / "frames", columns=4, rows=2, prefix="tile")
            self.assertEqual(len(rects), 8)
            self.assertEqual((root / "frames" / "tile_0_0.png").exists(), True)

            manifest = build_grid_manifest(source, columns=4, rows=2, layer="base", prefix="tile")
            self.assertEqual(manifest["frameSize"], {"width": 2, "height": 2})
            validate_manifest_rects(source, manifest["frames"])
            json.dumps(manifest)

    def test_grid_rejects_uneven_dimensions(self) -> None:
        with self.assertRaises(ValueError):
            grid_rects(7, 4, columns=4, rows=2)


if __name__ == "__main__":
    unittest.main()
