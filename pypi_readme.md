<!-- Generated from english_readme.md by tools/generate_pypi_readme.py. Do not edit directly. -->

# pyCapCut

### A lightweight, flexible Python tool for generating and editing CapCut drafts

[中文版本](https://github.com/GuanYixuan/pyCapCut/blob/main/README.md)

> This project shares its origins with [PyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) and targets CapCut drafts.

> ⚠️ **0.1.0 preview**: The next version will align track ordering and references with pyJianYingDraft, introduce `append_track(s)` / `insert_track(s)` and `TrackSpec` / `TrackRef`, and remove `add_track`. Scripts that depend on the old API or track layering behavior will need updating; a migration guide will accompany the release. To keep the current behavior, pin `pip install pycapcut==0.0.4` and refer to that version's [documentation](https://github.com/GuanYixuan/pyCapCut/blob/0.0.4/english_readme.md) and [example](https://github.com/GuanYixuan/pyCapCut/blob/0.0.4/demo.py).

> 📢 Join the [Discord server](https://discord.gg/WfHgGQvhyW) to discuss usage and new features

## Workflow

![Workflow](https://github.com/GuanYixuan/pyCapCut/raw/main/readme_assets/%E4%BD%BF%E7%94%A8%E6%80%9D%E8%B7%AF.jpg)

Open the generated draft in CapCut and export the video manually. Automated export is currently unsupported.

# Feature List

✅ Supported. The validation version column lists confirmed CapCut versions; “—” means no version is recorded. It does not specify a minimum version or guarantee compatibility with every version.

### Video and Image

| Feature | Support | Validation version |
|---|---|---|
| Local video/image media and [timing](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#source-trimming-and-global-speed) | ✅ | 8.2.0 |
| [Global video adjustments](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#global-video-adjustments) | ✅ | 8.2.0 |
| [Video keyframes](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#keyframes) | ✅ | — |
| [Video masks](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#masks) | ✅ | 9.5.0.4050 |
| [Video chroma keying](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-chroma-keying) | ✅ | 9.5.0.4050 |
| [Video blend modes](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#set-segment-blend-mode) | ✅ | 9.5.0.4050 |
| Video background fill [(example)](https://github.com/GuanYixuan/pyCapCut/blob/main/demo.py) | ✅ | — |
| [Audio fades](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#audio-fades) for videos with audio | ✅ | — |
| [Pitch change during speed adjustment](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#pitch-change-during-speed-adjustment) for videos with audio | ✅ | 9.5.0.4050 |

### Stickers

| Feature | Support | Validation version |
|---|---|---|
| Add stickers using [resource metadata](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#extract-resource-metadata) | ✅ | — |
| [Sticker keyframes](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#keyframes) | ✅ | — |

### Audio

| Feature | Support | Validation version |
|---|---|---|
| Local audio media and [timing](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#source-trimming-and-global-speed) | ✅ | 9.5.0.4050 |
| [Audio fades](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#audio-fades), volume and [keyframes](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#keyframes) | ✅ | — |
| [Pitch change during speed adjustment](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#pitch-change-during-speed-adjustment) | ✅ | 9.5.0.4050 |
| [Scene audio effects](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-effects) | ✅ | — |
| [Tone effects](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-effects) | ✅ | 9.5.0.4050 (花栗鼠) |

### Tracks

| Feature | Support | Validation version |
|---|---|---|
| [Add tracks and segments](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#multi-track-operations) | ✅ | 8.2.0 |
| [Track layer ordering](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#multi-track-operations) | ✅ | 8.2.0 (video tracks) |
| [Main track magnet](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#main-track-magnet) | ✅ | 8.2.0 |

### Effects, Filters, and Transitions

| Feature | Support | Validation version |
|---|---|---|
| [Video segment animations](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-animations) | ✅ | — |
| [Video segment effects](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-effects) | ✅ | — |
| [Video segment filters](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-filters) | ✅ | — |
| [Standalone effect and filter tracks](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#effect-and-filter-tracks) | ✅ | — |
| Transitions [(example)](https://github.com/GuanYixuan/pyCapCut/blob/main/demo.py) | ✅ | — |

### Text and Subtitles

| Feature | Support | Validation version |
|---|---|---|
| [Text and styles](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-text) | ✅ | 8.2.0 |
| [Fonts](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-text) | ✅ | 9.5.0.4050 |
| [Text keyframes](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#keyframes) | ✅ | — |
| [Text animations](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-segment-animations) | ✅ | — |
| Text stroke, background and shadow | ✅ | — |
| Text bubbles and fancy text [(example)](https://github.com/GuanYixuan/pyCapCut/blob/main/demo.py) | ✅ | 9.5.0.4050 (fancy text) |
| [Automatic line wrapping](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#automatic-line-wrapping) | ✅ | — |
| [Import SRT subtitles](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#import-subtitles) | ✅ | — |

### Template Mode

| Feature | Support | Validation version |
|---|---|---|
| [Load plaintext drafts](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#load-template) | ✅ | 8.2.0 |
| [Replace media by name](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#replace-media-by-name) | ✅ | — |
| [Replace media by segment](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#replace-media-by-segment) | ✅ | — |
| [Replace text content](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#replace-text-segment-content) | ✅ | — |
| [Import template tracks](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#import-tracks-from-a-template-draft) | ✅ | — |
| [Extract resource metadata](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#extract-resource-metadata) | ✅ | — |

# Installation

pyCapCut now supports pip installation (excluding demo).

```bash
pip install pycapcut
```

### Cross-platform Compatibility

Install the library on Windows, Linux or macOS to generate and edit drafts. **Open the generated drafts in CapCut for Windows and export videos manually.**

For complete usage examples, see the [full documentation](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#quick-start).
