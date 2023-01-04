_This is unfinished, but has some useful info._

## Transmitting to the Hack RF

One way to transmit this is using the `Mix Sine Wave Hier Block` that we created. You'll use what you created in `041`, but with the Vector Source and Repeat block instead of a Signal Source. Try it first, and then if needed, refer to the directions below.

`Vec_Sine_Osmocomsink.grc`

```
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
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Repeat:
  - Type: `float`
  - Interpolation: `int(2e6)`
- Mix Sine Wave Hier Block:
  - Sample Rate: `samp_rate`
  - Frequency: `sigfreq`
- Osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

This should produce on-off pulses that are 1 second each. (Why 1 second? Try changing the Interpolation on the Repeat block.)

_Note: The GUI Range is not strictly necessary, but is useful in a classroom setting for easily changing frequencies._