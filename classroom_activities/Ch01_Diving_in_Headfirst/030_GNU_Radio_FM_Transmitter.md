<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 030_GNU_Radio_FM_Transmitter.md
2022 Aug 30: 250-GNU-Radio-FM-Transmitter.md
2022 Aug 08: 150-GNU-Radio-FM-Transmitter.md
</pre>
</details>

## Disclaimer

Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Summary

```
GUI Range

Wav File Source  ⟶  Rational Resampler  ⟶  WBFM Transmit  ⟶  Osmocom sink
                                                          ⟶  Waterfall sink
```

- Have a (working) slider to pick the frequency that you're tuning in to. Working means the HackRF changes frequency when the slider changes
- Modulate the sound and transmit it


## How to set the Parameters

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `2e6`

### For the GUI Range:

- Id: `center_freq_slider`
- Default Value: `98.5e6`
- Start: `88e6`
- Stop: `108e6`
- Step: `10e3`

### For the Wav File Source:

- File: Pick a file by pressing the "..." button. It must be a wav file, not an mp3, etc.
- Repeat: Up to you; do you want it to repeat?

### For the Rational Resampler:

- Type: `Float -> Float (Real Taps)`
- Interpolation: `int(samp_rate)`
- Decimation: Check the sample rate in the properties of the wav file. If you can't find the sample rate, put `int(20e3)`. The song will play either too fast or too slowly; adjust up or down to make the song sound normal.  
  Good Example: `21000`  
  Bad Example: `21000 Hz`  (don't put the "Hz" part)

### For the WBFM Transmit:

- Audio Rate: `int(samp_rate)`
- Quadrature Rate: `int(samp_rate)`

### For the Osmocom Sink:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.

## Discussion

- Try different audio files, different IF Gains, and different broadcast frequencies.
