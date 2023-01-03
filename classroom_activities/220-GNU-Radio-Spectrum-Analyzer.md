## Summary

```
GUI Range

GUI Range


            ---->  GUI sink    
            |
Osmocom  ---|
Source      |
            ---->  Band Pass   ⟶  WBFM      ⟶  Rational   ⟶  Audio 
                   Filter         Receive      Resampler     Sink
                   (Optional)     (Optional)   (Optional)    (Optional)          

```

- Have a (working) slider to pick the frequency that you're tuning in to. Working means your physical SDR changes frequency when the slider changes
- Set `samp_rate` to 10000000 (10 Million)
- Have a GUI sink connected directly from the osmocom source
- Have the center of the GUI sink set correctly (OR SET TO ZERO)
- Have the bandwidth of the GUI sink set correctly
- For the center frequency slider, set the "Stop" to 500 Million, and "Step" to 10000 
- (Optional) Demodulate the sound and play it (i.e., demodulate the center of the spectrum that you're viewing, just like in the FM Radio)


## How to set the Parameters

### For the First GUI Range:

- Id: `if_gain_slider`
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `107.9e6`
- Start: `89e6`
- Stop: `500e6`
- Step: `10e3`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `10e6`

### For the GUI sink:

- FFT Size: `8192`
- Update Rate: `20`

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
- Transition Width: `50e3`

### For the WBFM Receive:

- Quadrature Rate: `samp_rate`
- Audio Decimation: `1`

### For the Rational Resampler:

- Type: `Float -> Float (Real Taps)`
- Interpolation: `int(48e3)`
- Decimation: `int(samp_rate)`

### For the Audio Sink:

- Sample Rate: `48 kHz` (Pick from drop-down menu)


## Discussion

- How big of a slice of the spectrum do you see?
- What does the FFT Size do?
