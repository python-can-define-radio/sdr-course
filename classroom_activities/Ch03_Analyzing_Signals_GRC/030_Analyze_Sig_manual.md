<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Feb 22: 070-Sig-interpret-bits-manual.md
2023 May 22: 030_Analyze_Sig_manual.md
</pre>
</details>

## Signal interpretation: manually decoding a sequence of bits

Filename: `Sig_interp_bits_manual.grc`

```
Python Block  -->  UChar to Float  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
import numpy as np
from gnuradio import gr



name = "Mystery Signal: small bit sequence"
out_sig_port_0 = np.uint8


class blk(gr.basic_block):

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[],
            out_sig=[out_sig_port_0]
        )
        
        self.state_content = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
        self.current_idx = 0
        

    def general_work(self, input_items, output_items):
        if self.current_idx >= len(self.state_content):
            return 0

        output_items[0][0] = self.state_content[self.current_idx]
        self.current_idx += 1
        return 1
  
```
</details>

Parameters:
- Time Sink:
  - Type: _Decide based on the color of the ports._
  - Number of Points: _Strangely, you should set this to `23`, run the program, then set it to `24`, and run the program again._
  - I recommend turning on the markers for the points.

---

Questions:

1. Would you say each sample represents one bit or one byte?
2. How many bits are in a byte?
3. How many bytes long is the messsage?
4. Assuming that each byte is a Unicode (or ASCII) character, what is the message? Note: You may find the following python code helpful.

```python3
x = 0b01010010
print("Python will now display this number in decimal:")
print(x)
print("Python can also convert it back to a character")
print(chr(x))
```
