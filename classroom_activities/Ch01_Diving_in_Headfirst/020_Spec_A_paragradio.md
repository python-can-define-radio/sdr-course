# Paragradio Spectrum Analyzer

ℹ️ This material coincides with material from SDR slideshow D (slides 1-27).  However, the slides are not necessary for building and operating this program.

### Introduction

Most of us have listened to an FM Radio at least once in our lives. We may even know that the music on these radio stations is transmitted using electromagnetic waves. However, it can be difficult to imagine what these invisible waves look like. A Spectrum Analyzer is one way to **_see_** those frequencies. 

### Dependencies

In the terminal, run these:

```
pip install paragradio
pip install marimo
```

### Simulated Spectrum Analyzer

We'll start by looking at a simulated spectrum analyzer. This allows us to familiarize ourselves with the Python code that launches GNU Radio without the hardware initially.

Open a terminal and type `marimo edit`. Create a new notebook and save it as **simspecan.py**. (For an intro to marimo, reference the [lesson in the Github python-course](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/01_marimo.md)).

Copy the following:

```python3
## Exercise 1
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2025_02 import SpecAnSim

#### In the second cell:
simsa = SpecAnSim()
simsa.start()
```

If it runs, you should see this:

![specAnSim.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specAnSim1.png?raw=true)  
 
For better viewing:
- in order to watch the changes as you make them, and if you do not have a secondary screen available, right click on the titlebar of the running spectrum analyzer and select ***always on top***.
- resize or move as necessary so it does not obstruct your view.

You'll see three views of the signal: the Time Domain view, the Frequency Domain view, and a Waterfall view.

- The Time Domain shows the raw signal as it is received from the USB port. (x-axis: time; y-axis: amplitude)
- The Frequency Domain shows the amount of each frequency that is present in the slice of the spectrum that we have selected. (x-axis: frequencies; y-axis: amplitude)
- The Waterfall shows the same information as the Frequency Domain, but using colors to represent strength of signal instead of the height of the spike. It also scrolls, which provides a view of the the history of the signal. (x-axis: frequencies; y-axis: time; colors: amplitude)

```python3
## Exercise 2
## Keep the same Marimo cells shown above.
## In the third cell:
simsa.set_center_freq(93.7e6)
```

What did it do? Look closely at the simspecan, then change the frequency and try again.

To improve the user experience, we can add a slider to control the frequency. This could be done using any graphics toolkit (Guizero, PyQt, PyGame, etc), but we will continue to use Marimo.

```python3
## Exercise 3
## In the fourth cell:
cfslider = mo.ui.slider(start=92.5e6, stop=94.5e6, step=10e3, label="Frequency (MHz)", show_value=True)
cfslider
```

This will create and display a slider, but the slider doesn't do anything yet. (Try sliding it to confirm.)

Let's make it actually work:

```python3
## Exercise 4
## Update the third cell to use the slider value:
simsa.set_center_freq(cfslider.value)
```

Adjust the slider, and you should see the view of the spectrum adjust accordingly.

#### Improving the display of the chosen frequency

You can show the frequency in a more pleasant way like so:

```python3
## Exercise 4b
## In the fifth cell:
cfslider, f"{cfslider.value} Hz",  f"{cfslider.value/1e3} kHz", f"{cfslider.value/1e6} MHz", f"{cfslider.value/1e9} GHz"
```

Now, let's start using hardware. 

#### Intro to the HackRF One

Your instructor will...

