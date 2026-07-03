---
type: technical-blog-draft
status: DRAFT_NOT_ACCEPTED
date: 2026-07-03
topic: codex-asset-pipeline-fde
source_html: docs/codex-asset-pipeline-fde-portfolio.html
---

# AI는 그림을 만들고, 파이프라인은 게임 자산을 만든다

> 포트폴리오/기술 블로그 겸용 초안. 공개 전에는 이미지 공개 범위, OSS repo 이름, 라이선스, claim guard를 다시 확인한다.

## 한 줄 요약

Codex image_gen으로 만든 raw pixel art를 투명 스프라이트, atlas, manifest, collision metadata, runtime proof까지 연결했다. 핵심은 예쁜 그림이 아니라, 생성물을 실제 제품 경로에 넣기 위한 자동화 파이프라인이다.

## 타깃 독자

- AI/FDE/플랫폼 엔지니어 채용 담당자
- AI 자동화 파이프라인을 보는 기술 면접관
- 게임 개발 도메인 지식은 약하지만 "현장 문제를 시스템으로 바꾸는 능력"을 보고 싶은 사람

## 제목 후보

1. AI는 그림을 만들고, 파이프라인은 게임 자산을 만든다
2. 생성 이미지에서 런타임 proof까지: Codex Asset Forge 만들기
3. AI output을 제품 자산으로 바꾸는 FDE식 자동화 파이프라인
4. PNG 한 장은 게임 에셋이 아니다

## 이미지 배치

1. Hero / 대표 이미지
   - `docs/portfolio-assets/codex-asset-pipeline/claudecraft-tile-item-proof.png`
   - 목적: 실제 런타임 proof가 있는 사례를 첫 화면에 둔다.

2. 파이프라인 출력 이미지
   - `docs/portfolio-assets/codex-asset-pipeline/agentforge-tileset.png`
   - `docs/portfolio-assets/codex-asset-pipeline/agentforge-player.png`
   - `docs/portfolio-assets/codex-asset-pipeline/agentforge-slime.png`
   - `docs/portfolio-assets/codex-asset-pipeline/agentforge-props.png`
   - 목적: raw -> atlas 결과를 한눈에 보여준다.

3. ClaudeCraft R020 생성 asset 이미지
   - `docs/portfolio-assets/codex-asset-pipeline/claudecraft-r020-tile-sprites.png`
   - `docs/portfolio-assets/codex-asset-pipeline/claudecraft-r020-tile-item-sprites.png`
   - 목적: proof screenshot만이 아니라 실제 생성된 tile/item asset을 보여준다.

4. Review-only governance 이미지
   - `docs/portfolio-assets/codex-asset-pipeline/voxel-turnaround-sheet.png`
   - `docs/portfolio-assets/codex-asset-pipeline/voxel-candidates.png`
   - `docs/portfolio-assets/codex-asset-pipeline/class-avatar-preview-sheet.png`
   - 목적: 최종 아트와 review artifact를 구분하는 게이트를 보여준다.

5. Bone Trail runtime context
   - `docs/portfolio-assets/bone-trail-runtime-gameplay-hud-p1.png`
   - 목적: 이 자동화가 고립된 툴이 아니라 실제 게임 개발 OS의 일부임을 보여준다.

## 글 구조

### 1. 도입: AI가 이미지를 만들어줬는데, 왜 바로 못 쓰지?

AI로 픽셀아트 이미지를 뽑으면 처음에는 일이 끝난 것처럼 보인다.  
그런데 게임 엔진 입장에서는 아직 아무것도 끝나지 않았다.

배경은 투명해야 한다. 프레임은 잘려 있어야 한다. 캐릭터의 발 위치나 타일의 충돌 여부도 알아야 한다. 무엇보다 실제 화면에 그려졌다는 증거가 있어야 한다.

이때부터 문제는 "그림 생성"이 아니라 "자산 생산 파이프라인"이 된다.

### 2. 문제 정의: PNG 한 장은 게임 에셋이 아니다

게임 에셋은 단순한 이미지가 아니다. 엔진이 이해할 수 있는 계약이다.

이 계약에는 최소한 다음이 필요하다.

- 어떤 이미지에서 어느 사각형을 잘라 쓸 것인가
- 어떤 layer에 그릴 것인가
- 충돌이 있는가
- 프레임 anchor는 어디인가
- fallback이 발생했는가
- 실제 runtime draw path를 탔는가

이 정보가 없으면 이미지는 사람에게만 그럴듯하다. 엔진에는 불친절하다.

### 3. 해결 방식: 생성 모델을 믿지 말고, 후처리를 결정론적으로 만든다

이번 파이프라인은 생성 모델을 만능으로 보지 않았다.

Codex built-in image_gen은 raw art를 만든다. 그 뒤는 결정론적 파이프라인이 맡는다.

```text
asset request / style contract
  -> image_gen raw image on #FF00FF
  -> chroma-key to transparent
  -> deterministic grid slicing
  -> atlas PNG + manifest JSON
  -> collision / layer / scene metadata
  -> runtime loader integration
  -> visible-map proof
```

이렇게 나누면 실패가 보인다.  
raw가 실패했는지, keying이 실패했는지, manifest가 틀렸는지, renderer가 fallback을 탔는지 분리해서 잡을 수 있다.

