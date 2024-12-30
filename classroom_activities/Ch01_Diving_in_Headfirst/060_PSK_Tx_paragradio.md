# Paragradio PSK transmitter

ℹ️ This material coincides with material from SDR slideshow F (all slides).

### Introduction

TODO

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
from paragradio.v2024_12 import PSK_Tx_loop

#### In the second cell:
phaser = PSK_Tx_loop()
phaser.start()
```

If it runs, you should see this:

[[TODO: Image]]

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

To improve the user experience, we can add a slider to control the frequency. This could be done using any graphics toolkit (Guizero, PyQt, PyGame, etc). In this lesson, we'll use Marimo.

```python3
## 3
## Try this.
cfslider = mo.ui.slider(start=92.5, stop=94.5, step=0.01, label="Frequency (MHz)", show_value=True)
cfslider
```

This will create and display a slider, but the slider doesn't do anything yet. (Try sliding it to confirm.)

To make it actually work, insert this:

```python3
## 4
simsp.set_center_freq(slider.value)
```

Adjust the slider, and you should see the view of the spectrum adjust accordingly.

Now, let's start using hardware. First, let's run the code without plugging in the hardware, so we can see the error message:

```python3
## 2
## Try this. You should get an error.
specan = PGR_specan()
specan.start()
specan.set_center_freq(104.5e6)
```

You should see `Failed to launch ... not enough devices [[ TODO: actual err msg]]`. As we expected, having no devices plugged in causes this error.

#### Intro to the HackRF One

Open your HackRF One box [[ TODO: assembly discussion, careful antenna, etc. Also discuss the HackRF docs, including block diagram, sample rate limitations (tell them this is the instantaneous bandwidth that it can see), gain limitations, transmit power limitations, pointing out that we chose 2.437 GHz because the HackRF One is stronger in this band ]]

Run the code again with the HackRF plugged in, and you should see something very similar to the simulated spectrum analyzer. The difference is that these are frequencies are being measured from the universe around you!

[[ TODO: Image of Spec A ]]

The spectrum will vary depending on what activity (if any) is present on those frequencies in your area.

#### Checkpoint Activity

The instructor will ensure that everyone has working hardware by doing the following activity:

1. The instructor will transmit a pure sine wave on 2.437 GHz that toggles on and off every few seconds.
2. Students will adjust the Python code to tune to 2.4369 GHz.
3. Students will look at the waterfall sink or the frequency sink to see the spike of activity appearing and disappearing.

Notice that you (the student) tuned to a frequency that was slightly offset from the transmitted frequency. This is because the Hack RF (and most SDR devices that aren't terribly expensive) have a "DC Spike" on the center frequency of the received spectrum. We tune off-center so that this spike doesn't obscure or distort the frequency of interest.

#### Modifying the parameters

[[ TODO: Show center frequency slider, if gain slider, bb gain slider, sample rate, hardware filter (adjustable, not simply on/off)]]

[[ Why you should almost always use the hardware filter (link to resources that state as much) ]]

#### What to expect on the assessment

See [here](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_Spec_A_paragradio.md#what-to-expect-on-the-assessment).