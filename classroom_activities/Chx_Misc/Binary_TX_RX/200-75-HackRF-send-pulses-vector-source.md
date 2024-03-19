If we want to transmit more interesting data, we can use the `Mix Sine Wave Hier Block` that we created with a Vector Source. We also use the Repeat block as discussed to make the pulses longer.

`Vec_Sine_Osmocomsink.grc`

```
GUI Range

GUI Range
                                          -->  Time Sink
Vector  -->  Repeat  -->  Mix Sine Wave   -->  Osmocom Sink 
Source                    Hier Block       
```

Parameters:

- GUI Range:
  - Id: `sigfreq`
  - Default: `70e3`
  - Start: `-300e3`
  - Stop: `300e3`
  - Step: `1e3`
- GUI Range:
  - Id: `pulse_length_in_samples`
  - Type: `int`
  - Default: `500000`
  - Start: `100`
  - Stop: `1000000`
  - Step: `100`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Repeat:
  - Type: `float`
  - Interpolation: `pulse_length_in_samples`
- Mix Sine Wave Hier Block:
  - Sample Rate: `samp_rate`
  - Frequency: `sigfreq`
- Osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

This should produce on-off pulses that are, by default, half a second second each. (Why half a second? What is controlled by the `pulse_length_in_samples` slider?)
