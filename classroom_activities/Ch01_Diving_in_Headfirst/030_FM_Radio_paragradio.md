# Paragradio FM Radio

ℹ️ This material coincides with material from SDR slideshow C (slides 1-44).  However, the slides are not necessary for building and operating this program.

### Introduction

Like we stated in the spectrum analyzer lesson, most of us have listened to an FM Radio at least once in our lives. Now let's try to build one for ourselves. 

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install paragradio
pip install marimo
```

### FM Radio

Open a terminal and type `marimo edit`. Create a new notebook and save it as **fm_radio.py**. (For an intro to marimo, reference the [lesson in the Github python-course](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## Exercise 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2024_12 import WBFM_rx

#### In the second cell:
fmrx = WBFM_rx()
fmrx.start()
```

If it runs, you should see two waterfall sinks:

[[TODO: Image of FM_radio]]

The first waterfall sink is the spectrum as it is received from the HackRF with no software filtering.[^1] The second is the same spectrum, with software filtering to remove signals outside of the target listening region.

We have the same methods available as we had in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `set_center_freq()`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available.

### Why are all radio stations odd numbers?

As we'll see in the waterfall view, the channel width for WBFM broadcasting in the United States is standardized to be 200 kHz. [This article from the FCC](https://www.fcc.gov/media/radio/fm-frequencies-end-odd-decimal) explains this. FCC regulations also require that stations use less than the full 200 kHz channel width in order to not interfere with neighboring stations.

#### Adding other UI elements

To improve the user experience, we can add various Marimo UI elements.

```python3
## Exercise 2
## Make a Numeric text field to control the center frequency.
## Set the left and right limits to match the US WBFM Broadcast range.
```

```python3
## Exercise 3
## Make a slider to control the BB gain.
## The range should match the HackRF One's hardware specs.
```

```python3
## Exercise 4
## Make a dropdown to control the IF gain. 
## The options should match the HackRF One's hardware specs.
```

```python3
## Exercise 5
## Make a dropdown to control the filter width. 
## Have three options: Narrow, Normal, Wide.
## Those labels should correspond to filter values of
##   120 kHz, 160 kHz, and 200 kHz respectively.
```

```python3
## Exercise 6
## Make a Numeric text field to control the frequency offset.
```

<!-- ```python3
## Make a .... to control the squelch.
``` -->

Adjust each UI element, and watch for changes in the view to ensure proper functionality.

#### Using UI elements together

In a car radio, you often have buttons for favorite stations. We can do something similar in Marimo by using a slider and a radio butttons widget together, as shown in the following example.

Recommended: create a new notebook for this example called **fm_radio_buttons_and_slider.py**.

```python3
## In the first cell, put your imports as mentioned above.

## In the second cell, create an instance of a WBFM receiver.

## In the third cell:
cfslider = mo.ui.slider(88.3, 99.5, 0.1)
cfslider

## In the fourth cell:
radiobuttons = mo.ui.radio({"Bob FM": 93.9, "WKXC": 95.5, "Use slider": 0})
radiobuttons

## In the fifth cell:
if radiobuttons.value == 0:
    tunemsg = "Tuning using slider"
    tunefreq = cfslider.value
else:
    tunemsg = "Tuning using radio buttons"
    tunefreq = radiobuttons.value

## In the sixth cell:
fmrx.set_center_freq(tunefreq*1e6)

## In the seventh cell:
f"{tunemsg}. Frequency: {tunefreq} MHz, which is {tunefreq*1e6} Hz."
```

Ways to explore:
- How can you tell whether the frequency is tuning correctly?
- What happens if you do `fmrx.set_center_freq(tunefreq)` without the `*1e6`?
- What happens if you do `*1e4` instead of `*1e6`?

#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure that they can receive at least one radio station, asking an instructor for assistance as needed.

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_Spec_A_paragradio.md#what-to-expect-on-the-assessment).

#### Footnotes

[^1]: While it doesn't have any _software_ filtering applied, the effects of _hardware_ filtering will show up in this view of the spectrum. Thus, it is not an "unfiltered" view, but a "pre-software filtering" view.
