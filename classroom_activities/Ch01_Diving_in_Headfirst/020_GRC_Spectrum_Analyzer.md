<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 120-GNU-Radio-Spectrum-Analyzer.md
2022 Aug 30: 220-GNU-Radio-Spectrum-Analyzer.md
2023 May 22: 040_GRC_Spectrum_Analyzer.md
2023 Aug 18: 020_GRC_Spectrum_Analyzer.md (moved to Chapter 1)
</pre>
</details>

# GRC Spectrum Analyzer

## Summary

```
GUI Range

GUI Range


Osmocom  --->  QT GUI sink
Source      
```


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

### For the QT GUI sink:

- FFT Size: `8192`
- Center Frequency (Hz): `center_freq_slider`
- Update Rate: `20`
- Show RF Freq: `Yes`

### For the Osmocom Source:

- Device Arguments: `"hackrf=0"`
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `if_gain_slider`
- Ch0: BB Gain (dB): `50`

## Discussion

- How big of a slice of the spectrum do you see?
- While running, in the Frequency Display tab, try raising the Average in the bottom right corner. Does it help make signals more visible?