## Digital data interpretation exercise #5

```
Python Block  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3

Name: Mystery Signal 5
Type: No input, output = float


5  |                                 
   |                               
4  |                •         • •     
   |            • •• •      •• • •         
3  |             •                  
   |                               
2  |                               
   |      •   •       • ••••             
1  |     • •••         •                
   |                                 
0  ------------------------------------

Preamble = 10101010
No cyclical repeat in vec;
Binary for "THE TEA IS READY TO DRINK.       " (with the spaces)
TODO
```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `60`
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
7. What block(s) would be useful for slicing the data into zeros and ones? At what height should you slice it?
8. After stripping the 8-bit preamble, what is the decimal number that corresponds to the first byte?
9.  What is the character that corresponds to the first byte?
10. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits (with the exception of the preamble) represents a single Unicode-encoded character.
