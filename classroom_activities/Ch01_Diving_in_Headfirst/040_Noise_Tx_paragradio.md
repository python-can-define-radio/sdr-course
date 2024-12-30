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
moose.start()
```

If it runs, you should see this:

[[TODO: Image]]

Discussion on sinks: TODO

```python3
## 2
TODO
```

```python3
## 3
TODO
```

What did they do?


#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