- Guide you through the assembly of the HackRF One
- Discuss the [HackRF documentation](https://hackrf.readthedocs.io/en/latest/), including...
  - The [Block diagram](https://hackrf.readthedocs.io/en/latest/_images/block-diagram.png)
  - The [Sample rate limitations and Frequency range](https://hackrf.readthedocs.io/en/latest/hackrf_one.html#features)[^1]
  - The [Gain limitations](https://hackrf.readthedocs.io/en/latest/faq.html#what-gain-controls-are-provided-by-hackrf)
  - The [Transmit power limitations](https://hackrf.readthedocs.io/en/latest/faq.html#what-is-the-transmit-power-of-hackrf)

### Spectrum Analyzer

Create a new Marimo notebook and save it as **specan.py**.
- If you don't see the "Create a new notebook" option, exit your current notebook by clicking the three lines in the top right of your screen and selecting Return home.

```python3
## Exercise 5
## Try this.
#### In the first cell:
import marimo as mo
from paragradio.v2025_02 import SpecAn

#### In the second cell:
sa = SpecAn()
sa.start()
sa.set_center_freq(2.4369e9)
```

You should see something very similar to the simulated spectrum analyzer. The difference is that these frequencies are being measured from the universe around you!  
If it doesn't work, ensure you have plugged in your HackRF One.

![specAn.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specAnSim2.png?raw=true) 

The spectrum will vary depending on what activity (if any) is present on those frequencies in your area.

#### Checkpoint Activity

The instructor will ensure that everyone has working hardware by doing the following activity. _If you are doing this lesson without instructor guidance, have a partner [create a transmitter](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#transmission-code)._
  
1. The instructor or your partner will transmit a narrow signal on 2.437 GHz that toggles on and off every few seconds.
2. Students will look at the waterfall sink or the frequency sink to see the spike of activity appearing and disappearing.

Notice that you (the student) tuned to a frequency that was slightly offset from the transmitted frequency (2.4369 GHz rather than 2.437 GHz). This is because the Hack RF (and most SDR devices that aren't terribly expensive) have a "DC Spike" on the center frequency of the received spectrum. We tune off-center so that this spike doesn't obscure or distort the frequency of interest.

Review: Why do you think we chose 2.437 GHz? [Hint](https://hackrf.readthedocs.io/en/latest/faq.html#what-is-the-transmit-power-of-hackrf).

#### Modifying the parameters

We've seen one of the spectrum analyzer's methods, `set_center_freq`. There are a few others available. Here's how to see them:

```python3
## Exercise 6
## In the third cell:
sa.
```

Marimo should show possible completions:

![completions.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specAnSim3.png?raw=true) 

Notice that each method's documentation is also visible. We recommend investigating and experimenting with each to learn what functionality is available.

#### What to expect on the assessment

For the graded assignment...
- You'll have access to this lesson, your own notes, and the Hack RF Docs. You will not be allowed to use any other resources.
- You'll be expected to be able to use the metric prefixes kilo, Mega, and Giga. For example, if the assignment says "Tune to 350 MHz", you'll need to be able to convert that to `350e6 Hz` or `0.35 GHz`. As a reminder, you will not be allowed to use online converter tools.
- You'll be expected to know the name and meaning of each of the parameters that is settable using a method (such as `set_if_gain`), ***including those which are not mentioned in the lesson above***.
  - If you need help finding the list of available methods, ask an instructor.
- You'll be asked to create Marimo UI elements that control specific parameters, similar to the `cfslider` above.
  - The Marimo UI elements will be limited to any that you've seen in this lesson or any previous lessons.
- You'll be expected to know the Hack RF's limitations for each settable parameter in order to adjust the associated settings in the UI elements. For example, Marimo sliders have a `step` parameter, and the HackRF One requires a Rx IF Gain step value of 8.[^2]
- If you'd like to practice, try creating Marimo UI elements to control each parameter, and ask an instructor to check your work.

#### Transmission code:

The following code is one way to create a transmission for testing that your Hack RF is able to receive signals.

```python3
from paragradio.v2025_02 import Noise_Tx
import time
ntx = Noise_Tx()
ntx.start()
ntx.set_center_freq(2.437e9)
ntx.set_filter_cutoff_freq(50e3)
ntx.set_filter_transition_width(50e3)
while True:
    ntx.set_amplitude(100)
    ntx.set_if_gain(47)
    time.sleep(2)
    ntx.set_amplitude(0)
    ntx.set_if_gain(0)
    time.sleep(2)
```

[^1]: The Sample rate limits the instantaneous bandwidth that the hardware can measure.

[^2]: Most of the HackRF One limitations can be found in the [FAQ](https://hackrf.readthedocs.io/en/latest/faq.html). The Hardware Baseband Filter's limits are a little more hidden; you'll see them on the [block diagram](https://hackrf.readthedocs.io/en/latest/_images/block-diagram.png).
