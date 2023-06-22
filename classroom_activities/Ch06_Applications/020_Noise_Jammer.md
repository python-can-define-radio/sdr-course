<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 130-GNU-Radio-Noise-Jammer.md
2022 Aug 30: 230-GNU-Radio-Noise-Jammer.md
2023 May 22: 020_Noise_Jammer.md
</pre>
</details>

## Disclaimer

Intentionally disrupting someone's wireless connection (i.e., using a jammer) is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Summary

```
GUI Range

GUI Range

GUI Range


Noise Source  ⟶  Low Pass Filter  ⟶  Osmocom sink
                                  ⟶  Waterfall sink
```

- In the Low Pass Filter, the **cutoff** and **transition width** should be sliders.
- Know how to change Noise Type in Noise Source.
- Have a slidable frequency to control where you are jamming.

## How to set the Parameters

### For the First GUI Range:

- Id: `cut_freq_slider`
- Default Value: `200e3`
- Start: `100e3`
- Stop: `1e6`
- Step: `50e3`

### For the Second GUI Range:

- Id: `tr_width_slider`
- Default Value: `200e3`
- Start: `100e3`
- Stop: `1e6`
- Step: `50e3`

### For the Third GUI Range:

- Id: `center_freq_slider`
- Default Value: `98.5e6`
- Start: `88e6`
- Stop: `108e6`
- Step: `10e3`

### For the Low Pass Filter:

- Cutoff Freq: `cut_freq_slider`
- Transition Width: `tr_width_slider`

### For the Noise Source:

- Noise Type: `Uniform`
- Amplitude: `50`

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

### How do I know if it's working?

- You'll need to have a receiving device to verify that the transmission is working. In class, the easiest approach is to ask another student to open GQRX.
- You can increase the power by setting the IF Gain higher. The highest IF Gain for a Hack RF is documented [here](https://hackrf.readthedocs.io/en/latest/faq.html#what-gain-controls-are-provided-by-hackrf).

### Noise Types

- Notice that the Noise Source has multiple Noise Types. As per the [documentation](https://wiki.gnuradio.org/index.php/Noise_Source), only Uniform and Gaussian are supported. As a result, the other two Noise Types will produce nothing, and the Waterfall will, as a result, be empty.
- What's the difference between Uniform and Gaussian? Try it yourself!  
  Here's the easiest way to see the difference: `Noise Source ⟶ Time Sink`  
  (I am not an expert on the practical implications of this difference, but I believe that Gaussian is more similar to  "naturally occurring" noise.)

### Filter parameters

Briefly, the cutoff and transition width both control how wide of a band is being jammed.

For more info, see the exercise about the Band Pass Filter (at time of writing, numbered  #160).



