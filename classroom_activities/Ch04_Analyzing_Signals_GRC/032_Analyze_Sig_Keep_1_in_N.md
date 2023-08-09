<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Oct 17: 058-OOK.md 
2023 Jan 17: 115-OOK.md 
2023 Jan 28: 110-Sig-interpret-practice-4.md
2023 May 22: 032_Analyze_Sig_Keep_1_in_N.md
</pre>
</details>

## Digital data interpretation exercise #4

```
Python Block  -->  UChar to Float  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
import numpy as np
from gnuradio import gr
from functools import reduce
from operator import concat



name = "Mystery Signal 4"
out_sig_port_0 = np.uint8



def use_func(state_container):
    idx = state_container["count"] // 5
    content = state_container["content"]
    if idx >= len(content):
        return None
    retval = content[idx]
    state_container["count"] += 1
    return retval


def unpackOne(x):
    return list(map(int, f"{x:b}".zfill(8)))


def unpackbits(x):
    return reduce(concat, map(unpackOne, x))


class blk(gr.basic_block):

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[],
            out_sig=[out_sig_port_0]
        )
        
        self.use_func = use_func
        content_packed = [170, 84, 72, 69, 32, 69, 71, 71, 83, 32, 65, 82, 69, 32, 72, 65, 84, 67, 72, 73, 78, 71, 46, 32, 32, 32, 32, 32, 32, 32]
        
        self.state_container = {
            "count": 0,
            "content": unpackbits(content_packed)
        }


    def general_work(self, input_items, output_items):
        outval = self.use_func(self.state_container)
        if outval == None:
            return 0
        else:
            dt = output_items[0][0].dtype
            npified = np.array(outval, dtype=dt)
            output_items[0][0] = npified
            return 1


```
</details>

Configuration for the rest of the flowgraph:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `80`
- Time Sink:
  - Turn on the markers and adjust anything else as necessary.

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
