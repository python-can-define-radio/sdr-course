## Digital data interpretation exercise #1

```
Python Block  -->  Time Sink
              -->  Waterfall Sink
```

<details><summary>A review of how to use the Python Block: (<i>click to expand</i>)</summary>

1. Double click the Python Block that you just created.
2. Click "Open in Editor". If the computer becomes unresponsive, press Esc a few times, and go back to step 2.
3. Click "Use Default Editor".
4. Erase all of the code that is there.
5. Paste the given code.

</details>

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
Name: Mystery Signal 1
Type: No input, output = complex 64

on Off on off off repeat
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - It's up to you! I recommend adjusting the `Number of Points` and the `Line 1 Marker`.

---

Questions:

1. What is the frequency of the wave?
2. Would you describe the signal as pulsing on and off, or continuously varying in amplitude? Based on that answer, is the modulation technique most likely analog or digital?
3. How wide is a single pulse (time?)
4. How wide is a single pulse (samples?)
5. If you were to guess, what modulation scheme do you think this is? Choices: FSK, OOK, PSK


