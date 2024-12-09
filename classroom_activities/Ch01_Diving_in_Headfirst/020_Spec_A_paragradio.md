
# GRC Spectrum Analyzer

ℹ️ This material coincides with material from SDR slideshow D (slides 1-27).  However, the slides are not necessary for building and operating this program.

Prerequisite: basic knowledge of [guizero](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/03_guizero.md), specifically creating an `App` with `Text` and `Slider` widgets.

### Introduction

Viewing the spectrum is useful. In order to effect change to the electromagnetic spectrum we first have to be able to `see` those frequencies.

### Execution

We'll start by displaying a simulated signal. This allows us to familiarize ourselves with the Python code that launches GNU Radio.

```python3
## 1
## Try this.
from paragradio.v2024_12 import PGR_sinewave
pgr = PGR_sinewave(simulated_freq=1e6)
pgr.start()
## [[ TODO: Does this stay open without needing to do something like a while loop to keep the computer busy?]]
```

If you get an error saying "No module named ...", pip install [[TODO]]

If it runs, you should see this:

[[TODO: Image of simulated sine wave in QT GUI Sink]]

Looking at the x-axis, we see [[TODO time disucssion, look how it's 1 MHz]]

[[ Also discuss the other tabs. constellation sink: say "outside scope of lesson" ]]

Now, let's start using hardware. First, let's run the code without plugging in the hardware, so we can see the error message:

```python3
## 2
## Try this. You should get an error.
from paragradio.v2024_12 import PGR_specan
default_freq = 98e6
default_gain = 16
pgr = PGR_specan(default_freq, default_gain)
pgr.start()
```

You should see `Failed to launch ... not enough devices [[ TODO: actual err msg]]`. As we expected, having no devices plugged in causes this error.

### Intro to the HackRF One

Open your HackRF One box [[ TODO: assembly discussion, careful antenna, etc. Also discuss the HackRF docs, including block diagram, sample rate limitations (tell them this is the instantaneous bandwidth that it can see), gain limitations, transmit power limitations, pointing out that we chose 2.437 GHz because the HackRF One is stronger in this band ]]

Run the code again with the HackRF plugged in, and you should see something like this:

[[ TODO: Image of Spec A ]]

The spectrum will vary depending on what activity (if any) is present on those frequencies in your area.

### Checkpoint Activity

The instructor will ensure that everyone has working hardware by doing the following activity:

1. The instructor will transmit a pure sine wave on 2.437 GHz that toggles on and off every few seconds.
2. Students will adjust the Python code to tune to 2.4369 GHz.
3. Students will look at the waterfall sink or the frequency sink to see the spike of activity appearing and disappearing.

Notice that you (the student) tuned to a frequency that was slightly offset from the transmitted frequency. This is because the Hack RF (and most SDR devices that aren't terribly expensive) have a "DC Spike" on the center frequency of the received spectrum. We tune off-center so that this spike doesn't obscure or distort the frequency of interest.
