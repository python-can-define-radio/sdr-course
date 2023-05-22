<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Jan 23: 090-Sig-interpret-practice-3.md
2023 May 22: 031_Analyze_Sig_Packbits.md
</pre>
</details>

## Digital data interpretation exercise #3

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



name = "Mystery Signal 3"
out_sig_port_0 = np.uint8


def use_func(state_container):
    idx = state_container["count"]
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
        content_packed = [84, 72, 69, 32, 68, 79, 71, 83, 32, 65, 82, 69, 32, 73, 78, 32, 80, 79, 83, 73, 84, 73, 79, 78, 46, 32, 32, 32, 32, 32, 32, 32, 32, 32]
        
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
  - Value: `10`
- Time Sink:
  - Number of Points: `150` (You may need more to see the whole message, but remember -- if you set it too high, GNU Radio won't display ANY data.)
  - I recommend turning on the markers for the points.

---

Questions:

1. Does it appear that each sample corresponds to one bit or one byte?
2. Given the sample rate, how many seconds of data are needed to express one bit?
3. How many seconds of data are needed to express one byte?
4. What is the decimal number that corresponds to the first byte?
5. What is the character that corresponds to the first byte?
6. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits represents a single Unicode-encoded character. _Note: This should not require manually counting zeros and ones._
