# Paragradio PSK transmitter

ℹ️ This material coincides with material from SDR slideshow F (all slides).

### Introduction

In the modern world, trillions of bits are sent wirelessly every day. How do we use electromagnetic waves to communicate this massive amount of data? One way to do so is using Phase Shift Keying, or PSK.

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install --upgrade "paragradio==2025.3.*"
pip install marimo
```

### PSK Transmitter

Create a new notebook and save it as **psk_tx_loop.py**. (For an intro to marimo, reference the lesson in the github python course [Marimo Lesson](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## Exercise 1
## Try this.
#### Name the first cell "imports". Put this code:
import marimo as mo
from paragradio.v2025_03 import PSK_Tx_loop

#### Name the second cell "launch". Put this code:
PSK_Tx_loop.config(
    data=[1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    center_freq=2.43e9,
)
```

If it runs, you should see a window open. It includes a waterfall sink and a time sink so you can see the bits being transmitted.

Many of the parameters of `config` are the same as the `SpecAn` discussed in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `center_freq`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available. Try using the "help(PSK_Tx_loop.config)" in a marimo cell for more information.

```python3
## Exercise 2
## Name the third cell "create_ui". 
## Name the fourth cell "render_ui".
## In the "create_ui" cell, add a `mo.ui.number` element to control the center frequency.
## Set the left and right limits to match the frequency range available to the HackRf One.
## Set the label to "Center Frequency".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 3
## In the "create_ui" cell, add a slider element to control the IF gain.  
## The parameters should match the HackRF One's hardware specs.
## Set the label to "IF Gain".
## Render the element in the "render_ui" cell.
```

```python3
## Exercise 4
## In the "create_ui" cell, add a dropdown menu to pick between all available modulation options.
## Set the label to "Modulation".
## Render the element in the "render_ui" cell.
## Remember to use "help(PSK_Tx_loop.config)" in a marimo cell for more information.
```

```python3
## Exercise 5
## In the "create_ui" cell, add a switch element that controls whether the PSK_Tx is running.
## Set the label to "On/Off".
## Render the element in the "render_ui" cell.
```


#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure with a partner that their PSK Transmitter signal can be seen, adjust each UI element, and watch for changes in the partners view to ensure proper functionality. asking an instructor for assistance as needed.

#### Creating more interesting data

You can generate random bits like so:

```python3
import random
bits = random.choices([0, 1], k=100)
print(bits)
```

As an exercise, try to use the `bits` variable as your `data` in `PSK_Tx_loop.config`.

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
