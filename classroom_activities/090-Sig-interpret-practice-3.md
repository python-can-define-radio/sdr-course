## Digital data interpretation exercise #3

```
Python Block  -->  UChar to Float  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3

Something involving Packing bits and writing to a file sink

Name: Mystery Signal 3
Type: No input, output = byte

Without repeat: Binary for "ELEPHANTS ARE APPROACHING.       " (with the spaces)
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `10`
- Time Sink:
  - It's up to you (again)! I recommend turning on the markers for the points.

---

Questions:

1. Does it appear that each sample corresponds to one bit or one byte?
2. Given the sample rate, how many seconds of data are needed to express one bit?
3. How many seconds of data are needed to express one byte?
4. What is the decimal number that corresponds to the first byte?
5. What is the character that corresponds to the first byte?
6. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits represents a single Unicode-encoded character.
