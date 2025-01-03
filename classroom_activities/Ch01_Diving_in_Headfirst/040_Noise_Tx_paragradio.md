# Paragradio Noise transmitter

ℹ️ This material coincides with material from SDR slideshow E (all slides).

### Introduction

Transmitting noise has a few uses. It can be used for research purposes, to test how well a signal is able to be demodulated in the presence of background noise. It can also be used to prevent others from using a specific frequency or range of frequencies. If the intent is disrupting legitimate users, it would be called jamming.

_Disclaimer: jamming is illegal in many countries. This should only be used in an environment that is sufficiently distant/radio-shielded from other electronics using those frequencies._

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install paragradio
pip install marimo
```

### Noise Transmitter

Open a terminal and type `marimo edit`. Create a new notebook and save it as **noise_tx.py**. (For an intro to marimo, reference this lesson [01_marimo.md](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md) in the Github python-course).

Copy the following:

```python3
## Exercise 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2025_02 import Noise_Tx

#### In the second cell:
moose = Noise_Tx()
moose.set_amplitude(1)
moose.set_noise_type("gaussian")
sr = 2e6
moose.set_samp_rate(sr)
moose.start()
```

If it runs, you should see a waterfall display. Note that it's possible to make a noise transmitter without a waterfall display. The display does not make the transmitter work better; it just provides a view of what is being transmitted.

We have the same methods available as we had in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `set_center_freq()`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available.

```python3
## Exercise 2
## Make a Numeric text field to control the center frequency.
## Set the left and right limits to match the frequency range available to the HackRf One
```

```python3
## Exercise 3
## Make a dropdown to control the IF gain. 
## The options should match the HackRF One's hardware specs.
```

```python3
## Exercise 4
## Make a slider to control the filter cutoff width. 
## The parameters should have these values: 
    - Left Limit: 2e3
    - Right Limit: sr/2
    - Step value: 1e3
```

```python3
## Exercise 5
## Make a slider to control the filter transition width. 
## The parameters should have these values: 
    - Left Limit: 2e3
    - Right Limit: sr/2
    - Step value: 1e3
```

#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure with a partner that their Noise Transmitter signal can be seen, adjust each UI element, and watch for changes in the partners view to ensure proper functionality. asking an instructor for assistance as needed.

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
