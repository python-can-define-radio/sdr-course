## Digital data interpretation exercise #6

```
Python Block  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3

Name: Mystery Signal 6
Type: No input, output = complex

Noisy wave that is either 1 ish and 5 ish in amplitude; make sure noise is small enough to not require filtering beyond the binary slice
200 samples per bit

Preamble = 10101010
No cyclical repeat in vec;
Binary for "WE LIKE BUTTER ON OUR TOAST.       " (with the spaces)
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `1000`
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
7. What block would be useful for "converting" the complex wave into a real amplitude?
8. What block(s) would be useful for slicing the data into zeros and ones? At what height should you slice it?
9. After stripping the 8-bit preamble, what is the decimal number that corresponds to the first byte?
10. What is the character that corresponds to the first byte?
11. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits (with the exception of the preamble) represents a single Unicode-encoded character.
