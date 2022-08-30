## Disclaimer

Intentionally disrupting someone's wireless connection (i.e., using a jammer) is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Summary

```
GUI Range

Constant Source  ⟶  Osmocom sink
                 ⟶  Waterfall sink
```

- Have a slidable frequency to control where you are jamming.

## How to set the Parameters

### For the GUI Range:

- Id: `center_freq_slider`
- Default Value: `98.5e6`
- Start: `89e6`
- Stop: `108e6`
- Step: `1e3`

### For the Constant Source:

- Output Type: `Complex`
- Constant: `1`

### For the `samp_rate` variable (Not pictured above):

- Value: `2e6`

### For the Osmocom Sink:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BF Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.

## Discussion

- [Wikipedia Radio Jamming article](https://en.wikipedia.org/wiki/Radio_jamming#Method) regarding Subtle Jamming: "Thanks to the FM capture effect, frequency modulated broadcasts may be jammed, unnoticed, by a simple unmodulated carrier."
