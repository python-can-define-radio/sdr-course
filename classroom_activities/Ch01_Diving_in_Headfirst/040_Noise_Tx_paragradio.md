# Paragradio Noise transmitter

ℹ️ This material coincides with material from SDR slideshow E (all slides).

### Introduction

Transmitting noise has a few uses. It can be used for research purposes, to test how well a signal is able to be demodulated in the presence of background noise. It can also be used to prevent others from using a specific frequency or range of frequencies. If the intent is disrupting legitimate users, it would be called jamming.

_Disclaimer: jamming is illegal in many countries. This should only be used in an environment that is sufficiently distant/radio-shielded from other electronics using those frequencies._

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install --upgrade "paragradio==2025.3.*"
pip install marimo
```

### Noise Transmitter

Open a terminal and type `marimo edit`. Create a new notebook and save it as **noise_tx.py**. (For an intro to marimo, reference this lesson [01_marimo.md](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md) in the Github python-course).

Copy the following:

```python3
## Exercise 1
## Try this.
#### Name the first cell "imports". Put this code:
import marimo as mo
from paragradio.v2025_03 import Noise_Tx

#### Name the second cell "launch". Put this code:
Noise_Tx.config(
    running=True,
    center_freq=2.45e9,
)
```

If it runs, you should see a waterfall display. Note that it's possible to make a noise transmitter without a waterfall display. The display does not make the transmitter work better; it just provides a view of what is being transmitted.

Many of the parameters of `config` are the same as the `SpecAn` discussed in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `center_freq`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available. Try using the "help(Noise_Tx.config)" in a marimo cell for more information.

```python3
## Exercise 2
## Name the third cell "create_ui". 
## Name the fourth cell "render_ui".
## In the "create_ui" cell, add a slider to control the amplitude.
## The parameters should have these values: 
##   - Left Limit: 0
##   - Right Limit: 30
##   - Step value: 0.01
##   - Default value: 0.5
##   - Label: Amplitude
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 3
## In the "create_ui" cell, add a `mo.ui.number` element to control the center frequency.
## Set the left and right limits to match the frequency range available to the HackRF One.
## Set the label to "Center Frequency".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 4
## In the "create_ui" cell, add a slider to control the IF gain. 
## The options should match the HackRF One's hardware specs.
## Set the label to "IF Gain".
## Hint: we're transmitting. What are the IF gain requirements?
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 5
## In the "create_ui" cell, add a slider to control the filter cutoff frequency. 
## The parameters should have these values: 
##   - Left Limit: 2 kHz
##   - Right Limit: 400 kHz
##   - Step value: 1 kHz
##   - Label: "Cutoff Frequency"
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 6
## In the "create_ui" cell, add a slider to control the filter transition width. 
## The parameters should have these values: 
##   - Left Limit: 2 kHz
##   - Right Limit: 500 kHz
##   - Step value: 1 kHz
##   - Label: "Transition width"
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 7
## In the "create_ui" cell, add a switch element that controls whether the Noise_Tx is running.
## Set the label to "Off/On".
## Render the element in the "render_ui" cell.
```



#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure with a partner that their Noise Transmitter signal can be seen, adjust each UI element, and watch for changes in the partners view to ensure proper functionality. asking an instructor for assistance as needed.

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
