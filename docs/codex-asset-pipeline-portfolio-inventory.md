---
type: portfolio-evidence-inventory
status: DRAFT_NOT_ACCEPTED
date: 2026-07-03
topic: codex-asset-pipeline-open-source-portfolio
owner_lane: Portfolio / Applications
write_policy: repo_local_packet_no_vault_write
---

# Codex Asset Pipeline OSS/Portfolio Inventory

This packet gathers the asset-generation pipeline the user has been building
through Codex sessions and Vault knowledge. It is meant as source material for a
future GitHub open-source package and a portfolio HTML page.

Status: `DRAFT_NOT_ACCEPTED`. This is content inventory and positioning, not
public release, not visual acceptance, and not a Vault skill promotion.

## One-Line Thesis

Codex can be used as an asset-production worker for 2D game projects when raw
image generation is separated from deterministic postprocessing, manifest
contracts, runtime proof, and human acceptance gates.

Applicant-facing wording:

> Built an AI-assisted 2D game asset pipeline that turns generated raw pixel art
> into transparent sprites, sliced atlases, manifest metadata, collision/layer
> contracts, and browser/runtime proof artifacts.

Do not frame it as "fully automatic final art production." The stronger and
more accurate claim is a controlled production workflow with measurable gates.

## Scope

Included:

- Vault asset-generation methods and skill knowledge.
- Codex sessions that generated or routed game assets.
- Existing portfolio HTML evidence and claim boundaries.
- A proposed open-source repo shape.
- A proposed HTML/case-study structure.

Not included:

- No Vault skill creation or modification.
- No public GitHub push.
- No HTML implementation in this pass.
- No claim that user visual/fun acceptance has happened.

## Source Authority Read

Repo and portfolio:

- `AGENTS.md`
- `docs/portfolio-application-bridge.md`
- `docs/portfolio-evidence-ledger.md`
- `ops/status.json`
- `ops/handoff.md`

Vault and memory:

- Sub-brain root `AGENTS.md`
- `wiki/learnings/methods/agent-sprite-forge.md`
- `wiki/learnings/methods/sprite-gen-skill.md`
- `wiki/learnings/techniques/perfectpixel-sprite-pipeline.md`
- `wiki/learnings/methods/aseprite-automation.md`
- `wiki/learnings/techniques/pixel-art-game-assets.md`
- `wiki/learnings/techniques/opengame.md`
- `wiki/projects/game-studio-pipeline-brief.md`
- `wiki/projects/libgdx-rogue-os-art-guide.md`
- `skills/html-publish/GUIDE.md`
- Codex memory entries for prior asset/portfolio sessions.

Prior local evidence:

- `/Users/godju/Downloads/AI AGENT/Old Project/Game Planning-Agent/_dev/RETURN-codex-asset.md`
- `/Users/godju/Downloads/AI AGENT/Old Project/Game Planning-Agent/public/assets/agentforge/`
- `/Users/godju/Downloads/AI AGENT/Old Project/Game Planning-Agent/docs/portfolio.html`
- `/Users/godju/Downloads/AI Game/ClaudeCraft/exports/RETURN-2026-06-28-r020-tile-item-sprites.md`
- `/Users/godju/Downloads/AI Game/ClaudeCraft/derived-source/world-of-claudecraft-renewed/artifacts/phase-d/r020-tile-item-sprite-proof.json`
- `/Users/godju/Documents/Codex/2026-06-30/ai-game-dev-os-portfolio/outputs/2026-07-02-game-portfolio-html-artifact-inventory.md`
- Local libGDX asset docs under `docs/asset-*.md` and `docs/voxel-turnaround-prepass-harness.md`.

## Pipeline Pattern

Canonical pattern:

```text
asset request / style contract
  -> built-in image_gen raw image on solid #FF00FF
  -> chroma-key / matting to transparency
  -> deterministic grid slicing or component extraction
  -> frame normalization, anchors, palette / QC
  -> atlas PNG + machine-readable manifest JSON
  -> collision / layer / scene metadata
  -> runtime loader or renderer integration
  -> proof: build + harness + visible/reachability check
  -> human visual/fun verdict
```

Key rule: generated pixels are not the source of truth. The source of truth is
the manifest plus proof that the engine consumed the asset correctly.

## Vault Knowledge Map

### agent-sprite-forge

Usable method:

- Raw art comes from Codex built-in `image_gen`.
- Postprocessing is local and deterministic: magenta keying, frame split, bbox
  alignment, atlas assembly, QC.
- Multi-cell character sheets should not be 1xN single rows. Use 2x2, 2x3,
  3x3, or 4x4 grids to reduce drift.
