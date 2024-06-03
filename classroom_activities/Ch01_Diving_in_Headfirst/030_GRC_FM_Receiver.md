<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Aug 18: 030_GRC_FM_Receiver.md
2023 Aug 18: 030_GNU_Radio_FM_Receiver.md
2023 May 22: 020_GNU_Radio_FM_Receiver.md
2022 Aug 30: 210-GNU-Radio-FM-Receiver.md
2022 Aug 08: 110-GNU-Radio-FM-Receiver.md
</pre>
</details>

# GRC FM Receiver

ℹ️ This material coincides with material from SDR slideshow C (slides 1-44).  However, the slides are not necessary for building and operating this program.

Build this flow diagram in the GNU Radio Companion progam on your computer. (This instruction may not be repeated in subsequent lessons.)

## Summary

```
GUI Chooser

GUI Range

GUI Range

GUI Check Box

                ┌─⟶  Time sink
                ├─⟶  Waterfall sink    ┌─⟶  Waterfall sink                                             
Osmocom Source ─┴─⟶  Band Pass Filter ─┴─⟶  WBFM Receive  ⟶  Rational Resampler  ⟶  Audio Sink                          
                                     

```

You may wish to reference these Common GNU Radio Companion [error messages](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/Common-GNURadio-error-messages.md).

## How to set the Parameters

### For the GUI Chooser:

- Id: `favorite_stations`
- Type: `Float`
- Num Options: `4`
- Default Option: `104_300_000`  (_This only applies if your version of GRC has a `Default Option` separated from `Option 0`._)
- Option 0: `104_300_000`  (_Replace these with actual stations_)
- Label 0: `Popular country rock jazz`  
- Option 1: `93_900_000`
- Label 1: `Baroque heavy metal`
- Option 2: `100_900_000`
- Label 2: `Noisy noise`
- Option 3: `105_700_000`
- Label 3: `Some other creative station name`


### For the First GUI Range:

- Id: `if_gain_slider`<sup>[ footnote](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_GRC_FM_Receiver.md#footnotes)</sup>
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `favorite_stations`
- Start: `88_000_000`
- Stop: `108_0009_000`
- Step: `10_000`

### For the GUI Check Box:

- Id: `hardware_filter`
- Default Value: `False`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `8_000_000`

### For the Osmocom Source:

- Device Arguments: `"hackrf=0"`<sup>[ footnote](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_GRC_FM_Receiver.md#footnotes)</sup>
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `50`
- Ch0: Bandwidth (Hz): `hardware_filter * 2_750_000`

### For the Band Pass Filter:

- FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
- Low Cutoff Freq: `-100_000` (notice the negative)
- High Cutoff Freq: `100_000`
- Transition Width: `90_000`

### For the WBFM Receive:

- Quadrature Rate: `samp_rate`
- Audio Decimation: `1`

### For the Rational Resampler:

- Type: `Float -> Float (Real Taps)`
- Interpolation: `48_000`
- Decimation: `int(samp_rate)`

### For the Audio Sink:

- Sample Rate: `48 kHz` (Pick from drop-down menu)

### First Waterfall Sink (directly connected from the osmocom Source):

- Name: `"Original spectrum"`

### Second Waterfall Sink (after the band pass filter):

- Name: `"Filtered: a 200 kHz band in the center of the received spectrum"`
- Center Frequency (Hz): `center_freq_slider`

### For the Time Sink:

- Leave all as defaults.

### Now Run the program:

- Press the triangular-shaped "run" button at the top of the program window, or press the F6 button on your keyboard.
- A new window with a GUI operation window will appear, showing graphs and controls.
- To stop, either close the GUI operation window, or in the programming window, press the square "stop" button at the top, or press F7 on your keyboard.

### Discussion

- If you have any errors, remember to look at the list of Common GNU Radio Error messages in the [resources](https://github.com/python-can-define-radio/sdr-course/tree/main/resources) folder.

- You'll notice that sometimes you need to move the antenna to ensure good reception. Watching the Waterfall can help with seeing how good your reception is.

- In our experience, the osmocom Source's Bandwidth parameter only works if you set it during runtime. Ask if you'd like to know details.

- The purpose of the `hardware_filter` is to avoid aliasing. For more info, see [this lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/034_Oversampling_Undersampling.md).

### Questions

- Why did we pick the given `Start` and `Stop` for the `center_freq_slider`?
- Does this range include all Commercial FM stations in the United States?
- If not, how should you adjust it to include any missing frequencies?

### Footnotes
1. `hackrf=0` explanation
    - Normally index zero is assigned to the first HackRF plugged in. If you have multiple HackRFs, they will be numbered sequentially (0, 1, 2, 3, etc).
2. IF Gain slider
    - Notice when you adjust the IF Gain slider, the intensity changes. (In the frequency sink, this is seen as a Y-axis increase. In the waterfall sink, this is seen as a color change).
    - Check out the [HackRF One FAQ](https://hackrf.readthedocs.io/en/latest/faq.html) to find out the Intermediate Frequency (IF), Radio Frequency (RF), and Baseband (BB) gain capabilities of the HackRF One. You'll most likely want to do Ctrl + f search for "gain" on that page.

### Optional exercise

- Student activity, groups of 5:
    - Draw pictures to show what each of these blocks is doing:
        - Band pass filter
        - WBFM Receive
        - Rational Resampler
    - Give textual descriptions of what every other block does.
- Discuss activity as a class
