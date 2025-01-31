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
#### Name the first cell "imports". Put this code:
import marimo as mo
from paragradio.v2025_03 import SpecAnSim

#### Name the second cell "launch". Put this code:
SpecAnSim.config(running=True)
```

If it runs, it should look like this:

![specAnSim.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specansim1.png?raw=true)  
 
For better viewing:
- in order to watch the changes as you make them, and if you do not have a secondary screen available, right click on the titlebar of the running spectrum analyzer and select ***always on top***.
- resize or move as necessary so it does not obstruct your view.

In the GNU Radio App that launched, you'll see three views of the signal: the Time Domain view, the Frequency Domain view, and a Waterfall view.

- The Time Domain shows the raw signal as it is received from the USB port. (x-axis: time; y-axis: amplitude)
- The Frequency Domain shows the amount of each frequency that is present in the slice of the spectrum that we have selected. (x-axis: frequencies; y-axis: amplitude)
- The Waterfall shows the same information as the Frequency Domain, but using colors to represent strength of signal instead of the height of the spike. It also scrolls, which provides a view of the the history of the signal. (x-axis: frequencies; y-axis: time; colors: amplitude)

```python3
## Exercise 2
## Replace the contents of the "launch" cell with the following:
SpecAnSim.config(
    running=True,
    center_freq=93.7e6,
)
```
It should now look like this:

![specAnSim.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specansim2.png?raw=true)  

What did it do? Look closely at the simspecan, then change the frequency and try again.

To improve the user experience, we can add a slider to control the frequency. This could be done using any graphics toolkit (Guizero, PyQt, PyGame, etc), but we will continue to use Marimo.

### Sliders
Now we are going to create a slider. For this example we will start by making a slider that can adjust our frequency called 'cfslider' (meaning 'Center Frequency Slider' for short).

```python3
## Exercise 3
## Create a third cell. Name it "create_ui". Put this code:
cfslider = mo.ui.slider(start=92.5e6, stop=94.5e6, step=10e3, value=93.7e6, label="Frequency")

## Create a fourth cell. Name it "render_ui". Put this code:
mo.md(f"""{cfslider} {cfslider.value} Hz""")
```
Let's pause here to discuss what all of the elements of this slider mean:
 - **Start:** This is the lowest value or left most limit of the slider.
 - **Stop:** This is the highest value or right most limit of the slider.
 - **Step:** This is how much the value will adjust between each 'step' on the slider as the user drags it between the start and stop values.
   - In the above code, the value of step is 10e3, or 10 thousand. As the user drags the slider, the value will increase or decrease by 10e3 increments.
 - **Value:** This is the default value the slider will be on when the program is launched. 
   - In the example slider above this would be 93.7 Million. This is where the slider will start, but may be adjusted down to 92.5 Million or up to 94.5 Million.
 - **Label:** This is the label or title that will appear next to the slider.

Notice how our 'Value' in the slider is the same as we set our frequency to in Exercise 2. The difference is we can now adjust the value of our frequency slider between multiple values by dragging the slider, however, the frequency value in the GNU Radio app is not changing.

Let's make it actually adjust our frequency:

```python3
## Exercise 4
## In the "launch" cell; replace the following to use the slider value:

# REPLACE:
center_freq=93.7e6

# WITH:
center_freq=cfslider.value

```

Adjust the slider, and you should see the view of the spectrum adjust accordingly.

### Features

There are a couple of nifty features we'll highlight here. 

- You will notice a timestamp above the "launch" cell. The timestamp shows the last time that a parameter change was sent to the GNU Radio App (for example, last time the `center_freq` was changed). This can help with troubleshooting because if the timestamp is not changing at all, then you know that your sliders are having no impact on the GNU Radio App.
- If you adjust a slider, but have closed your GNU Radio App, it will automatically re-launch.
   - This is what the "config" code is for -- updating the existing app or launching the app if it isn't running.
     
#### Improving the display of the chosen frequency

You can show the frequency in a more pleasant way like so:

```python3
## Exercise 5
## Replace the code in the "render_ui" cell with the following
mo.md(f"""{cfslider} {cfslider.value} Hz = {cfslider.value/1e6} MHz""")
```

Complete the following exercise:

```python3
## Exercise 6
## Change the "render_ui" cell to display the value in kHz and in GHz.
```

```python3
## Exercise 7
## Create a switch.
## Display the current True/False value of the switch.
## Change the SpecAnSim.config so that the switch controls whether it is running.
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

Now we are going to make a real spectrum analyzer since the previous one was just a simulation.

Start by ensuring your HackRF One is plugged into the proper computer.

Create a new Marimo notebook and save it as **specan.py**.
- If you don't see the "Create a new notebook" option, exit your current notebook by clicking the three lines in the top right of your screen and selecting Return home.