- Body-only animation and FX should be separated.
- Runtime map objects should be classified before generation:
  `compact_prop`, `wide_or_long`, `tall_or_large`, `collision_bearing`,
  `tileset_or_strip_piece`.
- Square prop packs are only for compact props. Floor, wall, stairs, doors,
  platforms, long traps, and collision-aligned pieces require tilesets, strips,
  one-by-one cells, or custom atlas pieces.
- Layers are a gameplay contract: base terrain, props, actors, FX, collision,
  and scene hooks should remain separate.
- Reference mockups are checkpoints, not final deliverables.

Portfolio value:

This gives the clearest reusable methodology for "Codex as sprite forge."

### sprite-gen-skill

Usable method:

- A numeric request JSON drives prompt, extraction, atlas, and QA.
- Runtime manifest contains absolute frame rectangles. The engine should sample
  rectangles from metadata, not guess a grid or reconstruct frames from alpha.
- Idle anchor owns identity; motion rows should not reattach full base art in a
  way that reopens identity drift.
- Curation should be a non-destructive sidecar.
- Label weak or unproven motion states honestly as experimental.
- Run-directory locks prevent two agents writing one asset folder concurrently.

Portfolio value:

This turns "AI generated sprites" into an engineering contract: request SSoT,
manifest SSoT, sidecar curation, and honest status labels.

### PerfectPixel Sprite Pipeline

Usable method:

- AI generation is non-deterministic; deterministic postprocessing makes output
  auditable.
- YCbCr/background-mode matting is more robust than naive RGB thresholds.
- Projection-profile and DP splitting can recover frames when equal grid split
  would cut through poses.
- Alpha-weighted centroid alignment reduces jitter.
- Shared palette quantization and pixel-grid snap prevent frame flicker.
- Closed-loop scoring can retry with measured hints.

Portfolio value:

This supplies the "why" behind the pipeline: non-deterministic generation plus
deterministic gates.

### Aseprite Automation

Usable method:

- Aseprite can be used headlessly with `--sheet` and `--data`.
- Output should be PNG sheet plus JSON metadata containing frame rectangles,
  tags, slices, and durations.
- `--list-tags --format json` and related introspection commands can become
  self-QA.
- Aseprite is not OSS in the same way as MIT/Apache tools, so it is best framed
  as optional refinement/export tooling, not a required open-source dependency.

Portfolio value:

It shows compatibility with industry-standard pixel-art tooling while keeping
the open-source core independent.

### Pixel-Art Game Assets

Usable method:

- Collision boxes must stay separate from sprite squash/stretch.
- Dungeon tile grammar should distinguish render layer and collision/object
  layer.
- Seamless tiles need 2x2 or 3x3 repeat previews.
- AI output is a draft: palette lock, orphan/banding cleanup, silhouette/light
  consistency, frame jitter cleanup, and provenance gate are required before
  final use.

Portfolio value:

This keeps the project from claiming mere generated images as finished game art.

### OpenGame / Game Studio Pipeline

Usable method:

- Game production can be framed as `Classify -> Scaffold -> GDD -> Assets ->
  Config -> Code -> Verify`.
- Asset keys must stay consistent across asset pack, animation metadata, and
  code.
- The user's game-studio brief maps the asset stage to PerfectPixel and
  agent-sprite-forge, with Codex `image_gen` absorbing the asset bottleneck when
  available.

Portfolio value:

This connects asset production to the larger "AI-assisted game studio" story,
not just isolated art generation.

### libGDX Art Guide

Usable method:

- Visual identity is high-contrast dungeon pixel art with restrained accent
  colors.
- Floor/wall tiles, actors, UI, and FX need different rules.
- DoD includes palette control, orphan removal, seamless tile checks, atlas
  naming, collision separation, and consistent upper-left light.
- Engine export contract is sprite-sheet PNG plus machine-readable JSON
  metadata. Repo loader format must be verified before hard-locking a format.

Portfolio value:

This is the local bridge from abstract asset pipeline to the Bone Trail /
libGDX project.

### html-publish

Usable method:

- HTML should be built from a clear source/config plan, not improvised as an
  untracked one-off.
- A portfolio page needs a visual thesis, content plan, system declaration, and
  effect budget before writing layout.
- Lint/build steps should distinguish generated HTML from source truth.

Portfolio value:

This gives the next phase a page-production protocol instead of another
one-off HTML.

## Codex Evidence Inventory

### 1. AgentForge Starter Asset Pack

Root:

- `/Users/godju/Downloads/AI AGENT/Old Project/Game Planning-Agent`

