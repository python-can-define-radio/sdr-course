## Transmitting the pulses

We're going to send the pulses that we created to the Hack RF. 

```
Signal Source  -->  Mix Sine Wave Hier Block  -->  Time Sink 
                                              -->  Osmocom Sink
```

<details><summary> ℹ️ <i>Why no Throttle?</i> </summary>

> ```
> You should usually use a Throttle if you're doing a pure simulation (as we were doing before),
> but you usually don't use a Throttle if you are working with audio hardware or SDR hardware (as we are doing now).  
> 
> When working with hardware, the hardware provides the needed throttling to avoid maxing out the CPU.   
> 
> When doing a pure simulation, GNU radio will run the blocks as quickly as possible unless
> it is told to slow down (hence the need for a Throttle).
> ```

</details>

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Mix Sine Wave Hier Block:
  - Sample Rate: `samp_rate`
  - Frequency: `100e3`
- Osmocom Sink:
  - Ch0: Frequency (Hz): `2.4e9`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `35`
  - Ch0: BB Gain (dB): `0`

<details><summary> ℹ️ <i>Why `100e3`?</i> </summary>
  To answer this question, try different numbers between `0` and `900e3`. You'll see that small frequencies are difficult to distinguish from the DC spike. Ask an instructor if this isn't clear.
</details>

## Receiving the pulses

To ensure that this indeed transmits pulses, let's receive the signal. For example, you can use the flowgraph `receiver.grc` from an earlier exercise. Remember that the Hack RF is half-duplex, so you'll need a separate Hack RF (or some other device) to receive the signal.

Once you've confirmed that you see pulsing, and that it's you (not someone else) transmitting, move to the next exercise.

Note: The received frequency may vary slightly from the transmitted frequency. We'll discuss this later; stay tuned!
