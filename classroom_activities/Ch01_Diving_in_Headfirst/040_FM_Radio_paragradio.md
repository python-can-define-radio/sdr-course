# Paragradio FM Radio

ℹ️ This material coincides with material from SDR slideshow C (slides 1-44).  However, the slides are not necessary for building and operating this program.

### Introduction

Like we stated in the spectrum analyzer lesson, most of us have listened to an FM Radio at least once in our lives. Now let's try to build one for ourselves. 

### Dependencies

In the terminal, run these:

```
pip install paragradio
pip install marimo
```

### Execution

Open a new Marimo notebook. (For an intro to marimo, reference the lesson in the github python course [Marimo Lesson](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2024_12 import WBFM_rx

#### In the second cell:
fmrx = WBFM_rx()
fmrx.start()
```

If it runs, you should see this:

[[TODO: Image of FM_radio]]

Discussion on FM Radio sinks: waterfall unfiltered, waterfall filtered to the listening region

We have the same methods available as we had in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_Spec_A_paragradio.md), such as `set_center_freq()`. There are also a few new ones:

- `set_freq_offset` adjusts the frequency that is being demodulated.
- `set_channel_width` adjusts the width of the band-pass filter, usually with the goal of matching the width of the transmitted station. [^1]

Examples:

```python3
## 2
fmrx.set_freq_offset(500e3)
```

```python3
## 3
fmrx.set_channel_width(200e3)
```

What did they do?

#### Adding a slider

To improve the user experience, we can add various Marimo UI elements.

```python3
## 4
## Make a Numeric text field to control the center frequency.
## Set the left and right limits to match the US WBFM Broadcast range.
```

```python3
## 5
## Make a slider to control the BB gain.
## The range should match the HackRF One's hardware specs.
```

```python3
## 6
## Make a dropdown to control the IF gain. 
## The options should match the HackRF One's hardware specs.
```

```python3
## 7
## Make a dropdown to control the filter width. 
## Have three options: Narrow, Normal, Wide
```

```python3
## 8
## Make a Numeric text field to control the frequency offset.
```

<!-- ```python3
## 3
## Make a .... to control the squelch.
``` -->

Adjust the UI elements, and watch for changes in the view to ensure functionality.

#### Checkpoint Activity

The instructor will provide 15 minutes for students to experiment.

#### Modifying the parameters

Adjust the UI elements, and watch for changes in the view to ensure functionality.

#### What to expect on the assessment

For the graded assignment, you'll have access to this lesson. You'll be expected to know the name and meaning of each of the parameters. We'll ask you to modify certain parameters, and you'll need to know what parameter we're referring to and where it would need to be modified in the provided code.

#### Footnotes

[^1]:  As we'll see in the waterfall view, the channel width for WBFM broadcasting in the United States is standardized to be 200 kHz. As [this article from the FCC describes](https://www.fcc.gov/media/radio/fm-frequencies-end-odd-decimal), this is why stations are always spaced by 0.2 MHz (200 kHz). Most stations use less than the full 200 kHz channel width in order to respect neighboring stations.