Key files:

- `_dev/CODEX-asset-gen.md`
- `_dev/RETURN-codex-asset.md`
- `public/assets/agentforge/raw/*.png`
- `public/assets/agentforge/keyed/*.png`
- `public/assets/agentforge/atlas/*.png`
- `public/assets/agentforge/atlas/*.json`
- `public/assets/agentforge/manifest.json`
- `public/assets/agentforge/qc.json`
- `src/assets/asset-loader.ts`
- `docs/portfolio.html`

Recorded result:

- Built a starter asset pack using built-in `image_gen`.
- Raw images used solid `#FF00FF` background.
- Postprocess converted to transparent keyed sheets.
- Produced 5 atlases: tileset, player, enemy slime, FX, props.
- Produced 27 frames total.
- Wrote collision metadata and scene hook metadata.
- Added a Canvas atlas loader seed.
- `npm run type-check` PASS.
- `npm run build` PASS.
- Manifest validation PASS: `atlases=5`, `frames=27`.
- `jq empty` over manifest/atlas/QC JSON PASS.
- Visible magenta residue was recorded as 0 in `qc.json`.
- Secret scan output 0.

Boundary:

- This is a starter pack plus loader seed.
- It is not yet a fully automatic game-template asset injection pipeline.
- `docs/asset-preview.png` was listed in the RETURN, but was not present during
  this inventory check. The asset files and manifest are present.

Portfolio use:

Strong evidence for the generic open-source package: raw -> key -> slice ->
atlas -> manifest -> loader.

### 2. ClaudeCraft R020 Tile / Item Sprite Conversion

Root:

- `/Users/godju/Downloads/AI Game/ClaudeCraft`

Key files:

- `exports/RETURN-2026-06-28-r020-tile-item-sprites.md`
- `derived-source/world-of-claudecraft-renewed/src/render/canvas.ts`
- `derived-source/world-of-claudecraft-renewed/public/sprites/sprites.json`
- `derived-source/world-of-claudecraft-renewed/assets/assets-manifest.json`
- `derived-source/world-of-claudecraft-renewed/public/sprites/tile/*/idle.png`
- `derived-source/world-of-claudecraft-renewed/public/sprites/item/*/idle.png`
- `derived-source/world-of-claudecraft-renewed/artifacts/phase-d/r020-tile-item-sprite-proof.json`
- `derived-source/world-of-claudecraft-renewed/artifacts/phase-d/r020-tile-item-sprite-proof.png`

Generated assets:

- Tiles: `crypt_floor`, `crypt_wall`, `mire_floor`, `mire_wall`,
  `stairs_down`, `stairs_up`, `stairs_down_locked`.
- Items: `minor_healing_potion`, `eastbrook_arming_sword`,
  `gatekeeper_relic`, `mire_lock_pearl`.

Recorded result:

- Converted the remaining glyph-rendered dungeon tiles and ground items to
  sprite-first rendering.
- Kept glyph fallback path.
- Did not touch player/enemy sprite path.
- Added tile/item manifest entries using the existing sprite manifest pattern.
- Added `lastTileSpriteProofs` and `lastItemSpriteProofs`.
- `npm run build` PASS.
- `python3 scripts/verify_harness.py` PASS.
- Playwright proof PASS against visible map route.
- Every in-scope tile/item asset key had `spriteRendered:true`.
- `failures: []`, `consoleErrors: []`, `glyphFallbacksAllowed: []`.

Reachability evidence:

- The proof JSON records 11 rendered asset keys.
- All 7 tile keys and all 4 item keys were loaded and sprite-rendered.
- This is stronger than a manifest load test because it proves visible draw
  path usage.

Boundary:

- `PROOF_READY_NOT_ACCEPTED`.
- Technical rendering proof is not visual/fun acceptance.

Portfolio use:

Best runtime proof case. Use it to show the pipeline can replace glyphs in an
existing game renderer without inventing a new harness.

### 3. libGDX Rogue OS Asset Pipeline Docs

Root:

- `/Users/godju/Downloads/AI Game/libgdx-rogue-os`

Key files:

- `docs/asset-pipeline-0a.md`
- `docs/asset-preproduction-0b.md`
- `docs/asset-production-0c.md`
- `docs/asset-production-0d.md`
- `docs/asset-voxel-turnaround-prepass.md`
- `docs/voxel-turnaround-prepass-harness.md`

Recorded result:

- 0A defines a design-only illustration-to-pixel-art pipeline.
- 0B defines a preproduction register and approval states.
- 0C produced review-only placeholder PNGs and preview sheets.
- 0D produced review-only HUD/content support placeholder PNGs and preview
  sheets.
