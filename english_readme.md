<!-- PYPI:BEGIN -->
# pyCapCut

### A lightweight, flexible Python tool for generating and editing CapCut drafts

[中文版本](README.md) | [한국어 버전](korean_readme.md)

> This project shares its origins with [PyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) and targets CapCut drafts.

> ⚠️ **0.1.0 preview**: The next version will align track ordering and references with pyJianYingDraft, introduce `append_track(s)` / `insert_track(s)` and `TrackSpec` / `TrackRef`, and remove `add_track`. Scripts that depend on the old API or track layering behavior will need updating; a migration guide will accompany the release. To keep the current behavior, pin `pip install pycapcut==0.0.4` and refer to that version's [documentation](https://github.com/GuanYixuan/pyCapCut/blob/0.0.4/english_readme.md) and [example](https://github.com/GuanYixuan/pyCapCut/blob/0.0.4/demo.py).

> 📢 Join the [Discord server](https://discord.gg/WfHgGQvhyW) to discuss usage and new features

## Workflow

![Workflow](readme_assets/使用思路.jpg)

Open the generated draft in CapCut and export the video manually. Automated export is currently unsupported.

# Feature List

✅ Supported. The validation version column lists confirmed CapCut versions; “—” means no version is recorded. It does not specify a minimum version or guarantee compatibility with every version.

### Video and Image

| Feature | Support | Validation version |
|---|---|---|
| Local video/image media and [timing](#source-trimming-and-global-speed) | ✅ | 8.2.0 |
| [Global video adjustments](#global-video-adjustments) | ✅ | 8.2.0 |
| [Video keyframes](#keyframes) | ✅ | — |
| [Video masks](#masks) | ✅ | 9.5.0.4050 |
| [Video chroma keying](#add-chroma-keying) | ✅ | 9.5.0.4050 |
| [Video blend modes](#set-segment-blend-mode) | ✅ | 9.5.0.4050 |
| Video background fill [(example)](demo.py) | ✅ | — |
| [Audio fades](#audio-fades) for videos with audio | ✅ | — |
| [Pitch change during speed adjustment](#pitch-change-during-speed-adjustment) for videos with audio | ✅ | 9.5.0.4050 |

### Stickers

| Feature | Support | Validation version |
|---|---|---|
| Add stickers using [resource metadata](#extract-resource-metadata) | ✅ | — |
| [Sticker keyframes](#keyframes) | ✅ | — |

### Audio

| Feature | Support | Validation version |
|---|---|---|
| Local audio media and [timing](#source-trimming-and-global-speed) | ✅ | 9.5.0.4050 |
| [Audio fades](#audio-fades), volume and [keyframes](#keyframes) | ✅ | — |
| [Pitch change during speed adjustment](#pitch-change-during-speed-adjustment) | ✅ | 9.5.0.4050 |
| [Scene audio effects](#add-segment-effects) | ✅ | — |
| [Tone effects](#add-segment-effects) | ✅ | 9.5.0.4050 (花栗鼠) |

### Tracks

| Feature | Support | Validation version |
|---|---|---|
| [Add tracks and segments](#multi-track-operations) | ✅ | 8.2.0 |
| [Track layer ordering](#multi-track-operations) | ✅ | 8.2.0 (video tracks) |
| [Main track magnet](#main-track-magnet) | ✅ | 8.2.0 |

### Effects, Filters, and Transitions

| Feature | Support | Validation version |
|---|---|---|
| [Video segment animations](#add-segment-animations) | ✅ | — |
| [Video segment effects](#add-segment-effects) | ✅ | — |
| [Video segment filters](#add-segment-filters) | ✅ | — |
| [Standalone effect and filter tracks](#effect-and-filter-tracks) | ✅ | — |
| Transitions [(example)](demo.py) | ✅ | — |

### Text and Subtitles

| Feature | Support | Validation version |
|---|---|---|
| [Text and styles](#add-text) | ✅ | 8.2.0 |
| [Fonts](#add-text) | ✅ | 9.5.0.4050 |
| [Text keyframes](#keyframes) | ✅ | — |
| [Text animations](#add-segment-animations) | ✅ | — |
| Text stroke, background and shadow | ✅ | — |
| Text bubbles and fancy text [(example)](demo.py) | ✅ | 9.5.0.4050 (fancy text) |
| [Automatic line wrapping](#automatic-line-wrapping) | ✅ | — |
| [Import SRT subtitles](#import-subtitles) | ✅ | — |

### Template Mode

| Feature | Support | Validation version |
|---|---|---|
| [Load plaintext drafts](#load-template) | ✅ | 8.2.0 |
| [Replace media by name](#replace-media-by-name) | ✅ | — |
| [Replace media by segment](#replace-media-by-segment) | ✅ | — |
| [Replace text content](#replace-text-segment-content) | ✅ | — |
| [Import template tracks](#import-tracks-from-a-template-draft) | ✅ | — |
| [Extract resource metadata](#extract-resource-metadata) | ✅ | — |

# Installation

pyCapCut now supports pip installation (excluding demo).

```bash
pip install pycapcut
```

### Cross-platform Compatibility

Install the library on Windows, Linux or macOS to generate and edit drafts. **Open the generated drafts in CapCut for Windows and export videos manually.**

For complete usage examples, see the [full documentation](english_readme.md#quick-start).
<!-- PYPI:END -->

# Quick Start

The `demo.py` example creates a CapCut draft with audio/video media and a line of text, and adds audio fade-in, a video intro animation, a transition, keyframes, and text bubble/fancy text effects.

How to run the example:

1. Find your CapCut Drafts folder path (like `.../CapCut Drafts`) and replace `<your CapCut Drafts folder>` in the code
2. Run `demo.py` (the example overwrites an existing draft named `demo`; make sure it is safe to replace)
3. In CapCut, find and open the newly created `demo` draft (you may need to enter and exit an existing draft, or restart CapCut to refresh the list). You should see a timeline similar to the image below:

![Quick Start](readme_assets/快速上手.png)

Adjust the media, timing and effects in the example to create your own draft. Export the finished video manually in CapCut.

# Usage Guide

> ℹ It’s recommended to jump to interesting features from the [Feature List](#feature-list) instead of reading sequentially.

### Template Mode

Templates must contain a readable, plaintext `draft_content.json`. Encrypted or otherwise unreadable formats are not supported.

To retain certain complex features (text effects, compound clips, etc.), you can load an existing CapCut draft as a template, then import parts of it into another draft, or directly replace part of its segments.

Currently three replacement methods are provided:

- [Replace media by name](#replace-media-by-name): replace the media itself, affecting all segments that reference it
- [Replace media by segment](#replace-media-by-segment): replace the media of a specific segment and reselect the source range it references
- [Replace the content of text segments](#replace-text-segment-content): keep all text formatting while replacing its content

Additionally, for items without a clear name (stickers, fancy text, etc.), [extract resource metadata](#extract-resource-metadata) to obtain their `resource_id`.

> ℹ If you encounter missing template content, please report it.

#### Load Template

It is recommended to use `DraftFolder` to manage CapCut’s drafts folder (found in CapCut “Global Settings” → “Drafts Location”), which makes it convenient to generate a new draft from a template.

```python
import pycapcut as cc

draft_folder = cc.DraftFolder("<CapCut Drafts folder>")  # Usually like ".../CapCut Drafts"
script = draft_folder.duplicate_as_template("Template Draft", "New Draft")  # Copy "Template Draft" to a new draft named "New Draft" and return an editable ScriptFile object

# Edit the returned ScriptFile object, e.g., replace media, add tracks and segments
script.save()  # Save your "New Draft"
```

To maximize compatibility with complex features in templates, the imported tracks are kept separate from the tracks created by pycapcut:

- Other than the replacement features below, you cannot add segments, transitions, fades, effects, etc. on imported tracks
- You can still create new tracks and add segments as in non-template mode

#### Extract Resource Metadata

For an imported `ScriptFile`, call `inspect_material` to extract `resource_id` for certain materials. `DraftFolder` also offers methods to inspect resource metadata of a specified draft.

```python
import pycapcut as cc

draft_folder = cc.DraftFolder("<CapCut Drafts folder>")
draft_folder.inspect_material("Draft Name")

# Or
script = draft_folder.load_template("Draft Name")
script.inspect_material()
```

The output might look like:

```
贴纸素材:
        Resource id: 7405878923323641129 '秋日手绘-枫叶'
        Resource id: 7429353555447893260 '电商购物促销/哇哦'
        Resource id: 7437707455267671315 '冬日涂鸦winter雪花冬天vlog装饰文字'
        Resource id: 7343931192204463401 '爱心'
文字气泡效果:
        Effect id: 763870 ,Resource id: 6838834573413978631 '标题59'
花字效果:
        Resource id: 7342020000812731658 '彩色手绘线条花字'
```

The metadata above can be used to add corresponding materials (e.g., via the `resource_id` parameter of `StickerSegment`).

#### Replace Media by Name

This approach replaces the media itself without directly modifying segments.

> ℹ Since materials have names (by default, the local file name), this replacement is easy to locate

> ℹ Because it doesn’t involve source range changes, this method is especially suitable for image media and rarely causes compatibility issues

Using the draft from [Quick Start](#quick-start) as an example, if we want to replace the audio media with a new one:
```python
new_material = cc.AudioMaterial("<path to new audio file>")
script.replace_material_by_name("audio.mp3", new_material)  # Replace the material named "audio.mp3"
```

After replacement, the segment still trims the first 5 seconds of the media, and properties like volume, fade in/out, playback speed remain unchanged.

#### Replace Media by Segment

This approach replaces a specific segment’s media, allowing you to reselect the source range and stretch/shrink the segment on the timeline accordingly.

> ℹ Since segments have no names, you usually need to locate them by index

This involves two steps: select a track and then replace the media. Using the audio example above:
```python
from pycapcut import trange_seconds, ShrinkMode, ExtendMode

audio_track = script.get_imported_track(
    cc.TrackType.audio,                # Select the imported audio track
    #name="audio",                         # If the track has a name, prefer using it
    index=0                                # Or locate by index; 0 means the bottom-most track of the same type
)

script.replace_material_by_seg(
    audio_track, 0, new_material,          # Select the 0-th segment in audio_track (i.e., the first segment)
    #source_timerange=None,                # If not specified, default to use the entire material
    source_timerange=trange_seconds(0, duration=10),  # Here we select the first 10 seconds of the material (note original segment length is 5s)
    handle_shrink=ShrinkMode.cut_tail,     # If the segment shortens, move its end earlier
    handle_extend=ExtendMode.push_tail     # If the segment extends, move its end later; push following segments if needed
)
```

As seen above, this may change the segment duration, so use `handle_shrink` and `handle_extend` to specify behavior when shortening or extending.

> ℹ Default behavior when not specifying `handle_shrink`/`handle_extend`:
> - If the new media is shorter than the original, move the segment end earlier to match the new length
> - If the new media is longer than the original, crop the source range to keep the segment duration unchanged

See enum classes `ShrinkMode` and `ExtendMode` for the full list of behaviors.

> ℹ It’s known that replacing segments with combined in/out animations does not automatically refresh animation timing

#### Replace Text Segment Content

This replaces the content of a specific text segment while keeping all formatting.

This also involves two steps: select a track and then replace the content. The “select track” step is similar to [Replace Media by Segment](#replace-media-by-segment).

Assuming we already selected a text track `text_track`:
```python
script.replace_text(
    text_track, 0,  # Select the 0-th segment in text_track (i.e., the first segment)
    "New text content"     # New text content
)
```

#### Import Tracks from a Template Draft

This literally copies the specified tracks in the template draft into the new draft. Suitable for stitching multiple templates together.

> ℹ Currently only audio/video/text tracks are supported.

> ⚠️ This method preserves IDs of segments and their materials, therefore you cannot import the same track into the same draft multiple times.

Example:
```python
source_script = draft_folder.load_template("<Template Draft Name>")     # Load the template draft
target_script = draft_folder.create_draft("New Draft", 1920, 1080)  # Create a new draft

# Select a text track from the template
text_track = source_script.get_imported_track(
    cc.TrackType.text,                # Select imported text track
    #name="text",                        # If the track has a name, prefer using it
    index=0                              # Or locate by index; 0 means the bottom-most track of the same type
)

# Import the text track into the new draft
target_script.import_track(
    source_script, text_track,
    offset=target_script.duration,  # Place the imported track at the end of the new draft
    new_name="imported_text",       # Optional new track name
    relative_index=1,               # Relative order among all text tracks; larger values are closer to the foreground; can be negative
)
```

### Time and Tracks

#### Time Format

CapCut (and this project) internally stores time in microseconds, which is not convenient to input. We provide a “string form” for time. Most time parameters support both:

- Microseconds: `int`, suitable for calculation
- String: `str`, like `"1.5s"`, `"1h3m12s"`, convenient for input

If you want to explicitly convert from string to microseconds, use `tim`. `trange` is a convenience constructor for `Timerange` that accepts string inputs.

For most uses, prefer `trange_seconds(start, end=...)` or `trange_seconds(start, duration=...)`. All arguments are in seconds; supply exactly one of `end` and `duration`. Start and end are rounded separately to microseconds, then used to calculate the duration. `trange` continues to accept microseconds or time strings.

Rounding can make the same duration differ by one microsecond at different start times. For adjacent segments, use `end` to specify their shared absolute boundary.

> ⚠️ The second parameter of `trange` is the duration, not the end time

For example:
```python
import pycapcut as cc
from pycapcut import SEC, tim, trange

# 1 second
assert 1000000 == SEC == tim("1s") == tim("0.01666667m")

# 0~1 minute
assert cc.Timerange(0, 60*SEC) == trange("0s", "1m") == trange("0s", "0.5m30s")

# 2 seconds after a segment starts
seg = cc.TextSegment("Example", cc.trange_seconds(0, duration=4))
assert seg.target_timerange.start + 2*SEC == seg.target_timerange.start + tim("2s")

# Specify the shared absolute boundary for adjacent segments
first = cc.trange_seconds(0, end=1.25)
second = cc.trange_seconds(1.25, end=2.5)
assert first.end == second.start
```

#### Source Trimming and Global Speed

Trimming and speed are configured when creating a `Segment`, via `target_timerange`, `source_timerange`, and `speed`.
> ℹ Curve speed change is not yet supported

Using `VideoSegment` as example (same for `AudioSegment`). Two construction styles are supported:

1. Convenience constructor: pass a media path string directly to auto-create a material instance
2. Traditional constructor: create the material instance first, then pass it to the segment constructor. Use this when you need to set crop properties on the media.

```python
import os
import pycapcut as cc
from pycapcut import trange, trange_seconds, SEC

# Assume we already have a draft object `script` (see “Quick Start”), and create three tracks
for i in range(3, 0, -1): # reverse order
    script.add_track(cc.TrackType.video, "%d" % i)

# The following demonstrates creation of materials and segments
# Method 1: convenience constructor (recommended)
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
video_path = os.path.join(tutorial_asset_dir, 'video.mp4')

# Pass the media path directly
seg1 = cc.VideoSegment(video_path, trange_seconds(0, duration=4))  # Trim the first 4 seconds of the material

# Method 2: traditional constructor
mat = cc.VideoMaterial(video_path)  # Create the material instance first
seg2 = cc.VideoSegment(mat, trange_seconds(0, duration=4))  # Then pass it to the constructor

# The video material length is 5s
print("Video material length: %f s" % (mat.duration / SEC))

# The following demonstrates source trimming and speed
# If source_timerange is not specified, the first segment of equal length is used automatically
seg11 = cc.VideoSegment(video_path, trange_seconds(0, duration=4))              # Automatically trim first 4 seconds (4 seconds is the duration)
seg2  = cc.VideoSegment(video_path, trange_seconds(0, duration=4), speed=1.25)  # Automatically trim the first 4*1.25=5 seconds
# seg4 = cc.VideoSegment(video_path, trange_seconds(0, duration=3), speed=3.0)   # Trim the first 3*3.0=9 seconds; will error if material is too short
# If source_timerange is specified, trim the specified range and auto-set speed
seg12 = cc.VideoSegment(video_path, trange_seconds(4, duration=1),
                            source_timerange=trange_seconds(0, duration=4))     # Play 4s of material within 1s; speed auto-set to 4.0

# If both source_timerange and speed are specified, trim the specified range and override target duration by speed
seg3  = cc.VideoSegment(video_path, trange("1s", "66666h"),
                            source_timerange=trange_seconds(0, duration=5),
                            speed=2.0) # Play 5s of material at 2x speed; target duration becomes 2.5s

# Add segments to tracks
script.add_segment(seg11, "1").add_segment(seg12, "1")
script.add_segment(seg2, "2")
script.add_segment(seg3, "3")
```

#### Pitch Change During Speed Adjustment

Set `change_pitch=True` on `AudioSegment` or a `VideoSegment` with audio to change pitch along with playback speed. The default is `False`, preserving the original pitch during speed adjustment. A video without audio has no audible change.

```python
audio_path = os.path.join(tutorial_asset_dir, 'audio.mp3')

audio_segment = cc.AudioSegment(audio_path, trange_seconds(0, duration=2),
                                speed=2.0, change_pitch=True)
```

#### Main Track Magnet

Set `maintrack_adsorb` when creating a draft to control the main track magnet. It is enabled by default.

```python
script = draft_folder.create_draft("New Draft", 1920, 1080, maintrack_adsorb=False)
script.save()
```

#### Multi-Track Operations

`ScriptFile.add_track` supports creating multiple tracks of the same type and customizing their order:
```python
script.add_track(cc.TrackType.video,
                 track_name="Foreground",       # Track name
                 relative_index=2)              # Relative position among all video tracks
script.add_track(cc.TrackType.video,
                 track_name="Background",
                 relative_index=1)              # Since 1 < 2, the background track is below the foreground
```

> ℹ For tracks with the same index, tracks created later are placed on top by default

Once multiple tracks of the same type exist, you must specify the target track when adding segments, e.g.:
```python
script.add_segment(video_segment, "Background")
```

### Global Video Adjustments

Set rotation, flip, scale, opacity and position through the `clip_settings` parameter of `VideoSegment`. Set media cropping through the `crop_settings` parameter of `VideoMaterial`.
> ℹ Keyframes have higher priority than global adjustments, so keyframes override corresponding global settings

Example: create a video segment and set its opacity to 0.5 and enable horizontal flip:
```python
from pycapcut import ClipSettings
video_segment = cc.VideoSegment(video_material,
                                   cc.Timerange(0, video_material.duration),      # Same length as the material
                                   clip_settings=ClipSettings(alpha=0.5,             # Opacity 0.5
                                                              flip_horizontal=True)  # Enable horizontal flip
                                    )
```

See the `ClipSettings` constructor for detailed parameters.

### Keyframes

A keyframe is a pair of (time within the segment, value) attached to a segment. To create keyframes, call `add_keyframe` with the time relative to the segment start, the value, and the property to control.
> ℹ Currently keyframes for effect or filter parameters are not supported

The following example simulates a fade-out using two opacity keyframes:
```python
import os
import pycapcut as cc
from pycapcut import KeyframeProperty, SEC

# Assume we already have a draft object `script` (see “Quick Start”), and create a video track
script.add_track(cc.TrackType.video)
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')

# Create a video segment
video_material = cc.VideoMaterial(os.path.join(tutorial_asset_dir, 'video.mp4'))
video_segment = cc.VideoSegment(video_material,
                                   cc.Timerange(0, video_material.duration)) # Same length as the material

# Add two opacity keyframes to make a 1s fade-out
video_segment.add_keyframe(KeyframeProperty.alpha, video_segment.duration - SEC, 1.0) # Fully opaque 1s before end
video_segment.add_keyframe(KeyframeProperty.alpha, video_segment.duration, 0.0) # Fully transparent at end

# Add the segment to the track
script.add_segment(video_segment)
```

Besides `alpha`, `KeyframeProperty` includes translation, rotation, scale, volume, saturation, etc., all of which support keyframes. Text and sticker segments also support keyframes for position-/size-related properties only.

For audio segments, currently only volume keyframes are supported, and you do not need to specify `KeyframeProperty`:
```python
audio_segment: cc.AudioSegment
audio_segment.add_keyframe("0s", 0.6) # Volume is 60% at the start of the segment
```

### Audio Fades

Call `add_fade(in_duration, out_duration)` on an audio segment or a video segment with audio to set its audio fade-in and fade-out durations. Use time strings or microseconds. Each segment can have one fade configuration.

```python
audio_segment.add_fade("1s", "0.5s")
video_segment.add_fade("0.5s", "1s")
```

Set volume through the segment constructor’s `volume` parameter; `1.0` keeps the original volume. Use [keyframes](#keyframes) to change volume over time.

### Masks

Adding masks is simple: call `VideoSegment.add_mask`:
```python
from pycapcut import MaskType

# Add a linear mask centered at (100, 0) pixels on the material, rotated 45 degrees clockwise
video_segment1.add_mask(MaskType.线性, center_x=100, rotation=45)
# Add a circular mask with diameter 50% of the material
video_segment2.add_mask(MaskType.圆形, size=0.5)
```
Where:

- `MaskType` stores CapCut’s built-in mask types
- `center_x` and `center_y` are the mask center coordinates, same meaning as in CapCut
- `rotation`, `feather`, and `round_corner` correspond to rotation, feathering, and round-corner parameters, same as in CapCut
- `size` is the “primary size” (visible surface height/ circle diameter/ heart height, etc.) as a proportion of the material

See the `add_mask` docstring for more details.

### Effects, Animations, and Filters

#### Effect Types

Currently supported effect enums:

- Audio: `AudioSceneEffectType` (scene audio), `ToneEffectType` (tone)
- Video: `VideoSceneEffectType` (visual effects), `VideoCharacterEffectType` (character effects)

Currently supported animation enums:

- Video: `IntroType` (intro), `OutroType` (outro), `GroupAnimationType` (group animation)
- Text: `TextIntro` (intro), `TextOutro` (outro), `TextLoopAnim` (looping animation)

Filter types are in `FilterType`, only for video segments.

Enum members are (usually) named directly after effect/filter names, with parameter annotations, for example:

![Effect Types](readme_assets/片段特效_annotation.jpg)

You can also use `from_name` to get a specific member, ignoring case, spaces, and underscores, e.g.:

```python
from pycapcut import VideoSceneEffectType

assert VideoSceneEffectType.from_name("__全息 扫描__") == VideoSceneEffectType.全息扫描
```

> ⚠️ Not all enum-listed effects are necessarily usable. Please verify the effect can be found in the CapCut UI before using it.

#### Add Segment Effects

Use `segment.add_effect()` to add effects. It accepts an effect type and a parameter array. The parameter order matches the order in the effect type’s annotations, which may differ from the order in the CapCut UI.

Example: add the `全息扫描` effect to a video segment, set `氛围` to 100 (CapCut value), others default:
```python
from pycapcut import VideoSceneEffectType

video_segment.add_effect(VideoSceneEffectType.全息扫描,
                         [None, None, 100.0]) # Leave first two params unset; third param (氛围) is 100; others unset
```
Audio segment effects are added similarly. For the “花栗鼠” tone, the two parameters are pitch and timbre. Both range from 0 to 100 and default to 50:

```python
from pycapcut import ToneEffectType

audio_segment.add_effect(ToneEffectType.花栗鼠, [50, 42])
```

An audio segment can have one tone effect and one scene audio effect at the same time. `ToneEffectType` provides 11 tones with adjustable parameters. Voice conversion effects that require AI processing are not supported. Some resources require a CapCut subscription; refer to the application for availability.

#### Add Segment Filters

Filters are added similarly via `VideoSegment.add_filter()`. Filters support a single “intensity” parameter.

```python
from pycapcut import FilterType

video_segment1.add_filter(FilterType.冷蓝, 10)  # Set intensity of "冷蓝" to 10
video_segment2.add_filter(FilterType.冷蓝, 50)  # Set intensity of "冷蓝" to 50
```

#### Set Segment Blend Mode

Use `VideoSegment.set_mix_mode()` to set the blend mode of an overlapping video segment. `MixModeType` provides ten modes: Multiply (正片叠底), Color Dodge (颜色减淡), Color Burn (颜色加深), Linear Burn (线性加深), Soft Light (柔光), Hard Light (强光), Screen (滤色), Overlay (叠加), Lighten (变亮), and Darken (变暗). Start the lower segment at 0 seconds on the main track, and place the upper segment on a higher track:

```python
import pycapcut as cc

# Assume script already exists and both video files are at least 5 seconds long
script.add_track(cc.TrackType.video, "Background", relative_index=0)
script.add_track(cc.TrackType.video, "Foreground", relative_index=2)
script.add_segment(cc.VideoSegment("background.mp4", cc.trange_seconds(0, duration=5)), "Background")

foreground = cc.VideoSegment("foreground.mp4", cc.trange_seconds(0, duration=5))
foreground.set_mix_mode(cc.MixModeType.正片叠底)
script.add_segment(foreground, "Foreground")
```

Each segment keeps one blend mode. Repeated calls replace it with the last setting. The upper segment must overlap the lower image for the effect to be visible.

#### Add Chroma Keying

Call `VideoSegment.add_chroma()` with a `#RRGGBBAA` color. The four numeric parameters range from 0 to 100 and correspond to intensity, shadow, edge smoothing, and spill removal. Their defaults are 20, 0, 0 and 0. Call it once per segment, before adding the segment to the script. Some controls require a CapCut subscription; refer to the application for availability.

```python
import pycapcut as cc

script.add_track(cc.TrackType.video, "Background", relative_index=0)
script.add_track(cc.TrackType.video, "Foreground", relative_index=2)
script.add_segment(cc.VideoSegment("background.mp4", cc.trange_seconds(0, duration=4)), "Background")

foreground = cc.VideoSegment("green_screen.mp4", cc.trange_seconds(1, duration=2))
foreground.add_chroma("#00FE00FF", intensity=36, shadow=10, edge_smooth=3, spill=26)
script.add_segment(foreground, "Foreground")
```

#### Effect and Filter Tracks

Besides attaching effects and filters to video segments, you can create standalone effect and filter tracks and add effect/filter segments to them.

First, create an effect track or filter track via `ScriptFile.add_track()`. For ordering, see [Multi-Track Operations](#multi-track-operations)
```python
script.add_track(cc.TrackType.effect, "my_effect")  # Create an effect track named "my_effect"
script.add_track(cc.TrackType.filter, "my_filter")  # Create a filter track named "my_filter"
```

Then use `add_effect` and `add_filter` to add segments to those tracks:
```python
from pycapcut import VideoSceneEffectType, FilterType, trange, trange_seconds

# Add a "胶片闪切" effect on the effect track, lasting 5s, with parameters
script.add_effect(VideoSceneEffectType.胶片闪切, trange_seconds(0, duration=5),
                  track_name="my_effect",  # Can be omitted if only one effect track
                  params=[50, None, 80])   # Set speed=50, keep intensity default (100), set texture=80

# Add a "冷蓝" filter to last for the entire video, intensity 70
# script.duration is in microseconds; use trange directly
script.add_filter(FilterType.冷蓝, trange(0, script.duration),
                  track_name="my_filter",  # Can be omitted if only one filter track
                  intensity=70)
```

#### Add Segment Animations

Use `segment.add_animation()` to add animations. Text intro and outro animations use the effect’s default duration when omitted; pass a duration as the second argument to override it. Loop animations fill the remaining part of the text segment. To add multiple animations, call the method multiple times on the same segment.

> ℹ For text segments, if you need both loop and in/out animations, add in/out animations first, then the loop animation

Example of adding three animations to a text segment:
```python
from pycapcut import TextIntro, TextOutro, TextLoopAnim

text_seg.add_animation(TextIntro.复古打字机).add_animation(TextOutro.弹簧)
text_seg.add_animation(TextLoopAnim.色差故障)  # Note: loop animations must be added after in/out animations
```


### Text and Subtitles

#### Add Text

Adding text is similar to adding video/audio segments: create a `TextSegment` and add it via `add_segment`. Font, text style, and image adjustments are specified via `font`, `style`, and `clip_settings`.

Example:
```python
import pycapcut as cc
from pycapcut import FontType, TextStyle, ClipSettings, trange_seconds

# A light-blue subtitle-like text with underline and positioned like subtitles
seg1 = cc.TextSegment("Subtitle", trange_seconds(0, duration=10),
                          font=FontType.思源粗宋,
                          style=TextStyle(size=5.0, color=(0.7, 0.7, 1.0), underline=True, align=1),
                          clip_settings=ClipSettings(transform_y=-0.8))
```

See `TextStyle` and `ClipSettings` constructors for details.

#### Automatic Line Wrapping

Text segments support auto-wrapping via `TextStyle.auto_wrapping` and `TextStyle.max_line_width`:

```python
# Enable auto wrapping, with max line width at 70% of screen width
seg2 = cc.TextSegment("This is a long text; when it exceeds the set max line width, it wraps automatically.",
                          trange_seconds(0, duration=10),
                          font=FontType.思源粗宋,
                          style=TextStyle(size=5.0,
                                          auto_wrapping=True,      # Enable auto wrapping
                                          max_line_width=0.7))     # Max line width at 70% of screen
```

#### Import Subtitles

> ℹ Currently only SRT format is supported

Importing subtitles essentially creates a series of texts based on each subtitle’s timestamps and content, and adds them to a track. This is done via `ScriptFile.import_srt`. Imported subtitles enable auto-wrapping by default.

Example:
```python
import pycapcut as cc

# Assume we already have a draft object `script` (see “Quick Start”)
# Import subtitles into a track named "subtitle". If the track does not exist, it will be created automatically.
# If `style` and `clip_settings` are not specified, defaults mimic CapCut’s imported subtitle style.
script.import_srt("subtitle.srt", track_name="subtitle", time_offset="1.5s")  # Shift the subtitles by 1.5s
```

The following examples are alternatives. Choose the one you need to avoid importing overlapping subtitles into the same track.

```python
# Adjust subtitle styles using `text_style` and `clip_settings` (same semantics as in `TextSegment()`)
script.import_srt("subtitle.srt", track_name="subtitle",
                  text_style=cc.TextStyle(size=10.0, color=(1.0, 0.0, 0.0)),
                  clip_settings=cc.ClipSettings(transform_y=0.8))  # Place subtitles at the top of the screen
```

```python
# For more complex styles or to apply animations, pass a `TextSegment` as `style_reference` (text and duration are ignored)
# Note animation timing does not adapt to segment length; very short subtitle segments may look odd
script.import_srt("subtitle.srt", track_name="subtitle", style_reference=seg1)  # Use `seg1` from “Add Text” as reference
```

```python
# By default `clip_settings` from `style_reference` is not applied. Pass `clip_settings=None` if you want to adopt it.
script.import_srt("subtitle.srt", track_name="subtitle", style_reference=seg1, clip_settings=None)  # Equivalent to clip_settings=seg1.clip_settings
```
