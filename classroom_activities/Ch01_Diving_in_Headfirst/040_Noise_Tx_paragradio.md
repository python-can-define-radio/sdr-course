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

Open a terminal and type `marimo edit`. Create a new notebook and save it as **noise_tx.py**. (For an intro to marimo, reference the [lesson in the Github python-course](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2024_12 import Noise_Tx

#### In the second cell:
moose = Noise_Tx()
moose.set_amplitude(1)
moose.set_noise_type("gaussian)
moose.start()
```

If it runs, you should see this:

[[TODO: Image of Noise_tx]]

Technically we do not require any sink for the transmission to work but we have added a single waterfall sink in order to view our transmission.

We have the same methods available as we had in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `set_center_freq()`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available.

```python3
## 2
## Make a Numeric text field to control the center frequency.
## Set the left and right limits to match the frequency range available to the HackRf One
```

```python3
## 3
## Make a dropdown to control the IF gain. 
## The options should match the HackRF One's hardware specs.
```

```python3
## 4
## Make a dropdown to control the filter cutoff width. 
## Have three options: Narrow, Normal, Wide
```

```python3
## 5
## Make a dropdown to control the filter transition width. 
## Have three options: Narrow, Normal, Wide
```

Adjust each UI element, and watch for changes in the view to ensure proper functionality.


#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
