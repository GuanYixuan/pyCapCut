## A lightweight, flexible, and easy-to-use Python tool for generating and exporting CapCut drafts to build fully automated video editing/remix pipelines!

> 🧪 This project is being migrated from [PyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft). Please ⭐️ to stay tuned!

> 📢 Join the [Discord server](https://discord.gg/WfHgGQvhyW) to discuss usage and new features

## Workflow
![Workflow](https://github.com/GuanYixuan/pyJianYingDraft/raw/main/readme_assets/%E4%BD%BF%E7%94%A8%E6%80%9D%E8%B7%AF.jpg)

# Feature List

> ℹ Please refer to [Github Repository](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md) for full documentation.

### Template Mode
> 🧪 This module has just been migrated. If something doesn’t fit your template, please open an issue.

- ☑️ [Load](#load-template) an (unencrypted) `draft_content.json` file as a template
- ☑️ [Replace media for video/audio segments](#replace-media-by-name)
- ☑️ [Modify text contents of text segments](#replace-text-segment-content)
- ☑️ [Import entire audio/video/text tracks from a template draft into another draft](#import-tracks-from-a-template-draft)
- ☑️ [Extract resource metadata (stickers/bubbles/fancy text, etc.)](#extract-resource-metadata)

### Batch Export
> ⚠️ This module is being migrated. If interested, see the corresponding part in [PyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft?tab=readme-ov-file#%E6%89%B9%E9%87%8F%E5%AF%BC%E5%87%BA%E8%8D%89%E7%A8%BF)

- ☑️ Control CapCut to open a specific draft
- ☑️ Export a draft to a specific location
- ☑️ Adjust export resolution and frame rate

### Video and Image
> 🧪 This module has just been migrated. If animations/effects/transitions don’t take effect, please open an issue.

- ☑️ Add local video/image media, and [customize segment timing, duration, or playback speed](#source-trimming-and-global-speed)
- ☑️ Adjust audio fade in/out durations
- ☑️ [Global video adjustments](#global-video-adjustments) (rotation, scale, brightness, etc.) and [keyframe generation](#keyframes)
- ☑️ [In/Out/Group animations](#add-segment-animations) for video segments
- ☑️ Add [masks](#masks), [segment effects](#add-segment-effects), and [filters](#add-segment-filters)
- ☑️ Video background fill [(example code)](demo.py)

### Stickers
- ☑️ Add stickers based on metadata [extraction](#extract-resource-metadata)
- ☑️ [Keyframe](#keyframes) generation for stickers

### Audio
- ☑️ Add local audio media, and [customize segment timing, duration, or playback speed](#source-trimming-and-global-speed)
- ☑️ Adjust fade in/out durations [(example code)](demo.py), adjust volume [(example code)](demo.py), and its [keyframes](#keyframes)
- ☑️ Add [scene audio effects](#add-segment-effects) to audio segments and configure parameters

### Tracks
- ☑️ [Add tracks](#multi-track-operations) and [append segments to a specific track](#multi-track-operations)
- ☑️ Customize [layer ordering](#multi-track-operations) among video/filter/effect tracks

### Effects, Filters, and Transitions
- ☑️ Clip-attached [effects](#add-segment-effects), [filters](#add-segment-filters), and [animations](#add-segment-animations)
- ☑️ [Standalone tracks for effects and filters](#effect-and-filter-tracks)
- ☑️ Add transitions [(example code)](demo.py) and customize duration

### Text and Subtitles
- ☑️ [Add text, set fonts and styles](#add-text), modify [position and rotation](#global-video-adjustments) of text segments
- ☑️ [Keyframes](#keyframes) and [animations](#add-segment-animations) for text
- ☑️ Text stroke and text background
- ☑️ Text bubble effects and fancy text effects [(example code)](demo.py)
- ☑️ [Automatic line wrapping](#automatic-line-wrapping) with configurable max line width
- ☑️ [Import `.srt` files](#import-subtitles) to create subtitles in bulk and style them

> ℹ The [Github Repository](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md) contains a [demonstration of the above features](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#quick-start).
