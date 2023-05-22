<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 020_GNU_Radio_FM_Receiver.md
2022 Aug 30: 210-GNU-Radio-FM-Receiver.md
2022 Aug 08: 110-GNU-Radio-FM-Receiver.md
</pre>
</details>

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
- Option 0: `100.3e6`  (_Replace these with actual stations_)
- Label 0: `Popular country rock jazz`  
- Option 1: `99.7e6`
- Label 1: `Baroque heavy metal`
- Option 2: `99.9e6`
- Label 2: `Noisy noise`
- Option 3: `88.7e6`
- Label 3: `Some other creative station name`


### For the First GUI Range:

- Id: `if_gain_slider`
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `favorite_stations`
- Start: `88e6`
- Stop: `108e6`
- Step: `20e3`

### For the GUI Check Box:

- Id: `filteron`
- Default Value: `0`
- True: `1`
- False: `0`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `8e6`

### For the Osmocom Source:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `50`
- Ch0: Bandwidth (Hz): `filteron * 2.75e6`

### For the Band Pass Filter:

- FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
- Low Cutoff Freq: `-100e3` (notice the negative)
- High Cutoff Freq: `100e3`
- Transition Width: `90e3`

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

- If you have any errors, remember to look at the list of Common GNU Radio Error messages in the `resources` folder.

- You'll notice that sometimes you need to move the antenna to ensure good reception. Watching the Waterfall can help with seeing how good your reception is.

- In our experience, the osmocom Source's Bandwidth parameter only works if you set it during runtime. Ask if you'd like to know details.

## Questions

- Why did we pick the given `Start` and `Stop` for the `center_freq_slider`? Does this range include all Commercial FM stations in the United States? If not, how should you adjust it to include any missing frequencies?
