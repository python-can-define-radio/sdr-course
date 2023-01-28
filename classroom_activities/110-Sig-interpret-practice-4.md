## Digital data interpretation exercise #4

```
Python Block  -->  UChar to Float  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3

Something involving Packing bits and writing to a file sink

Name: Mystery Signal 4
Type: No input, output = byte

Preamble = 10101010
No cyclical repeat in vec;
repeat interpolation 5 on the samples
Binary for "THE EGGS ARE HATCHING.       " (with the spaces)
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `80`
- Time Sink:
  - It's up to you (again)! I recommend turning on the markers for the points.

---

Questions:

1. How many samples do you think express a single bit?
2. Given the sample rate, how many seconds of data are needed to express one bit?
3. How many seconds of data are needed to express one byte?

A collaborator suggests that this communication most likely has an 8 bit preamble.

4. How many samples long is the preamble?
5. What block would be useful for skipping the preamble?
6. What block would be useful for removing the duplicate samples that are being used to express a single bit?
7. After stripping the 8-bit preamble, what is the decimal number that corresponds to the first byte?
8. What is the character that corresponds to the first byte?
9. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits (with the exception of the preamble) represents a single Unicode-encoded character.
