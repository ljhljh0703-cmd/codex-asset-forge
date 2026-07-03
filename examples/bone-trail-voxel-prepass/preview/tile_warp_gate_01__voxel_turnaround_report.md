# tile_warp_gate_01 Voxel Turnaround Prepass Report

Status: REVIEW_ONLY_NOT_ACCEPTED

Prepass review state: `VOXEL_PREPASS_REVIEW_READY`

## Source

- assetId: `tile_warp_gate_01`
- class: `tile_symbol_32`
- approvalState: `READY_FOR_CONVERSION_ORDER`
- sourceOwner: `project_authored`
- derivativePolicy: `review_only_prototype_generated_for_this_repo`

## Source Hashes

- front: `67522dcc7612e639cdf1cb859ceaada1b0768aa6cf6dd110029ae78e890ddf0b`
- side: `c5561f7bd3fe7d0524599e1c93c4a8430736e880335bc9ae3c9999c734921f52`

## Quality Gate

- source preflight: `SOURCE_QUALITY_PREFLIGHT_PASS`
- manual review gate: `PASS_REVIEW_WORTHY_NOT_PLACEHOLDER_EQUIVALENT`
- sheet hash: `565929aa417bf98ddfab245923e0b734b9112a2c56ba7ca0f32ee8f5931171e7`
- note: The contact sheet shows distinct front, side, and diagonal volume; this is a Tooling OS review reference, not cleaned runtime pixel art.

## Surface

- gridResolution: `[48, 48, 48]`
- occupiedVoxels: `15194`
- surfaceVoxels: `5664`

## Outputs

- turnaroundSheet: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/preview/tile_warp_gate_01__voxel_turnaround_sheet__v001.png`
- canonicalSpriteSheet: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/preview/tile_warp_gate_01__canonical_sprite_candidates__v001.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__front__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__front_right__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__right__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__back_right__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__back__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__back_left__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__left__prepass.png`
- render: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/renders/tile_warp_gate_01__front_left__prepass.png`

## Canonical Sprite Cleanup Set

- front: authored/cleaned frame
- back: authored/cleaned frame
- side_right: authored/cleaned frame
- side_left: mirror of `side_right`
- actor detail policy: Base actor sprites must not bake weapon hand, bag side, bandage position, or other left/right equipment details into the body silhouette.

The 8-direction sheet remains a volume review aid. It is not the runtime direction count.

## Cleanup Runtime Preview

- status: `REVIEW_RUNTIME_PREVIEW_NOT_ACCEPTED`
- cleanupManifest: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/cleanup/cleanup-manifest.json`
- cleanupPreviewSheet: `tools/asset-pipeline/voxel-turnaround-prepass/tile_warp_gate_01/preview/tile_warp_gate_01__cleanup_preview__v001.png`
- runtimePreviewCopy: `assets/sprites/tile_warp_gate.png`
- runtimePreviewCopySha256: `c5a1ee3f6ee6807ebda44d208dc687086876e8826872d56afc6353e4c48a99cd`
- reviewCopy: `assets/review/voxel-turnaround/tile_warp_gate_01/tile_warp_gate_01.png`
- reviewCopySha256: `c5a1ee3f6ee6807ebda44d208dc687086876e8826872d56afc6353e4c48a99cd`

## Boundary

- This is a Tooling OS review reference, not runtime voxel rendering.
- This does not approve final art, source conversion for other assets, or runtime export.
- Palette limits are checked after pixel cleanup, not claimed from this prepass output.
- Runtime export still requires preview review and a separate Command Center route.
