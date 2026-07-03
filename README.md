# Codex Asset Forge

Codex Asset Forge is a small, engine-agnostic toolkit and case study for turning
AI-generated pixel-art drafts into game-ready asset artifacts.

The core idea is simple:

```text
image_gen raw art on #FF00FF
  -> chroma-key transparency
  -> deterministic grid slicing
  -> atlas PNG + manifest JSON
  -> collision / layer metadata
  -> runtime proof
  -> human visual acceptance
```

The project is not a promise that AI output is final art. It is a workflow for
making generated output auditable, repeatable, and safe to hand to an engine.

## Why This Exists

Generated images are not game assets yet. A runtime needs frame rectangles,
layers, anchors, collision metadata, fallback behavior, and proof that the asset
was actually drawn. This repository packages that idea as a lightweight CLI,
sample assets, and a portfolio case study.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

codex-asset-forge key examples/agentforge-starter/raw/tileset_raw.png /tmp/tileset_keyed.png
codex-asset-forge slice-grid /tmp/tileset_keyed.png /tmp/tiles --columns 2 --rows 2 --prefix tile
codex-asset-forge manifest-grid /tmp/tileset_keyed.png /tmp/tileset.json --columns 2 --rows 2 --layer base
python -m unittest discover -s tests -v
```

## Repository Map

```text
src/codex_asset_forge/      Python CLI and reusable helpers
tests/                      standard-library unittest checks
examples/                   generated sample assets and proof artifacts
docs/index.html             portfolio / case-study page
docs/portfolio-assets/      images used by the page
NOTICE.md                   provenance and claim boundaries
```

## Case Study

The GitHub Pages site is the public-facing case-study draft:

- `docs/index.html`
- `docs/codex-asset-pipeline-portfolio-inventory.md`
- `docs/codex-asset-pipeline-fde-blog-draft.md`

The page frames the project as FDE-style work: taking an ambiguous asset
production bottleneck and turning it into a reusable automation contract with
visible runtime proof.

## Claim Boundaries

Safe:

- Built a raw-to-atlas asset pipeline using generated input and deterministic
  postprocessing.
- Produced sample atlases, manifests, collision/layer metadata, and proof
  artifacts.
- Demonstrated visible-map sprite rendering in a related ClaudeCraft proof.

Not claimed:

- final art quality
- user acceptance of all visuals
- fully automatic final asset production
- shipped or store-ready game art
- proprietary ownership over third-party or GPL-covered material

## License

MIT. See `LICENSE` and `NOTICE.md`.
