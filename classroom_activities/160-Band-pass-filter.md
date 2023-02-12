Often, there are signals that we want to remove from the data we're working with. The unwanted signals may be random electrical noise or radio stations that are near our station of interest, but in either case, filtering out these unwanted signals is a very useful skill.

`filter_exploration_2.grc`
```
Python Block -->  Throttle  -->  Time Sink
                            -->  Waterfall Sink
                            -->  Frequency Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

```
Name: Learning Signal for band pass
Type: No input, output = complex

complex output.
TODO: Two signals at two freqs. One turns on and off once per 2 seconds, and the other turns on and off once per 3 seconds. Similar amplitude. Add a little noise (just a tiny bit). The two freqs should both be positive and should be far enough away to easily distinguish the waves in the time sink.
Repeat cyclicly.
```

</details>

Watch what happens when you run that flowgraph. Then, insert a band pass filter in the middle (before or after the Throttle; it doesn't matter).

- Band Pass Filter parameters:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cutoff Freq: `low_cut`
  - High Cutoff Freq: `high_cut`
  - Transition Width: `samp_rate/20`

Make two GUI Ranges: one for `low_cut` and one for `high_cut`.

- `low_cut`: from `-samp_rate/2` to `0`; you pick default and step
- `high_cut`: from `0` to `samp_rate/2`; you pick default and step

Try sliding the sliders to see if you can filter one signal or the other. If you find that the sliders aren't able to reach where you want them to reach, then adjust the Start and Stop of the sliders. However, GNU Radio will behave unpredictably if you ever break the rule that `low_cut < high_cut`.

