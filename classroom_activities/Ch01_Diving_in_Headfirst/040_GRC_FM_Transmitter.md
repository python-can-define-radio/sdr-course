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

- _NOTE: You can use a Audio Source instead if you'd like. See notes at the bottom of this page._
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

- Device Arguments: `"hackrf=0"`
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.

### Discussion

- Try different audio files, different IF Gains, and different broadcast frequencies.

### Using an Audio Source

You have two options:
1. Simply using an `Audio Source` block allows you to use a microphone as your source.
2. You can also use an `Audio Source` block with a special configuration to broadcast whatever is currently playing on your computer:
    1. Do the setup described on the [GNU Radio Wiki](https://wiki.gnuradio.org/index.php?title=ALSAPulseAudio#Monitoring_the_audio_input_of_your_system_with_PulseAudio).
    2. In your `Audio Source` block, for the Device Name, put "pulse_monitor".