### 4. 사례 A: AgentForge starter asset pack

AgentForge에서는 Codex image_gen으로 raw pixel art를 만들고, 이를 starter asset pack으로 정리했다.

결과물은 다음과 같다.

- raw PNG
- keyed PNG
- tileset/player/enemy/fx/props atlas
- collision metadata
- scene hook metadata
- manifest JSON
- Canvas loader seed

검증 결과도 같이 남겼다.

- `npm run type-check` PASS
- `npm run build` PASS
- manifest validation PASS
- visible magenta residue 0
- secret scan output 0

여기서 중요한 점은 "에셋을 만들었다"가 아니다.  
raw image를 engine-facing artifact로 바꾸는 골격을 만들었다는 점이다.

### 5. 사례 B: ClaudeCraft tile/item glyph를 sprite로 바꾸기

ClaudeCraft에서는 더 강한 증거가 있다.

기존에는 dungeon tile과 ground item이 glyph로 렌더링되고 있었다. 이걸 sprite-first path로 교체했다. 단, 기존 glyph fallback은 남겼다. 실패하면 화면이 깨지지 않아야 하기 때문이다.

proof JSON은 다음을 기록했다.

- expected tile keys: 7
- expected item keys: 4
- rendered keys: 11
- failures: []
- consoleErrors: []
- glyphFallbacksAllowed: []
- 모든 in-scope assetKey가 `spriteRendered:true`

이건 단순히 manifest를 읽었다는 뜻이 아니다.  
visible map에서 실제로 그려졌다는 뜻이다.

### 6. 사례 C: libGDX/Bone Trail의 review-only asset governance

Bone Trail 쪽에서는 또 다른 축을 만들었다.

여기서는 최종 아트를 주장하지 않았다. 대신 review-only asset pipeline을 만들었다.

- source approval state
- review-only folder
- preview sheet
- voxel turnaround prepass
- cleanup candidate
- runtime preview copy
- not accepted label

이 구분이 중요하다. AI 자동화는 빠르게 산출물을 만들 수 있지만, 빠르다는 이유로 승인 상태까지 건너뛰면 안 된다.  
FDE 관점에서는 이게 오히려 핵심이다. 현장에서는 기술보다 상태 관리가 더 자주 사고를 낸다.

### 7. FDE 관점: 현장 문제를 자동화 가능한 계약으로 바꾸기

이 프로젝트에서 내가 보여주고 싶은 역량은 세 가지다.

첫째, 문제를 다시 정의했다.

"에셋이 없다"가 아니라 "raw generation, postprocess, manifest, runtime proof가 이어지지 않는다"로 쪼갰다.

둘째, 자동화 단위를 설계했다.

사람이 반복하던 배경 제거, slice, atlas, manifest 작성, proof 확인을 pipeline contract로 바꿨다.

셋째, 증거를 남겼다.

build pass만으로 끝내지 않고, 실제 화면에서 assetKey가 그려졌는지 확인했다. 그리고 proof와 acceptance를 분리했다.

이건 게임에만 갇힌 이야기가 아니다. 광고 소재, UI icon set, product visual variant, content QA에도 같은 구조를 쓸 수 있다.  
AI가 많이 만들수록 더 필요한 것은 생성량이 아니라 gate다.

### 8. 마무리: AI 자동화 실력은 실패를 통제하는 구조에서 드러난다

AI 자동화는 "모델이 잘 만들었다"로 끝나면 약하다.

진짜 실력은 모델이 흔들려도 파이프라인이 흔들리지 않게 만드는 데 있다.  
어떤 입력이 들어와도 무엇을 검사하고, 무엇을 거절하고, 무엇을 manifest로 남길지 정해야 한다.

이번 Codex Asset Forge는 그 방향의 작은 사례다.

AI는 그림을 만든다.  
파이프라인은 그 그림을 제품 자산으로 만든다.

## 포트폴리오용 핵심 문장

> Codex image_gen을 raw art 생성 단계로 제한하고, chroma-key, grid slicing, atlas manifest, collision metadata, runtime proof를 연결해 AI-generated pixel art를 검증 가능한 game asset pipeline으로 전환했다.

> FDE 관점에서 현장형 asset bottleneck을 분석하고, 사람이 반복하던 후처리와 검증 작업을 재사용 가능한 자동화 계약으로 설계했다.

## Claim Guard

Safe:

- Codex 기반 raw-to-atlas asset pipeline을 구축했다.
- AgentForge에서 starter asset pack과 loader seed를 만들었다.
- ClaudeCraft에서 tile/item sprite rendering을 visible map proof로 검증했다.
- Bone Trail/libGDX에서 review-only asset governance와 prepass harness를 설계했다.

Careful:

- `game-ready`는 runtime proof가 있는 asset에만 쓴다.
- `open-source`는 repo, license, tests, public push 이후에만 쓴다.
- `portfolio page`는 HTML local reference와 배포 URL 검증 이후에만 쓴다.

Do not claim:

- 최종 아트 품질
- 사용자 시각/재미 acceptance
- 완전 자동 최종 에셋 생산
- 상용 출시 또는 store-ready
- GPL-covered combined distribution의 proprietary ownership
