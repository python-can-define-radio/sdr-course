<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Jan 21: 081-Sig-interpret-practice-2.md
2022 Feb 22: 145-81-Sig-interpret-practice-2.md
2023 Apr 14: 145b-Sig-interpret-practice.md
2023 May 22: 034_Analyze_Sig_Data_from_analog_wave.md
</pre>
</details>

## Digital data interpretation exercise #2

```
Python Block  -->  Time Sink
              -->  Waterfall Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Waterfall sink, etc.

```python3
import numpy as np
from gnuradio import gr


name = "Mystery Signal 2"
out_sig_port_0 = np.complex64


def use_func(state_container):
    idx = state_container["count"] // 200
    content = state_container["content"]
    if idx >= len(content):
        return None
    curOutput = content[idx]
    retval = curOutput *  np.exp(0.1j * state_container["count"])
    state_container["count"] += 1
    return retval


class blk(gr.basic_block):

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[],
            out_sig=[out_sig_port_0]
        )
        
        self.use_func = use_func
        self.state_container = {
            "count": 0,
            "content": ([
                1, 0, 1, 0, 1, 0, 1, 0,
                0, 1, 0, 1, 1, 0, 0, 1,
            ] + [0] * 16)
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
  - Value: `2e6`
- Time Sink:
  - Number of Points: `4000`
  - _You may wish to make other adjustments._

---

Questions:

1. What is the period of the wave (approx)?
2. What is the frequency of the wave (approx)?
3. Would you describe the signal as pulsing on and off, or continuously varying in amplitude? Based on that answer, is the modulation technique most likely analog or digital?
4. How wide is a single pulse (time, approx)?
5. How wide is a single pulse (samples, approx)? _Hint: Use the time and the sample rate to determine this rather than counting samples._
6. If you were to guess, what modulation scheme do you think this is? Choices: FSK, OOK, PSK

A collaborator suggests that this communication may be the letter Y or N in Unicode. You point out that there seem to be 16 bits of information rather than 8. The collaborator says that this might be an 8-bit preamble* followed by a single Unicode character. In other words, the first 8 bits are not conveying information, they are just intended to mark the start of the message. 

Questions continued:

7. What is the bit sequence of the 8-bit preamble? (Hint: It starts with 1 0).
8. What is the bit sequence of the 8-bits of actual data?
9. Assuming a Unicode interpretation, was the data a "Y" or an "N"?


*Incidentally, Ethernet frames have a preamble that is similar to the one shown above. The Ethernet preamble is longer (approx 60 bits long, depending how you count), but the 101010... pattern at the beginning is the same.
