Often, there are signals that we want to remove from the data we're working with. The unwanted signals may be random electrical noise or radio stations that are near our station of interest, but in either case, filtering out these unwanted signals is a very useful skill.

`filter_exploration_2.grc`
```
Python Block -->  Throttle  -->  Time Sink
                            -->  Waterfall Sink
                            -->  Frequency Sink
```

<details><summary>The code for the Python block: (<i>click to expand</i>)</summary>

```
import numpy as np
from gnuradio import gr
from functools import reduce
from operator import concat
import random



name = "Learning Signal for band pass"
out_sig_port_0 = np.complex64



def sigOne(state_container):
    cou = state_container["count"]
    content = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    idx = (cou // 20000) % len(content)
    return content[idx] * np.exp(0.2j * cou)


def sigTwo(state_container):
    cou = state_container["count"]
    content = [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    idx = (cou // 50000) % len(content)
    return content[idx] * np.exp(1.2j * cou)


def use_func(state_container):
    noise = (random.random() - 0.5) * 0.25 + (random.random() - 0.5) * 0.25j
    summ = sigOne(state_container) + sigTwo(state_container) + noise    
    state_container["count"] += 1
    # Note: the count will grow unbounded. Python has arbitrary size integers, so 
    # that should be ok since this isn't a tight-performance situation
    return summ


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
        
        
        self.state_container = {
            "count": 0,
           
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

Watch what happens when you run that flowgraph. Then, insert a band pass filter in the middle (before or after the Throttle; it doesn't matter).

- Band Pass Filter parameters:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cutoff Freq: `low_cut`
  - High Cutoff Freq: `high_cut`
  - Transition Width: `samp_rate/50`

Make two GUI Ranges: one for `low_cut` and one for `high_cut`.

- `low_cut`: from `-samp_rate/2` to `0`. Default: Pick anything within the slider's range except zero. Step: 1
- `high_cut`: from `0` to `samp_rate/2`. Default: Pick anything within the slider's range except zero. Step: 1

Try sliding the sliders to see if you can filter one signal or the other. If you find that the sliders aren't able to reach where you want them to reach, then adjust the Start and Stop of the sliders. However, GNU Radio will behave unpredictably if you ever break the rule that `low_cut < high_cut`.

