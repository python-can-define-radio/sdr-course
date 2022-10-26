## Sending more interesting data

We've seen how to create a square wave using the Vector Source. Now, let's send a more interesting signal.

Create this flowgraph. Name it `repeat_demo_3.grc`.

```
Vector Source  -->  Repeat  -->  Time Sink
```

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `10`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Repeat:
  - Type: `float`
  - Interpolation: `5`
- Time Sink:
  - General tab:
    - Type: `float`
    - Number of Points: `100`
    - Y min: `-2`
    - Y max: `2`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

## Transmitting to the Hack RF

One way to transmit this is using the `Mix Sine Wave Hier Block` that we created. You'll use what you created in `041`, but with the Vector Source and Repeat block instead of a Signal Source. Try it first, and then if needed, refer to the directions below.

```
                                          -->  Time Sink
Vector  -->  Repeat  -->  Mix Sine Wave   -->  Osmocom Sink 
Source                    Hier Block       
```

Parameters:

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
  - Frequency: `100e3`
- Osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

This should produce on-off pulses that are 1 second each. (Why 1 second? Try changing the Interpolation on the Repeat block.)
