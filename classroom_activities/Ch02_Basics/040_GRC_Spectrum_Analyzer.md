<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 120-GNU-Radio-Spectrum-Analyzer.md
2022 Aug 30: 220-GNU-Radio-Spectrum-Analyzer.md
2023 May 22: 040_GRC_Spectrum_Analyzer.md
</pre>
</details>

## Summary

```
GUI Range

GUI Range


Osmocom  --->  GUI sink
Source      
```

- Have a (working) slider to pick the frequency that you're tuning in to. Working means your physical SDR changes frequency when the slider changes
- Set `samp_rate` to 20000000 (20 Million)
- Have a GUI sink connected directly from the osmocom source
- Have the center of the GUI sink set correctly (OR SET TO ZERO)
- Have the bandwidth of the GUI sink set correctly
- For the center frequency slider, set the "Stop" to 500 Million, and "Step" to 10000 


## How to set the Parameters

### For the First GUI Range:

- Id: `if_gain_slider`
- Default Value: `24`
- Start: `0`
- Stop: `40`
- Step: `8`

### For the Second GUI Range:

- Id: `center_freq_slider`
- Default Value: `107.9e6`
- Start: `40e6`
- Stop: `500e6`
- Step: `10e3`

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `20e6`

### For the GUI sink:

- FFT Size: `8192`
- Update Rate: `20`

### For the Osmocom Source:

- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `50`

## Discussion

- How big of a slice of the spectrum do you see?
- While running, in the Frequency Display tab, try raising the Average in the bottom right corner. Does it help make signals more visible?
