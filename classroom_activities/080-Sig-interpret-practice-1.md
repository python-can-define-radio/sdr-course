## Digital data interpretation exercise #1

```
Python Block  -->  Time Sink
              -->  Frequency Sink
```

Configuration:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - It's up to you! I recommend adjusting the `Number of Points` and the `Line 1 Marker`.
- Python Block:
  - Follow the steps described in an earlier exercise to fill in the code below:

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

Note: this code is not meant to be readable. Rather, the goal of this exercise is to explore the mystery signal using the Time Sink, Frequency Sink, etc.

```python3
import numpy as np
from gnuradio import gr


name = "Mystery Signal 1"
out_sig_port_0 = np.complex64


def use_func(state_container):
    if state_container["count"] > 2000:
        return None
    if state_container["count"] < 20 or 40 <= state_container["count"] < 60:
        retval = np.exp(0.5j * state_container["count"])
    else:
        retval = 0
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
        self.state_container = {"count": 0}


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

---

Questions:

1. What is the period of the wave (approx)?
2. What is the frequency of the wave (approx)?
3. Would you describe the signal as pulsing on and off, or continuously varying in amplitude? Based on that answer, is the modulation technique most likely analog or digital?
4. How wide is a single pulse (time, approx)?
5. How wide is a single pulse (samples)?
6. If you were to guess, what modulation scheme do you think this is? Choices: FSK, OOK, PSK