- Voxel turnaround prepass defines an upstream 2D-reference -> voxel visual hull
  -> 8-direction/contact-sheet -> sprite cleanup route.
- The harness has proof for `tile_warp_gate_01` including validation commands,
  canonical sprite sheet, cleanup preview, runtime preview copy, palette count,
  and desktop smoke commands.

Important boundary:

- Most libGDX asset work is `REVIEW_ONLY_NOT_ACCEPTED` or
  `RUNTIME_PREVIEW_EXPORTED_REVIEW_ONLY`.
- It is not final art.
- It is evidence for an asset governance pipeline.

Portfolio use:

Use this as the "production governance" case: approval states, source/license
checks, review folders, preview sheets, and runtime promotion boundaries.

### 4. Existing Game Portfolio HTML Inventory

Key file:

- `/Users/godju/Documents/Codex/2026-06-30/ai-game-dev-os-portfolio/outputs/2026-07-02-game-portfolio-html-artifact-inventory.md`

Recorded public artifacts:

- BackRoom playable page:
  `https://ljhljh0703-cmd.github.io/backroom-level-0-godot/`
- BackRoom portfolio page:
  `https://ljhljh0703-cmd.github.io/backroom-level-0-godot/portfolio.html`
- Bone Trail game page:
  `https://ljhljh0703-cmd.github.io/bone-trail/`
- Bone Trail technical page:
  `https://ljhljh0703-cmd.github.io/bone-trail/technical.html`

Recorded state:

- BackRoom and Bone Trail were live HTTP 200 in that inventory.
- Bone Trail `docs/index.html` and
  `docs/libgdx-rogue-os-portfolio-public.html` were byte-identical.
- Bone Trail technical page was separate.
- hwigi-tower expected portfolio HTML was missing.

Portfolio use:

This is the model for the future asset-pipeline HTML inventory: separate public
pages, technical case study, internal evidence draft, live URL validation, and
claim guards.

### 5. AgentForge Portfolio HTML

Key file:

- `/Users/godju/Downloads/AI AGENT/Old Project/Game Planning-Agent/docs/portfolio.html`

Recorded memory:

- This repo maps to `https://github.com/ljhljh0703-cmd/agent-forge.git`.
- `docs/portfolio.html` is the tracked portfolio target path.
- A prior Codex session found the provided source and `docs/portfolio.html`
  already identical with SHA-256
  `49f0913d1f41dc6ccea38977c19f4f1e433b4ef4d2288bc966b491c91be25cf6`.

Portfolio use:

This is likely the "recent similar HTML" the user remembered. It should be
used as a comparison/reference, not blindly overwritten.

## Proposed Open-Source Package

Working repo names:

- `codex-asset-forge`
- `agent-sprite-forge-codex-kit`
- `ai-game-asset-pipeline`

Recommended public framing:

> A small, engine-agnostic toolkit and case study for converting AI-generated
> pixel-art drafts into game-ready sprite atlases with deterministic
> postprocessing, metadata, and runtime proof.

Suggested structure:

```text
README.md
LICENSE
NOTICE.md
docs/
  pipeline.md
  asset-contract.md
  case-study-agentforge.md
  case-study-claudecraft.md
  case-study-libgdx-review-gates.md
  html/
    index.html
examples/
  agentforge-starter/
    raw/
    keyed/
    atlas/
    manifest.json
    qc.json
  claudecraft-tile-item/
    sprites/
    proof.json
    proof.png
  libgdx-voxel-prepass/
    manifest-example.json
    preview-example.md
src/
  chroma_key.py
  slice_grid.py
  atlas_manifest.py
  qa_preview.py
  asset_loader.ts
tests/
  test_chroma_key.py
  test_manifest_rects.py
  test_no_magenta_residue.py
  test_sample_atlas_bounds.py
```

Open-source boundaries:

- Do not vendor Aseprite.
- Do not include GPL-covered Shattered Pixel Dungeon assets/text as original.
- Keep generated images with provenance metadata.
- Include generated raw images only when the user is comfortable publishing
  them.
- Separate sample assets from pipeline code.
- If any asset descends from a third-party pack, include source URL, license,
  derivative status, and approval state.

Minimum useful release:

- `chroma_key.py`
- `slice_grid.py`
- `atlas_manifest.py`
- `qa_preview.py`
- one small sample asset pack
- manifest schema
- tests for alpha, frame bounds, and metadata consistency
- an HTML case-study page

## Proposed HTML Page

Target role:

