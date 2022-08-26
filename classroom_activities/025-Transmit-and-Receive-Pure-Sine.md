**Disclaimer**: Broadcasting without a license is illegal in many countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.


# The Flowgraphs:

## Flowgraph #1: transmit_pure_sine.grc

```
GUI Range

GUI Range

GUI Range


Signal Source  --->  osmocom Sink
               --->  Time Sink
               --->  Waterfall Sink
               --->  Frequency Sink
```

### Parameters:

- First GUI Range:
  - Id: `amplitu`
  - Default: `0.5`
  - Start: `0`
  - Stop: `1`
  - Step: `0.01`
- Second GUI Range:
  - Id: `sigfreq`
  - Default: `70e3`
  - Start: `10e3`
  - Stop: `200e3`
  - Step: `1e3`
- Third GUI Range:
  - Id: `ifgain`
  - Default: `20`
  - Start: `0`
  - Stop: `32`
  - Step: `1`
- Variable `samp_rate` (Not pictured above):
  - Value: `2e6`
- Signal Source:
  - Frequency: `sigfreq`
  - Amplitude: `amplitu`
- osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `ifgain`
  - Ch0: BB Gain (dB): `0`
- Time Sink:
  - "General" Tab:
    - _No changes._
  - "Trigger" Tab:
    -  Trigger Mode: `Normal`
- Waterfall Sink:
  - FFT Size: `8192`
- Frequency Sink:
  - FFT Size: `8192`
  - Y Min: `-110`


## Flowgraph #2: receiver.grc

```
osmocom Source  --->  Time Sink
                --->  Waterfall Sink
                --->  Frequency Sink
```

### Parameters:

- Variable `samp_rate` (Not pictured above):
  - Value: `2e6`
- osmocom Source:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BB Gain (dB): `32`
- Time Sink:
  - "General" Tab:
    - _No changes._
  - "Trigger" Tab:
    -  Trigger Mode: `Normal`
- Waterfall Sink:
  - FFT Size: `8192`
- Frequency Sink:
  - FFT Size: `8192`
  - Y Min: `-110`


# Directions

1. A single HackRF One is half-duplex. So, if you want to transmit and receive, you'll have to have two HackRFs. I recommend working with another student.
2. You should be able to see the transmitted wave on the receiving end. If you don't, ask for assistance.
3. Adjust the transmitter's IF Gain slider to be lower if possible (to reduce the amount of unnecessary energy transmitted).
4. Play with the amplitude and frequency sliders. After about a second, you'll see the changes reflected on the receiving end.

# FAQ

- Q: Why are there two waves (blue and red)?  
  A: This is Complex data, meaning it has a Real part and an Imaginary part. We'll discuss more details later, but for now, you can ignore or turn off one of the parts.

# Exercises

1. For a frequency of `100,000 Hz`, what is the period of the wave? Calculate the period first, then verify visually.
2. For a frequency of `200,000 Hz`, what is the period of the wave? Calculate the period first, then verify visually.
3. What happens on the receiving end when the transmission power is too high?  _Hint: Look up "Clipping in Signal Procesing"._ 
4. At what point do you start to see clipping?
5. Can clipping happen on the transmitter's side? _Hint: Try setting the transmitter's amplitude to a number such as `1.5`. You may need to modify the GUI Range that adjusts amplitude._
