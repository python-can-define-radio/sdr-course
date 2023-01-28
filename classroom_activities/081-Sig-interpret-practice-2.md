## Digital data interpretation exercise #2

```
Python Block  -->  Time Sink
              -->  Waterfall Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
Name: Mystery Signal 2
Type: No input, output = complex 64

do different carrier freq and symbol length from previous

on off on off on off on off
binary for Y
off off off off off off off off
off off off off off off off off
NO repeat
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - It's up to you (again)!

---

Questions:

1. What is the frequency of the wave?
2. Would you describe the signal as pulsing on and off, or continuously varying in amplitude? Based on that answer, is the modulation technique most likely analog or digital?
3. How wide is a single pulse (time?)
4. How wide is a single pulse (samples?)
5. If you were to guess, what modulation scheme do you think this is? Choices: FSK, OOK, PSK

A collaborator suggests that this communication may be the letter Y or N in Unicode. You point out that there seem to be 16 bits of information rather than 8. The collaborator says that this might be an 8-bit preamble* followed by a single Unicode character. In other words, the first 8 bits are not conveying information, they are just intended to mark the start of the message. 

Questions continued:

6. What is the bit sequence of the 8-bit preamble? (Hint: It starts with 1 0).
7. What is the bit sequence of the 8-bits of actual data?
8. Assuming a Unicode interpretation, was the data a "Y" or an "N"?


*Incidentally, Ethernet frames have a preamble that is similar to the one shown above. The Ethernet preamble is longer (approx 60 bits long, depending how you count), but the 101010... pattern at the beginning is the same.
