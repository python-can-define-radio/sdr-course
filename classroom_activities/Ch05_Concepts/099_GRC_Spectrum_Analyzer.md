
# GRC Spectrum Analyzer

ℹ️ This material coincides with material from SDR slideshow D (slides 1-27).  However, the slides are not necessary for building and operating this program.

Build this flow diagram in the GNU Radio Companion progam on your computer.

## Summary

```
GUI Range

GUI Range


Osmocom  --->  QT GUI sink
Source      
```

You may wish to reference these Common GNU Radio Companion [error messages](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/Common-GNURadio-error-messages.md).

## How to set the Parameters:

### For the First GUI Range:

- Id: `if_gain_slider`
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `107_900_000` #This is the same as 107.9e6
- Start: `40e6`
- Stop: `500e6`
- Step: `10e3`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `20e6`

### For the QT GUI sink:

- FFT Size: `8192`
- Center Frequency (Hz): `center_freq_slider`
- Update Rate: `20`
- Show RF Freq: `Yes`

### For the Osmocom Source:

- Device Arguments: `"hackrf=0"`
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `50`

### Now Run the program

- Press the triangular-shaped "run" button at the top of the program window, or press F6 button on your keyboard.
- A new window with a GUI operation window will appear, showing graphs and controls.
- To stop, either close the GUI operation window, or in the programming window, press the square "stop" button at the top.

### Discussion

- What are the limits of the Hack RF's IF gain?
- How big of a slice of the spectrum do you see? What part of the flowgraph defines this?
- While running, in the Frequency Display tab, try raising the Average in the bottom right corner. Does it help make signals more visible?
- What happens when various variables are either left as default or set incorrectly?
  - In particular, the instructor will demonstrate this problem using the GUI Sink's Center Frequency attribute.
