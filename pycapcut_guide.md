# pyCapCut 사용 가이드 (macOS)

> 🖥️ **내 환경 기준으로 작성된 가이드**
> - OS: macOS
> - Python: 3.9.13 (Anaconda, `/opt/anaconda3/bin/python3`)
> - CapCut: `/Applications/CapCut.app`
> - CapCut 초안 폴더: `/Users/morg/Movies/CapCut/User Data/Projects/com.lveditor.draft`
> - 기존 초안 목록: `0816`, `0827`, `0828`, `0907`, `0914`, `0915`, `0916`, `0920`

---

## 1. pyCapCut이란?

Python으로 CapCut 초안 파일(`draft_content.json`)을 **프로그래밍으로 자동 생성/수정**하는 도구.

동영상 편집을 코드로 자동화할 수 있다. 예를 들어:
- 여러 영상의 자막을 일괄 생성
- 템플릿 초안에서 소재만 교체하여 대량 생산
- 키프레임, 애니메이션, 특수효과 자동 설정

---

## 2. 설치

### pip 설치 (권장)
```bash
pip install pycapcut
```

### 또는 클론한 소스에서 직접 설치
```bash
cd /Users/morg/Desktop/Pycapcut
pip install -e .
```

### 의존성
| 패키지 | 용도 |
|--------|------|
| `pymediainfo` | 영상/오디오 파일 정보 읽기 |
| `imageio` | 이미지 처리 |
| `uiautomation` | 자동 내보내기 (Windows 전용, Mac에선 불필요) |

> [!IMPORTANT]
> `pymediainfo`는 시스템에 **MediaInfo 라이브러리**가 필요하다. Mac에서는:
> ```bash
> brew install mediainfo
> ```

---

## 3. 핵심 개념

### 작동 원리
```
Python 코드 → draft_content.json 생성 → CapCut이 읽어서 열기
```
CapCut의 내부 프로젝트 파일 구조를 직접 조작하는 방식이다. 공식 API가 아닌 **리버스 엔지니어링** 기반.

### 주요 클래스
| 클래스 | 역할 |
|--------|------|
| `DraftFolder` | CapCut 초안 폴더를 관리 |
| `ScriptFile` | 하나의 초안(프로젝트)을 표현 |
| `VideoSegment` | 비디오 클립 하나 |
| `AudioSegment` | 오디오 클립 하나 |
| `TextSegment` | 텍스트/자막 클립 하나 |
| `VideoMaterial` / `AudioMaterial` | 소재 파일 |

### 시간 표현
CapCut 내부는 **마이크로초(μs)** 단위를 사용하지만, 문자열로 편하게 입력 가능:

```python
from pycapcut import tim, trange, SEC

tim("1s")       # → 1,000,000 (1초 = 100만 μs)
tim("1.5s")     # → 1,500,000
tim("1m30s")    # → 90,000,000
trange("0s", "5s")  # 0초 시작, 5초 동안 (주의: 두 번째는 "지속시간")
```

> [!WARNING]
> `trange`의 두 번째 인자는 **종료 시간이 아니라 지속 시간**이다!

---

## 4. 빠른 시작 (데모 실행)

### 4-1. demo.py 수정

