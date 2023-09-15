**Disclaimer**: Broadcasting without a license is illegal in many countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

# Transmitting and receiving a pure sine wave

Since the Hack RF is half-duplex, you'll need two flowgraphs to do this activity: one for transmit, and one for receive.

The Instructor will assign work groups. Coordinate within your assigned group so that one student transmits, and the other receives. Then rotate roles.

You'll also notice that the osmocom frequencies are unspecified. Use the frequency band assigned to your group:

- Group 0: `2.40e9`
- Group 1: `2.41e9`
- Group 2: `2.42e9`
- Group 3: `2.43e9`
- Group 4: `2.44e9`
- Group 5: `2.45e9`
- Group 6: `2.46e9`
- Group 7: `2.47e9`
- Group 8: `2.48e9`
- Group 9: `2.49e9`

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
  - Ch0: Frequency (Hz): `Use frequency from group # above`
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
  - Ch0: Frequency (Hz): `Use frequency from group # above`
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


### Notes

1. You should be able to see the transmitted wave on the receiving end. If you don't, ask for assistance.
2. Adjust the transmitter's IF Gain slider to be lower if possible (to reduce the amount of unnecessary energy transmitted).
3. Play with the amplitude and frequency sliders. After about a second, you'll see the changes reflected on the receiving end.
4. You may or may not see a difference between the transmitted frequency and the received frequency. This is due to variations in equipment.

### FAQ

- Q: Why are there two waves (blue and red)?  
  A: This is Complex data, meaning it has a Real part and an Imaginary part. We'll discuss more details later, but for now, you can ignore or turn off one of the parts.

### Questions

1. Adjust the `sigfreq` slider to `100,000 Hz`. What is the period of the wave? Calculate the period first, then verify visually.  
   _**Note:** The period is conventionally represented with a capital T._ 
2. For a frequency of `200,000 Hz`, what is the period of the wave? Calculate the period first, then verify visually.
3. When you change the `amplitu` slider, are the changes reflected on the transmission side, the receiving side, or both?
4. When you change the `ifgain` slider, are the changes reflected on the transmission side, the receiving side, or both?
5. What happens on the receiving end when too much power is received?   
6. At what point do you start to see clipping?
7. Can clipping happen on the transmitter's side?  
   _**Hint:** Try setting the transmitter's amplitude to a number such as `5`. You may need to modify the GUI Range that adjusts amplitude._   
8. How could you communicate data using just these sliders?

<details><summary>Click for answers.</summary>

1. 0.00001 seconds or .01 milliseconds or 10 microseconds.  
  
2. 0.000005 s, .005 ms, or 5 μs.

3. Both.

4. Receive only, because the IF gain amplification happens inside the HackRF right before it is transmitted.

5. The signal clips. For more info, look up "Clipping in Signal Processing".

6. At 1 and -1

7. Clipping on the transmitter side is only visible on the receiving side. It often appears as a waveform that is distorted, but isn't obviously clipped.
   
8. Basic OOK (On-Off Keying), ASK (Amplitude shift keying), or FSK (Frequency shift keying)

</details>

### Exercises  
  
1. Modify your receiver to have slidable IF and BB gains. Use proper start, stop, step from [the HackRF docs](https://hackrf.readthedocs.io/).
2. In the Signal Source, there's an option for the Waveform. Experiment with the different waveforms.  
3. You'll notice the receiver has a spike in the center of the received spectrum. This is called the "DC Spike" -- it is produced by the Hack RF. We often choose to tune to a frequency slightly offset from our desired frequency to avoid interference caused by this spike.  

