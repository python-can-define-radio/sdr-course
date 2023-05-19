**Disclaimer**: Broadcasting without a license is illegal in many countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

# Transmitting and receiving a pure sine wave

Now that we've seen the basics of GNU Radio Companion, we're going to start using the Hack RFs.

Since the Hack RF is half-duplex, you'll need two flowgraphs to do this activity: one for transmit, and one for receive.

Coordinate with the other students in your row so that one student transmits, and the others receive. Then rotate roles.

You'lll also notice that the osmocom frequencies are unspecified. The instructor will assign frequency bands by rows:

- Row 0: `2.40e9`
- Row 1: `2.41e9`
- Row 2: `2.42e9`
- Row 3: `2.43e9`
- Row 4: `2.44e9`
- Row 5: `2.45e9`
- Row 6: `2.46e9`
- Row 7: `2.47e9`
- Row 8: `2.48e9`
- Row 9: `2.49e9`

_Practical note:_ When retracting the antenna, please push gently in the center of the antenna. Pushing at the top causes the antenna to bend.

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

_Note: the following block names are abbreviated:_
- _Time Sink: QT GUI Time Sink_
- _Waterfall Sink: QT GUI Waterfall Sink_
- _Frequency Sink: QT GUI Frequency Sink_

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
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Signal Source:
  - Frequency: `sigfreq`
  - Amplitude: `amplitu`
- osmocom Sink:
  - Ch0: Frequency (Hz): `ASK_THE_INSTRUCTOR`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `ifgain`
  - Ch0: BB Gain (dB): `0`
- Time Sink:
  - "General" Tab:
    - _No changes._
  - "Trigger" Tab:
    -  Trigger Mode: `Normal`
- Frequency Sink:
  - Y Min: `-110`


## Flowgraph #2: receiver.grc

```
osmocom Source  --->  Time Sink
                --->  Waterfall Sink
                --->  Frequency Sink
```

### Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- osmocom Source:
  - Ch0: Frequency (Hz): `ASK_THE_INSTRUCTOR`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BB Gain (dB): `32`
- Time Sink:
  - "General" Tab:
    - _No changes._
  - "Trigger" Tab:
    -  Trigger Mode: `Normal`
- Frequency Sink:
  - Y Min: `-110`


# Notes

1. You should be able to see the transmitted wave on the receiving end. If you don't, ask for assistance.
2. Adjust the transmitter's IF Gain slider to be lower if possible (to reduce the amount of unnecessary energy transmitted).
3. Play with the amplitude and frequency sliders. After about a second, you'll see the changes reflected on the receiving end.

# FAQ

- Q: Why are there two waves (blue and red)?  
  A: This is Complex data, meaning it has a Real part and an Imaginary part. We'll discuss more details later, but for now, you can ignore or turn off one of the parts.

# Exercises

1. For a frequency of `100,000 Hz`, what is the period of the wave? Calculate the period first, then verify visually.  
   _Note: The period is conventionally represented with a capital T._ 
2. For a frequency of `200,000 Hz`, what is the period of the wave? Calculate the period first, then verify visually.
3. When you change the amplitude, are the changes reflected on the transmission side, the receiving side, or both?
4. When you change the IF gain, are the changes reflected on the transmission side, the receiving side, or both?
5. What happens on the receiving end when too much power is received?  _Hint: Look up "Clipping in Signal Procesing"._ 
6. At what point do you start to see clipping?
7. Can clipping happen on the transmitter's side?  
   _Hint: Try setting the transmitter's amplitude to a number such as `5`. You may need to modify the GUI Range that adjusts amplitude._  
   _Note: Clipping on the transmitter side is only visible on the receiving side. It often appears as a waveform that is distorted, but isn't obviously clipped. If you aren't able to reproduce transmitter-side clipping, just remember that data entering your osmocom Sink will be distorted if it higher than 1 or lower than -1._
8. How could you communicate data using just these sliders?
9. Modify your receiver to have slidable IF and BB gains. Use proper start, stop, step from [the HackRF docs](https://hackrf.readthedocs.io/). 
10. _Looking ahead:_ In the Signal Source, there's an option for the Waveform. Does it matter which you pick?
11. You'll notice the receiver has a spike in the center of the received spectrum. This is called the "DC Spike" -- it is produced by the Hack RF. We often choose to tune to a frequency slightly offset from our desired frequency to avoid interference caused by this spike.
12. You may or may not see a difference between the transmitted frequency and the received frequency. This is due to variations in equipment.
