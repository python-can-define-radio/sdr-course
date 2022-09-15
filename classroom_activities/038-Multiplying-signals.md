Together as a class:

Graph a Square wave from `0 seconds` to `2 seconds` that has these attributes:

- When the wave is high, it is `1`.
- When the wave is low, it is `0`.
- Starts low.
- One full cycle (the **period**) is `1 seconds`.
- Question: What is the frequency?

Graph a Sin wave with a frequency of `4 Hz` across the same time range.

Now, multiply them.


------------------------

After doing that on paper, implement in GNU Radio:

`square_wave_separate.grc`

```
Signal Source  -->  Time Sink

Signal Source  -->  Time Sink
```

- First Signal Source:
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Waveform: `Sine`
  - Frequency: `4`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `100`

-----------------------

Now that we've seen the separate waves, let's multiply them:

`square_multiplied.grc`
```
Signal Source  -->  Multiply  -->  Time Sink
Signal Source  -->  
```

- First Signal Source:
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Waveform: `Sine`
  - Frequency: `4`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `100`


-------------------

What should the Square Wave frequency be if you want the signal to turn on for two seconds, and off for two seconds? _Hint: Try `2` and `0.5`. Neither is the correct answer, but those may help you find the anwwer._
