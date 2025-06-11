# Paragradio FM Radio

ℹ️ This material coincides with material from SDR slideshow C (slides 1-44).  However, the slides are not necessary for building and operating this program.

### Introduction

Like we stated in the spectrum analyzer lesson, most of us have listened to an FM Radio at least once in our lives. Now let's try to build one for ourselves. 

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install --upgrade "paragradio==2025.3.*"
pip install marimo
```

### FM Radio

Open a terminal and type `marimo edit`. Create a new notebook and save it as **fm_radio.py**. (For an intro to marimo, reference the [lesson in the Github python-course](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## Exercise 1
## Try this.
#### Name the first cell "imports". Put this code:
import marimo as mo
from paragradio.v2025_03 import WBFM_Rx

#### Name the second cell "launch". Put this code:
WBFM_Rx.config(running=True)
```

If it runs, you should see two waterfall sinks and a frequency sink:

![WBFM_Rx.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/WBFM_Rx.png?raw=true)  

The first waterfall sink is the spectrum as it is received from the HackRF with no software filtering.[^1] The second is the same spectrum, with software filtering to remove signals outside of the target listening region. The frequency sink shows the same signal as the first waterfall, before software filtering.

Many of the parameters of `config` are the same as the `SpecAn` discussed in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `center_freq`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available. Try using the "help(WBFM_Rx.config)" in a marimo cell for more information.

### Why are all radio stations odd numbers?

As we'll see in the waterfall view, the channel width for WBFM broadcasting in the United States is standardized to be 200 kHz. [This article from the FCC](https://www.fcc.gov/media/radio/fm-frequencies-end-odd-decimal) explains this. FCC regulations also require that stations use less than the full 200 kHz channel width in order to not interfere with neighboring stations.

#### Adding other UI elements

To improve the user experience, we can add various Marimo UI elements.

```python3
## Exercise 2
## Name the third cell "create_ui". 
## Name the fourth cell "render_ui".
## Create and render a `mo.ui.number` element that controls the center frequency.
## Set the label to "Center Frequency".
## Set the left and right limits to match the US WBFM Broadcast range taking into account the 200 kHz channel width.
```

```python3
## Exercise 3
## In the "create_ui" cell, add a slider to control the BB gain.
## The range should match the HackRF One's hardware specs.
## Set the label to "BB Gain".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 4
## In the "create_ui" cell, add a dropdown to control the IF gain. 
## The options should match the HackRF One's hardware specs.
## The labels for the options should be the words "zero", "eight", etc.
## Set the label to "IF Gain".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 5
## In the "create_ui" cell, add a dropdown to control the channel width. 
## Have three options: Narrow, Normal, Wide.
## Those labels should correspond to filter values of
##   120 kHz, 160 kHz, and 200 kHz respectively.
## Set the label to "Channel Width".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 6
## In the "create_ui" cell, add a `mo.ui.number` element to control the frequency offset.
##   - Left Limit: -2 MHz
##   - Right Limit: 2 MHz
##   - Step value: 5 kHz
##   - Default value: 0 kHz
##   - Label: "Frequency Offset"
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 7
## In the "create_ui" cell, add a switch element that controls whether the FM_Radio is running.
## Set the label to "Off/On".
## Render the element in the "render_ui" cell.
```

<!-- ```python3
## Make a .... to control the squelch.
``` -->

Adjust each UI element, and watch for changes in the view to ensure proper functionality.

#### Using UI elements together

In a car radio, you often have buttons for favorite stations. We can do something similar in Marimo by providing both radio buttons and a slider, as shown in the following sequence of examples.

```python3
## Exercise 8
## In the "create_ui" cell, remove or comment any UI elements that control the frequency. 
## Then add the following:
freqsli = mo.ui.slider(90e6, 93e6, label="Center Frequency")

## Create a new cell called "create_radio_buttons", add the following:
favorites = mo.ui.radio({"Use Slider": freqsli.value, "A": 91.3e6, "B": 92.5e6}, value="Use Slider", label="Favorite station")

## Render both elements in the "render_ui" cell.

## In the "launch" cell, set the 
## center_freq to `favorites.value`. This should
## allow BOTH of the ui elements to work. Test both 
## to ensure that they both work.
```



<details><summary>Optionally, you can create a dropdown menu that switches between `mo.ui.radio` and `mo.ui.slider`. Click here to expand to see.</summary>

## _Note: this method should not be used on our graded assignments._

Recommended: create a new notebook for this example called **fm_radio_dropdown.py**.

```python3
## In the first cell, put your imports as mentioned above.

## In the second cell, launch a WBFM receiver as above.
## In `config`, the center_freq should be set to the value of freq_ui_elem, which we create below.

## In the third cell:
tuner_ui = mo.ui.dropdown(["radio buttons", "slider"], label="Tune using", value="radio buttons", allow_select_none=False)

## In the fourth cell:
if tuner_ui.value == "slider":
    freq_ui_elem = mo.ui.slider(88e6, 108e6, 0.1e6, label="Station", show_value=True)
elif tuner_ui.value == "radio buttons":
    freq_ui_elem = mo.ui.radio({"Some station": 100.1e6, "Another": 102.3e6}, label="Station", value="Another")
else:
    raise ValueError('The dropdown menu should only have exactly two options: "slider" and "radio buttons". If you see this error, it most likely means that you have a typo or capitalization error.')

## In the fifth cell:
mo.md(f"""
{tuner_ui}  
{freq_ui_elem}
""")

```

This will create three UI elements:
- A dropdown that allows the user to choose between radio buttons and a slider.
- A slider that tunes the frequency.
- Radio buttons that tune the frequency to one of a collection of provided options.

</details>

#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure that they can receive at least one radio station, asking an instructor for assistance as needed.

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).

#### Footnotes

[^1]: While it doesn't have any _software_ filtering applied, the effects of _hardware_ filtering will show up in this view of the spectrum. Thus, it is not an "unfiltered" view, but a "pre-software filtering" view.
