<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Aug 18: 040_GRC_FM_Transmitter.md
2023 May 22: 030_GNU_Radio_FM_Transmitter.md
2022 Aug 30: 250-GNU-Radio-FM-Transmitter.md
2022 Aug 08: 150-GNU-Radio-FM-Transmitter.md
</pre>
</details>

# GRC FM Transmitter

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
- Decimation: This should match the sample rate that you'll find in the properties of the wav file. If you can't find the sample rate, put `60_000` (which is 60000 Hz, or 60 kHz). The song will probably play too fast; adjust to make the song sound normal. 

### For the WBFM Transmit:

- Audio Rate: `int(samp_rate)`
- Quadrature Rate: `int(samp_rate)`

### For the Osmocom Sink:

- Device Arguments: `"hackrf=0"`
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.

### Discussion

- Try different audio files, different IF Gains, and different broadcast frequencies.