```python3
## Exercise 8
## Try this.
#### Name the first cell "imports". Put this code:
import marimo as mo
from paragradio.v2025_03 import SpecAn

## Initially let's hardcode our frequency instead of using a ui element value.
#### Name the second cell "launch". Put this code:
SpecAn.config(
    running=True,
    center_freq=2.4369e9,
)
```
**Notice:** In the "imports" cell, we are importing 'SpecAn' from Paragradio now instead of the "SpecAnSim" that was in the previous exercises.

You should see something very similar to the simulated spectrum analyzer. The difference is that these frequencies are being measured from the universe around you!  
If it doesn't work, ensure you have plugged in your HackRF One.  
The spectrum will vary depending on what activity (if any) is present on those frequencies in your area.

#### Checkpoint Activity

The instructor will ensure that everyone has working hardware by doing the following activity. _If you are doing this lesson without instructor guidance, have a partner [create a transmitter](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md#transmission-code)._
  
1. The instructor or your partner will transmit a narrow signal on 2.437 GHz that toggles on and off every few seconds.
2. Students will look at the waterfall sink or the frequency sink to see the spike of activity appearing and disappearing.

Notice that you (the student) tuned to a frequency that was slightly offset from the transmitted frequency (2.4369 GHz rather than 2.437 GHz). This is because the Hack RF (and most SDR devices that aren't terribly expensive) have a "DC Spike" on the center frequency of the received spectrum. We tune off-center so that this spike doesn't obscure or distort the frequency of interest.

Review: Why do you think we chose 2.437 GHz? [Hint](https://hackrf.readthedocs.io/en/latest/faq.html#what-is-the-transmit-power-of-hackrf).

#### Using the help function

We've seen that the spectrum analyzer's `center_freq` is settable. Here's how to see the other settable parameters:

```python3
## Exercise 9
## import cell:
import marimo as mo
from paragradio.v2025_03 import SpecAn
## in a second cell:
mo.md(SpecAn.config.__doc__)
```

This will print the documentation string (docstring) for the `config` function and it should look something like this:

![docstring.png](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/assets/specanhelp1.png?raw=true) 

The instructor can demonstrate the usage of each parameter upon request.

#### More exercises

```
## Exercise 10
## In the "create_ui" cell, add a slider element that controls the center frequency.
## Set the left limit to 400e6 and right limit to 600e6.
## Render the element in the "render_ui" cell.
## Hint: It should look like this:
##    mo.md(f"""{replace_this_part_with_the_name_of_the_slider}""")


## Exercise 11
## In the "create_ui" cell, add a switch element that controls whether the SpecAn is running.
## Render the element in the "render_ui" cell.
## Hint: it should be inside the quotes of the mo.md() that you added in Exercise 10.


## Exercise 12
## In the "create_ui" cell, add a slider that controls the samp_rate.
## The limits should match the Hack RF's limitations.
## Render the element in the "render_ui" cell.

```

#### What to expect on the assessment

For the graded assignment...
- You'll have access to this lesson, your own notes, and the Hack RF Docs. You will not be allowed to use any other resources.
- You'll be expected to know how to use the metric prefixes kilo, Mega, and Giga. For example, if the assignment says "Tune to 350 MHz", you'll need to be able to convert that to `350e6 Hz` or `0.35 GHz`. As a reminder, you will not be allowed to use online converter tools.
- You'll be expected to know the name and meaning of each of the parameters that is settable in `config()` (such as `if_gain`), ***including those which are not mentioned in the lesson above***.
- You'll be asked to create Marimo UI elements that control specific parameters, similar to the `cfslider` above.
  - The Marimo UI elements will be limited to any that you've seen in this lesson or any previous lessons.
- You'll be expected to know the Hack RF's limitations for each settable parameter in order to adjust the associated settings in the UI elements. For example, Marimo sliders have a `step` parameter, and the HackRF One requires a Rx IF Gain step value of 8.[^2]
- If you'd like to practice, try creating Marimo UI elements to control each parameter, and ask an instructor to check your work.

#### Transmission code:

The following code is one way to create a transmission for testing that your Hack RF is able to receive signals.

```python3
from paragradio.v2025_03 import Noise_Tx
import time

def ntxconfig(ampli, ifg):
    Noise_Tx.config(
        center_freq=2.437e9,
        filter_cutoff_freq=50e3,
        filter_transition_width=50e3,
        amplitude=ampli,
        if_gain=ifg,
    )

while True:
    ntxconfig(100, 47)
    time.sleep(2)
    ntxconfig(0, 0)
    time.sleep(2)
```

[^1]: The Sample rate limits the instantaneous bandwidth that the hardware can measure.

[^2]: Most of the HackRF One limitations can be found in the [FAQ](https://hackrf.readthedocs.io/en/latest/faq.html). The Hardware Baseband Filter's limits are a little more hidden; you'll see them on the [block diagram](https://hackrf.readthedocs.io/en/latest/_images/block-diagram.png).
