<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 08: 140-GNU-Radio-Digital-Jammer.md
2022 Aug 30: 240-GNU-Radio-Digital-Jammer.md
2023 May 22: 021_Digital_Jammer.md
</pre>
</details>

# Digital Jammer

ℹ️ This material coincides with material from SDR slideshow F (all slides).

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
- Default Value: Choose a value between your start and stop values
- Start: `88e6`
- Stop: `108e6`
- Step: `10e3`

### For the Constellation Object:

- ID: `myconstell`
- Constellation Type: `BPSK`. _Also, try these: `QPSK`, `8PSK`, `DQPSK`, `16QAM`_
- Leave all other attributes as defaults.

### For the Random Source:

- Output Type: `Byte`
- Leave all other attributes as defaults.

### For the Constellation Modulator:

- Constellation: `myconstell`
- Leave all other attributes as defaults.

### For the Osmocom Sink:

- Device Arguments: `"hackrf=0"`
- Ch0: Frequency (Hz): `center_freq_slider`
- Ch0: Frequency Correction (ppm): `0`
- Ch0: RF Gain (dB): `0`
- Ch0: IF Gain (dB): `32`
- Ch0: BB Gain (dB): `0`

### For the Waterfall Sink:

- Center Frequency (Hz): `center_freq_slider`

## Discussion:

- Generally speaking, a jammer that matches the modulation scheme of the target is more effective than a simple noise jammer.
  - For example, if someone were to use this Digital Jammer to jam an FM radio station, it would probably be negligibly different from a noise jammer.
  - But if someone were transmitting data using BPSK (which is a modulation technique that is used in cell phones, for example), then a BPSK jammer _with matching parameters_ would be able to jam more effectively and/or with less power than a simple noise jammer.
    - What parameters must match? Perhaps the most important would be the number of symbols sent every second. The goal of a digital jammer is to closely imitate a real transmission, so that the receiver has trouble distinguishing the real data from the fake random data that the jammer is sending.

## Exercise:

- Sender: Whistle short pulses and long pulses to represent zeros and ones. Let's say a short pulse is a zero, and a long pulse is a one.
- Receiver: Announce what you're receiving.
- Rest of class: Make a "psshhhhh" noise. That's noise jamming of a broad range of frequencies.
- Now, rest of class, whistle on same pitch (frequency), with very short pulse-lengths. That's a type of noise jamming called spot jamming -- all of your energy is focused on the target frequency.
- Finally, rest of class, whistle on the same frequency, but this time, whistle a random sequence of fake data using the same pulse lengths that the sender is using. That's digital jamming. Notice that whistle pulses that are similar in length to the sender's are more effective than pulses that merely match pitch (and not pulse duration).

### See also...

- https://itecnotes.com/electrical/electrical-question-about-digital-modulation/