[demo.py](file:///Users/morg/Desktop/Pycapcut/demo.py)의 7번째 줄을 내 초안 폴더 경로로 변경:

```python
# 변경 전
draft_folder = cc.DraftFolder(r"<你的草稿文件夹>")

# 변경 후 (내 Mac 기준)
draft_folder = cc.DraftFolder("/Users/morg/Movies/CapCut/User Data/Projects/com.lveditor.draft")
```

### 4-2. 실행

```bash
cd /Users/morg/Desktop/Pycapcut
python demo.py
```

### 4-3. CapCut에서 확인

1. CapCut 앱을 열거나 재시작
2. 프로젝트 목록에서 **`demo`** 초안을 찾아서 열기
3. 타임라인에 오디오, 비디오, 텍스트가 배치된 것을 확인

---

## 5. 기본 사용법

### 5-1. 새 초안 만들기

```python
import pycapcut as cc

# 초안 폴더 설정 (내 Mac 경로)
draft_folder = cc.DraftFolder(
    "/Users/morg/Movies/CapCut/User Data/Projects/com.lveditor.draft"
)

# 1920x1080 해상도의 새 초안 생성
script = draft_folder.create_draft("내_프로젝트", 1920, 1080)

# 트랙 추가
script.add_track(cc.TrackType.video)
script.add_track(cc.TrackType.audio)
script.add_track(cc.TrackType.text)
```

### 5-2. 비디오 추가

```python
from pycapcut import trange

# 비디오 클립 생성 (소재 경로, 타임라인 배치)
video_seg = cc.VideoSegment(
    "/Users/morg/Desktop/my_video.mp4",  # 소재 파일 경로
    trange("0s", "10s")                  # 0초부터 10초 동안
)

script.add_segment(video_seg)
```

### 5-3. 오디오 추가

```python
audio_seg = cc.AudioSegment(
    "/Users/morg/Desktop/bgm.mp3",
    trange("0s", "10s"),
    volume=0.8       # 볼륨 80%
)
audio_seg.add_fade("2s", "1s")  # 페이드인 2초, 페이드아웃 1초

script.add_segment(audio_seg)
```

### 5-4. 텍스트/자막 추가

```python
text_seg = cc.TextSegment(
    "안녕하세요!",
    trange("0s", "5s"),
    style=cc.TextStyle(
        size=8.0,
        color=(1.0, 1.0, 1.0)  # 흰색
    ),
    clip_settings=cc.ClipSettings(
        transform_y=-0.8  # 화면 하단에 배치
    )
)

script.add_segment(text_seg)
```

### 5-5. 저장

```python
script.save()
```
저장 후 CapCut을 재시작하면 프로젝트 목록에 나타난다.

---

## 6. 고급 기능

### 6-1. 키프레임

시간에 따라 속성 값을 변화시킨다 (이동, 투명도, 크기 등):

```python
from pycapcut import KeyframeProperty, SEC

# 투명도로 페이드아웃 효과 만들기
video_seg.add_keyframe(KeyframeProperty.alpha, video_seg.duration - SEC, 1.0)  # 끝나기 1초 전: 불투명
video_seg.add_keyframe(KeyframeProperty.alpha, video_seg.duration, 0.0)        # 끝날 때: 완전 투명

# 위치 이동 애니메이션
video_seg.add_keyframe(KeyframeProperty.position_x, 0, -2)       # 시작: 화면 왼쪽 바깥
video_seg.add_keyframe(KeyframeProperty.position_x, "0.5s", 0)   # 0.5초 후: 화면 중앙
```

### 6-2. 애니메이션

```python
# 비디오 입장/퇴장 애니메이션
video_seg.add_animation(cc.IntroType.噪点拽入)  # 입장 애니메이션

# 텍스트 애니메이션
text_seg.add_animation(cc.TextIntro.复古打字机)   # 입장: 타자기 효과
text_seg.add_animation(cc.TextOutro.故障闪动)     # 퇴장: 글리치 효과
```

### 6-3. 멀티 트랙

```python
# 여러 비디오 트랙 만들기
script.add_track(cc.TrackType.video, track_name="전경", relative_index=2)
script.add_track(cc.TrackType.video, track_name="배경", relative_index=1)

# 특정 트랙에 클립 추가
script.add_segment(foreground_clip, "전경")
script.add_segment(background_clip, "배경")
```

### 6-4. SRT 자막 가져오기

```python
script.import_srt(
    "/Users/morg/Desktop/subtitle.srt",
    track_name="자막",
    time_offset="0s",
    text_style=cc.TextStyle(size=6.0, color=(1.0, 1.0, 1.0))
)
```

### 6-5. 템플릿 모드 (기존 초안 복제 후 소재 교체)

```python
# 기존 초안 "0920"을 템플릿으로 복제
script = draft_folder.duplicate_as_template("0920", "자동_생성_1")

# 소재 교체
new_video = cc.VideoMaterial("/Users/morg/Desktop/new_video.mp4")
script.replace_material_by_name("원래소재.mp4", new_video)

# 텍스트 교체
text_track = script.get_imported_track(cc.TrackType.text, index=0)
script.replace_text(text_track, 0, "새로운 텍스트")

script.save()
```

---

## 7. 소재 변속 & 구간 자르기

```python
from pycapcut import trange

# 기본: 소재 앞 4초를 그대로 사용
seg1 = cc.VideoSegment("/path/to/video.mp4", trange("0s", "4s"))

# 1.25배속: 소재 앞 5초를 4초에 재생
seg2 = cc.VideoSegment("/path/to/video.mp4", trange("0s", "4s"), speed=1.25)

# 특정 구간 지정: 소재 0~4초를 1초에 압축 재생 (자동 4배속)
seg3 = cc.VideoSegment("/path/to/video.mp4",
                       trange("4s", "1s"),
                       source_timerange=trange(0, "4s"))
```

---

## 8. 마스크

```python
from pycapcut import MaskType

# 원형 마스크 (지름이 소재의 50%)
video_seg.add_mask(MaskType.圆形, size=0.5)

# 선형 마스크 (45도 회전)
video_seg.add_mask(MaskType.线性, center_x=100, rotation=45)
```

---

## 9. 특수효과 & 필터

```python
from pycapcut import VideoSceneEffectType, FilterType

# 클립에 특수효과 추가
video_seg.add_effect(VideoSceneEffectType.全息扫描, [None, None, 100.0])

# 클립에 필터 추가
video_seg.add_filter(FilterType.冰城, 50)  # 강도 50
```

---

## 10. 주의사항

> [!CAUTION]
> **Mac 한정 제약사항**
> - pyCapCut으로 초안을 **생성/수정**하는 것은 Mac에서 가능
> - 하지만 **일괄 내보내기(Batch Export)** 기능은 Windows 전용 (`uiautomation` 사용)
> - Mac에서는 CapCut 앱을 열고 **수동으로 내보내기** 해야 함

> [!NOTE]
> **기타 참고사항**
> - 이 도구는 비공식이므로, CapCut 업데이트 시 호환성이 깨질 수 있음
> - 특수효과/애니메이션 이름은 중국어 원본 그대로 사용 (예: `噪点拽入`, `全息扫描`)
> - `from_name` 메서드로 이름 검색 가능: `VideoSceneEffectType.from_name("全息扫描")`

---

## 11. 프로젝트 구조

```
/Users/morg/Desktop/Pycapcut/
├── demo.py              ← 예제 스크립트
├── setup.py             ← 패키지 설정
├── requirements.txt     ← 의존성 목록
├── README.md            ← 원본 문서 (중국어)
├── english_readme.md    ← 원본 문서 (영어)
├── readme_assets/       ← 문서용 이미지/튜토리얼 소재
└── pycapcut/            ← 핵심 패키지
    ├── __init__.py
    ├── draft_folder.py      # 초안 폴더 관리
    ├── script_file.py       # 초안 파일 (핵심)
    ├── video_segment.py     # 비디오 클립
    ├── audio_segment.py     # 오디오 클립
    ├── text_segment.py      # 텍스트 클립
    ├── local_materials.py   # 로컬 소재
    ├── keyframe.py          # 키프레임
    ├── animation.py         # 애니메이션
    ├── track.py             # 트랙
    ├── template_mode.py     # 템플릿 모드
    ├── time_util.py         # 시간 유틸
    └── assets/              # 내장 JSON 데이터
```

---

## 12. 유용한 링크

- 📦 GitHub: [GuanYixuan/pyCapCut](https://github.com/GuanYixuan/pyCapCut)
- 💬 Discord: [참여하기](https://discord.gg/WfHgGQvhyW)
- 🔗 관련 프로젝트: [pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) (중국판 CapCut = 剪映 용)
