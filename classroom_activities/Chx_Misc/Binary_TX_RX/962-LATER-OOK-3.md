Convert your transmit and receive simulation to use osmocom source and sink.

Ensure your osmocom Source has adjustable IF and BB gains.

## Transmitter 

`Transmit_binary_data_osmocom.grc`

```
                               --> Waterfall Sink
                               |
Vector Source  --->  OOK Mod  -->  osmocom Sink
                |              |
                --> Time       --> Time
                    Sink           Sink
                    (First)        (Second)
```

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Time Sink (First):
  - Name: `"Original Data"`
  - Sample Rate: `1`
  - Number of Points: `20`
- OOK Mod:
  - Frequency: `70e3`
  - Sample Rate: `samp_rate`
  - Symbol Length: `int(1e6)`
- Time Sink (Second):
  - Name: `"Wavey Data"`
- osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

## Receiver

`Receive_binary_data_osmocom.grc`

```
                 --> Waterfall Sink
                 |
osmocom Source  --->  OOK Demod  ------
                 |                    |
                 -->  Time Sink       --->  UChar to  --> Time Sink 
                      (First)               Float         (Second)
```

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- osmocom Source:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BB Gain (dB): `32`
- Time Sink (First):
  - Name: `"From the osmocom"`
- OOK Demod:
  - Symbol Length: `int(1e6)`
  - Threshold: `0.2`
- Time Sink (Second):
  - Name: `"Demodulated Data"`
  - Sample Rate: `1`
  - Number of Points: `20`

You will most likely want to add GUI Ranges for the IF Gain, BB Gain, and Threshold. Threshold should be between 0 and 1.
