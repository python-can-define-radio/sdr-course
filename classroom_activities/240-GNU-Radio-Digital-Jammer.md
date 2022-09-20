## Disclaimer

Intentionally disrupting someone's wireless connection (i.e., using a jammer) is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Summary

```
GUI Range

Constellation object


Random source  ⟶  Constellation modulator  ⟶  Osmocom sink
                                           ⟶  Waterfall sink
```

- The constellation modulator should have a correct Constellation attribute.
- Have a slidable frequency to control where you are jamming.

## How to set the Parameters

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `2e6`

### For the GUI Range:

- Id: `center_freq_slider`
- Default Value: `98.5e6`
- Start: `89e6`
- Stop: `108e6`
- Step: `1e3`

### For the Constellation Object:

- ID: `myconstell`
- Constellation Type: Pick one of these: `BPSK`, `QPSK`, or `16QAM`.
- Leave all other attributes as defaults.

### For the Random Source:

- Output Type: `Byte`
- Leave all other attributes as defaults.

### For the Constellation Modulator:

- Constellation: `myconstell`
- Leave all other attributes as defaults.

### For the Osmocom Sink:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.


## Discussion:

- Generally speaking, a jammer that matches the modulation scheme of the target is more effective than a simple noise jammer.
  - For example, if someone were to use this Digital Jammer to jam an FM radio station, it would probably be negligibly different from a noise jammer.
  - But if someone were transmitting data using BPSK (which is a modulation technique that is used in cell phones, for example), then a BPSK jammer _with matching parameters_ would be able to jam more effectively and/or with less power than a simple noise jammer.
    - What parameters must match? Perhaps the most important would be the number of symbols sent every second. The goal of a digital jammer is to closely imitate a real transmission, so that the receiver has trouble distinguishing the real data from the fake random data that the jammer is sending.