- Technical portfolio page, not marketing-only landing page.
- It should show the pipeline, proof artifacts, and boundaries.

Possible title:

- `Codex Asset Forge`
- `AI Game Asset Pipeline`
- `From Generated Pixels to Runtime Proof`

Suggested sections:

1. Hero: one sentence thesis plus a real atlas/proof image.
2. Problem: AI images are not game assets until sliced, keyed, named, anchored,
   and proven in runtime.
3. Pipeline: raw -> key -> slice -> atlas -> manifest -> loader -> proof.
4. Case Study A: AgentForge starter pack.
5. Case Study B: ClaudeCraft glyph-to-sprite runtime proof.
6. Case Study C: Bone Trail/libGDX review-only asset governance.
7. Contract: manifest schema, layer/collision rules, status vocabulary.
8. Open-source package: repo shape, tests, license/provenance.
9. Limits: visual quality remains HITL, no final art claim, no automatic fun
   proof.

Visual direction:

- Do not use ParkDal as the visual baseline for this new portfolio work.
- Use a technical product/case-study feel: dark neutral base, sharp atlas
  grids, compact evidence tables, proof badges, and actual generated images.
- Avoid vague AI imagery. Show the sprites, atlases, proof JSON excerpts, and
  before/after glyph/sprite comparison.

HTML proof requirements before public use:

- Local HTML parse/lint PASS.
- All local image references resolved.
- If deployed, public URL returns HTTP 200.
- Public images return HTTP 200.
- Claim guard section remains visible or linked.

## Public Claim Ledger

Safe claims:

- Built a Codex-assisted asset pipeline that uses generated raw art plus
  deterministic postprocessing.
- Produced raw, keyed, atlas, manifest, collision, scene hook, and QC artifacts
  in AgentForge.
- Converted ClaudeCraft tile/item glyph rendering to sprite-first rendering
  with Playwright visible-map proof.
- Designed libGDX/Bone Trail asset preproduction gates with review-only states,
  source approval checks, preview sheets, and runtime-promotion boundaries.
- Maintained proof-vs-acceptance separation.

Careful claims:

- "Game-ready" only for assets proven in a runtime draw path.
- "Open-source pipeline" only after the new repo has license, tests, and public
  push.
- "Portfolio page" only after HTML exists and references are verified.
- "AI-generated" should be paired with provenance and postprocessing.

Do not claim:

- Final visual quality or user acceptance.
- Store-ready or shipped game art.
- Fully automatic final asset pipeline.
- Proprietary ownership over GPL-covered combined distribution.
- Shattered Pixel Dungeon assets/text as project-original.
- That tests prove fun.

## Skill Candidate

```text
[Skill candidate] codex-asset-forge
[Basis] agent-sprite-forge, sprite-gen-skill, PerfectPixel, Aseprite automation, pixel-art-game-assets, ClaudeCraft R020 proof, AgentForge codex-asset RETURN, libGDX asset preproduction docs.
[Workflow] image_gen raw on #FF00FF -> chroma-key/matting -> grid or component slice -> frame normalization/anchors -> atlas + manifest -> collision/layer metadata -> QC preview -> runtime reachability proof -> HITL visual verdict.
[Why skill] The workflow has now repeated across AgentForge, ClaudeCraft, and libGDX/Bone Trail planning. It has enough rules and failure modes that a reusable skill would prevent ad hoc asset generation and overclaiming.
[Proposed location] /Users/godju/.codex/skills/codex-asset-forge/SKILL.md
[Needs approval] yes
```

Vault boundary: Codex should not create or modify the Vault skill directly.
Vault Claude/user approval should decide promotion.

## Next Route

Recommended next user decision:

1. Choose whether the open-source repo should be generic (`codex-asset-forge`)
   or tied to AgentForge.
2. Decide which generated assets are safe to publish as samples.
3. Choose license for the toolkit code.
4. Route a new implementation pass to create the repo package and HTML.

Recommended implementation gate for the next pass:

- Build code package with tests.
- Include one sanitized sample pack.
- Generate one local HTML page.
- Verify HTML local references.
- Push only after user approves public scope.
- If deployed, verify live URLs and image assets.

## Risks / Gaps

- AgentForge `docs/asset-preview.png` was listed in RETURN but not found during
  this inventory; verify before using it in HTML.
- Some Vault notes are provisional. The doc should treat them as methods and
  not as user-confirmed authority unless their status is confirmed.
- libGDX/Bone Trail asset outputs are mostly review-only and should not be
  presented as final art.
- The future OSS package needs clean license separation before publishing.
- Technical gate PASS remains separate from visual/fun quality.
