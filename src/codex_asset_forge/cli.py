from __future__ import annotations

import argparse
import json
from pathlib import Path

from .chroma import chroma_key_file, parse_hex_color
from .grid import slice_grid_file
from .manifest import build_grid_manifest, write_manifest
from .preview import build_contact_sheet
from .qa import count_visible_key_pixels


def main() -> None:
    parser = argparse.ArgumentParser(prog="codex-asset-forge")
    sub = parser.add_subparsers(dest="command", required=True)

    key = sub.add_parser("key", help="remove a solid chroma-key background")
    key.add_argument("input", type=Path)
    key.add_argument("output", type=Path)
    key.add_argument("--key", default="ff00ff")
    key.add_argument("--tolerance", type=int, default=24)

    grid = sub.add_parser("slice-grid", help="slice an evenly spaced sprite grid")
    grid.add_argument("input", type=Path)
    grid.add_argument("output_dir", type=Path)
    grid.add_argument("--columns", type=int, required=True)
    grid.add_argument("--rows", type=int, required=True)
    grid.add_argument("--prefix", default="frame")

    manifest = sub.add_parser("manifest-grid", help="write a JSON manifest for an evenly spaced atlas")
    manifest.add_argument("input", type=Path)
    manifest.add_argument("output", type=Path)
    manifest.add_argument("--columns", type=int, required=True)
    manifest.add_argument("--rows", type=int, required=True)
    manifest.add_argument("--layer", default="base")
    manifest.add_argument("--prefix", default="frame")

    qa = sub.add_parser("qa-key", help="count visible chroma-key pixels")
    qa.add_argument("input", type=Path)
    qa.add_argument("--key", default="ff00ff")
    qa.add_argument("--tolerance", type=int, default=0)

    preview = sub.add_parser("contact-sheet", help="make a simple contact sheet")
    preview.add_argument("output", type=Path)
    preview.add_argument("images", type=Path, nargs="+")
    preview.add_argument("--columns", type=int, default=4)

    args = parser.parse_args()

    if args.command == "key":
        chroma_key_file(args.input, args.output, key=parse_hex_color(args.key), tolerance=args.tolerance)
        return
    if args.command == "slice-grid":
        rects = slice_grid_file(args.input, args.output_dir, columns=args.columns, rows=args.rows, prefix=args.prefix)
        print(json.dumps([rect.__dict__ for rect in rects], indent=2))
        return
    if args.command == "manifest-grid":
        data = build_grid_manifest(args.input, columns=args.columns, rows=args.rows, layer=args.layer, prefix=args.prefix)
        write_manifest(data, args.output)
        return
    if args.command == "qa-key":
        count = count_visible_key_pixels(args.input, key=parse_hex_color(args.key), tolerance=args.tolerance)
        print(count)
        return
    if args.command == "contact-sheet":
        build_contact_sheet(args.images, args.output, columns=args.columns)
        return

    raise AssertionError(args.command)
