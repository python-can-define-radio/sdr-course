Now that we've seen square waves and sine waves plotted on paper and in Python using Matplotlib, let's graph them in GNU Radio.

## GNU Radio: Separate waves

`square_wave_separate.grc`

```
Signal Source  -->  Time Sink

Signal Source  -->  Time Sink
```

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `4`
- Time Sink (both):
  - Type: `Float`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `100`

## GNU Radio: Multiplying

Now that we've seen the separate waves, let's multiply them:

`square_multiplied.grc`
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
  - Frequency: `4`
- Time Sink:
  - Type: `Float`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `100`

### Exercises

1. What should the Square Wave frequency be if you want the signal to turn on for two seconds, and off for two seconds? _Hint: Try `2` and `0.5`. Neither is the correct answer, but those may help you find the answer._
2. How would you make the Sine wave's frequency slideable between 2 Hz and 20 Hz?
3. Once you've set up that slider, try some other frequencies for the Sine wave to see what they look like. For example, try `10` and `20`. 
4. Try the Print block in addition to the Time Sink. Does it print what you expect? You may want to change the sample rate so that you can look at less data.