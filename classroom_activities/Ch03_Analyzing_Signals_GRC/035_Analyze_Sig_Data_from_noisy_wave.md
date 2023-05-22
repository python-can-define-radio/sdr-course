<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 15: 065-ASK-full.md
2022 Aug 30: 165-ASK-full.md
2022 Oct 25: 165-OOK-full-Fourstep.md
2023 Jan 28: 150-Sig-interpret-practice-6.md
2023 May 22: 035_Analyze_Sig_Data_from_noisy_wave.md
</pre>
</details>

## Digital data interpretation exercise #6

```
Python Block  -->  Time Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
import numpy as np
from gnuradio import gr
from functools import reduce
from operator import concat
import random



name = "Mystery Signal 6"
out_sig_port_0 = np.complex64



def use_func(state_container):
    idx = state_container["count"] // 200
    content = state_container["content"]
    if idx >= len(content):
        return None
    # since the noise is bounded, it won't require filtering beyond the binary slice
    noise = random.random() * 0.5  
    retval = content[idx] * 3 * np.exp(0.5j * state_container["count"]) + noise
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
        content_packed = [170, 87, 69, 32, 76, 73, 75, 69, 32, 66, 85, 84, 84, 69, 82, 32, 79, 78, 32, 79, 85, 82, 32, 84, 79, 65, 83, 84, 46, 32, 32, 32, 32, 32, 32, 32]
        
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
  - Value: `1000`
- Time Sink:
  - You may wish to increase the Number of Points. Remember that GNU Radio sometimes takes a few seconds to display data when the Number of Points is large, and that it will (unfortunately) display no data if the Number of Points is too large.

---

Questions:

1. How many samples do you think express a single bit?
2. Given the sample rate, how many seconds of data are needed to express one bit?
3. How many seconds of data are needed to express one byte?

A collaborator suggests that this communication most likely has an 8 bit preamble.

4. How many samples long is the preamble?
5. What block would be useful for skipping the preamble?
6. What block would be useful for removing the duplicate samples that are being used to express a single bit?
7. What block (that you have already used) would be useful for "converting" the complex wave into a magnitude?
8. What block(s) would be useful for slicing the data into zeros and ones? At what height should you slice it?
9. After stripping the 8-bit preamble, what is the decimal number that corresponds to the first byte?
10. What is the character that corresponds to the first byte?
11. Using whatever blocks necessary, decode the message. Assume that each group of 8 bits (with the exception of the preamble) represents a single Unicode-encoded character.
