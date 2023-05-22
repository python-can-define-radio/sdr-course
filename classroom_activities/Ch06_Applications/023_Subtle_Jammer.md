<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 160-GNU-Radio-FM-Subtle-Jammer.md
2022 Aug 30: 260-GNU-Radio-FM-Subtle-Jammer.md
2023 May 22: 023_Subtle_Jammer.md
</pre>
</details>

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
- Start: `88e6`
- Stop: `108e6`
- Step: `10e3`

### For the Constant Source:

- Output Type: `Complex`
- Constant: `1`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `2e6`

### For the Osmocom Sink:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Leave all as defaults.

## Discussion

The [Wikipedia Radio Jamming article](https://en.wikipedia.org/wiki/Radio_jamming#Method) says this regarding subtle jamming: "Thanks to the FM capture effect, frequency modulated broadcasts may be jammed, unnoticed, by a simple unmodulated carrier."

It may seem strange that a "Constant Source" block is used to accomplish this. The reason this works is because behind the scenes, the Hack RF combines (using multiplication) the given signal with the specified carrier frequency. That means that the transmission that goes to the antenna is actually a pure sinusoidal wave of frequency 98.5 MHz.
