_Prerequisite: `038-Multiplying-signals.md`_

We want to be able to transmit the generated on-off signal to the Hack RF.

To do so, we need to adjust the sample rate, because the Hack RF requires at least 2 million samples per second.

We also adjust the number of points displayed in the time sink so that we can still see what is happening. (The default value of `1024` points would show a relatively small chunk of time, since `2000000` points is a single second.)

Note: The sine wave's frequency is arbitrary. Feel free to adjust it.

----------------------------------

Make a new file: `square_multiplied_2.grc`
```
Signal Source  -->  Multiply  -->  Time Sink
Signal Source  -->  
```

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `20`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Number of Points: `int(samp_rate)*4`

Note: When you run this file, it will take about 4 seconds before displaying any data.

----------------------------------

We can't transmit to the osmocom sink unless the data type is blue (complex).

So, copy the previous flowgraph into a new file called `square_multiplied_complex.grc`

```
Signal Source --> Float to Complex -->  Multiply  -->  Time Sink
                    Signal Source  -->
    
```

_Note:_ The Square Signal source should be attached to the `re` port on the Float to Complex block.

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `complex`  (**different**)
  - Waveform: `Sine`
  - Frequency: `20`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Number of Points: `int(samp_rate)*4`
