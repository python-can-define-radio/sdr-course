# Paragradio PSK transmitter

ℹ️ This material coincides with material from SDR slideshow F (all slides).

### Introduction

In the modern world, trillions of bits are sent wirelessly every day. How do we modulation electromagnetic waves to commuicate this massive amount of data? One way to do so is using Phase Shift Keying, or PSK.

### Dependencies

In the terminal, if you haven't already, run these:

```
pip install paragradio
pip install marimo
```

### PSK Transmitter

Create a new notebook and save it as **psk_tx.py**. (For an intro to marimo, reference the lesson in the github python course [Marimo Lesson](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2025_02 import PSK_Tx_loop

#### In the second cell:
phaser = PSK_Tx_loop()    # This was updated 2025 Jan 13. Requires paragradio version 2025.2.4
phaser.start()
data = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0]
phaser.set_center_freq(2.43e9)
phaser.set_data(data)
phaser.set_amplitude(1)
phaser.set_if_gain(32)
```

If it runs, you should see a window open. It includes a waterfall sink and a time sink so you can see the bits being transmitted.

We have the same methods available as we had in the [Spectrum Analyzer Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md), such as `set_center_freq()`. There are also a few new ones. As before, we recommend investigating and experimenting with each to learn what functionality is available.

```python3
## 2
## Make a Numeric text field to control the center frequency.
## Set the left and right limits to match the frequency range available to the HackRf One.
```

```python3
## 3
## Make a slider to control the IF gain. 
## The parameters should match the HackRF One's hardware specs.
```

```python3
## 4
## Make a dropdown menu to pick between the five modulation options.
```

#### Checkpoint Activity

The instructor will provide 30 minutes for students to experiment. Each student should ensure with a partner that their PSK Transmitter signal can be seen, adjust each UI element, and watch for changes in the partners view to ensure proper functionality. asking an instructor for assistance as needed.

#### Creating more interesting data

You can generate random bits like so:

```python3
import random
bits = random.choices([0, 1], k=100)
print(bits)
phaser.set_data(bits)
```

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#what-to-expect-on-the-assessment).
