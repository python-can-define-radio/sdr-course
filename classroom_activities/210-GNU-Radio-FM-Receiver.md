## Summary

```
GUI Chooser

GUI Range

GUI Range

                ┌─⟶  Time sink
                ├─⟶  Waterfall sink    ┌─⟶  Waterfall sink                                             
Osmocom Source ─┴─⟶  Band Pass Filter ─┴─⟶  WBFM Receive  ⟶  Rational Resampler  ⟶  Audio Sink                          
                                     

```

- Have a (working) slider to pick the frequency that you're tuning in to. Working means your physical SDR changes frequency when the slider changes
- Demodulate the sound and play it
- Have two (2) waterfall sinks: one before the Band Pass Filter, and one after
- Have the centers of the waterfall sinks set correctly (OR SET TO ZERO)
- Working IF Gain slider (moving the slider changes the IF Gain)
- Working GUI Chooser to pick a station from a list


## How to set the Parameters

### For the GUI Chooser:

- Id: `favorite_stations`
- Type: `Float`
- Num Options: `4`
- Option 0: `100.3e6`
- Label 0: `First radio station (may be real)`
- Option 1: `99.7e6`
- Label 1: `Second radio station (may be real)`
- Option 2: (Leave this unchanged till you get the rest of the radio working, then fill it in after you've located some stations.)
- Label 2: (Same)
- Option 3: (Same)
- Label 3: (Same)


### For the First GUI Range:

- Id: `if_gain_slider`
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `favorite_stations`
- Start: `89e6`
- Stop: `108e6`
- Step: `20e3`

### For the `samp_rate` variable (Not pictured above):

- Value: `8e6`

### For the Osmocom Source:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `32`

### For the Band Pass Filter:

- FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
- Low Cutoff Freq: `-100e3` (notice the negative)
- High Cutoff Freq: `100e3`
- Transition Width: `100e3`

### For the WBFM Receive:

- Quadrature Rate: `samp_rate`
- Audio Decimation: `1`

### For the Rational Resampler:

- Type: `Float -> Float (Real Taps)`
- Interpolation: `int(48e3)`
- Decimation: `int(samp_rate)`

### For the Audio Sink:

- Sample Rate: `48 kHz` (Pick from drop-down menu)

### For BOTH Waterfall Sinks:

- Leave all as defaults.

### For the Time Sink:

- Leave all as defaults.


## Discussion

- You'll notice that sometimes you need to move the antenna to ensure good reception. Watching the Waterfall can help with seeing how good your reception is.

