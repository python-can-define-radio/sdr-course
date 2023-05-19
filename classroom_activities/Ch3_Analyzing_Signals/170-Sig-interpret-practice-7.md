## Digital data interpretation exercise #7

```
Python Block  -->  Time Sink
              -->  Waterfall Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

```
complex output.
TODO: Two signals at two freqs. One turns on and off once per 0.3 seconds, and the other has actual data similar to practice 6. The unwanted one has about 3x the amplitude of the wanted one. Add a little noise (just a tiny bit). The two freqs should both be positive and should be far enough away to easily distinguish the waves in the time sink.
Repeat the fake one cyclicly, and the real one only once, then stop everything.

Name: Mystery Signal 7
Type: No input, output = complex

100 samples per bit

Preamble = 10101010
No cyclical repeat in vec;
Binary for "PUT THE APPLES WITH THE ORANGES.       " (with the spaces)
TODO
```

</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2000`

---

Questions:

In the waterfall sink, you'll see two signals.

1. What is the carrier frequency of the lower-frequency signal?
2. What is the carrier frequency of the higher-frequency signal?

Insert a Band Pass filter, and adjust the low cut and high cut of the filter in order to separately view each signal. One of the two signals is cycling regularly and does not appear to have much information content. The other looks more like it might be carrying some information.

3. Which of the two carrier frequencies looks like it might be carrying information -- low or high?

Adjust the Band Pass filter to just view the signal that is carrying information.

4. How many samples do you think express a single bit?
5. Given the sample rate, how many seconds of data are needed to express one bit?
6. How many seconds of data are needed to express one byte?

A collaborator suggests that this communication most likely has an 8 bit preamble.

7. How many samples long is the preamble? 
8. What block would be useful for skipping the preamble?
9. What block would be useful for removing the duplicate samples that are being used to express a single bit?
10. What block would be useful for "converting" the complex wave into a real amplitude?
11. What block(s) would be useful for slicing the data into zeros and ones? At what height should you slice it?
12. After stripping the 8-bit preamble, what is the decimal number that corresponds to the first byte?
13. What is the character that corresponds to the first byte?
14. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits (with the exception of the preamble) represents a single Unicode-encoded character.
