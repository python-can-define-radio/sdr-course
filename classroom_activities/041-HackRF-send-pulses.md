_Prerequisites: `038-Multiplying-signals.md` and `039-Multiply-signals-continued.md`_

We're going to send the pulses that we created to the Hack RF. 

```
Signal Source  -->  On Off Cycle Hier Block  -->  Time Sink 
                                             -->  Osmocom Sink
```

<details><summary>_Why no Throttle?_</summary>
<p>
  
------
  
You always use a Throttle if you're doing a pure simulation (as we were doing before), but you should never use a Throttle if you are working with audio hardware or SDR hardware (as we are doing now).

When working with hardware, the hardware provides the needed throttling to avoid maxing out the CPU. 

When doing a pure simulation, GNU radio will run the blocks as quickly as possible unless it is told to slow down.
  
------
  
</p>
</details>

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Signal Source:
  - Output Type: `complex`
  - Waveform: `Sine`
  - Frequency: `20`
- On Off Cycle Hier Block:
  - Frequency: `1`
  - Sample Rate: `samp_rate`
- Osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

Ask a classmate to receive this signal and see what it looks like.
