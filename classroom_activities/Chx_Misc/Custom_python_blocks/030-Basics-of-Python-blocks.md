This gives an example of how to configure your own custom GNU Radio Python blocks.

### A simple flowgraph

This flowgraph consists of three blocks:

- A source block that produces the number 213 (repeatedly).
- A block whose output is the input multiplied by 3.
- A sink block that prints its input.

```python3
import numpy as np
from gnuradio import gr
import time


class Blk_source_output_arb_num(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Source: the number 213', in_sig=[], out_sig=[np.float32])

    def work(self, input_items, output_items):
        output_items[0][0] = 213.0
        return 1


class Blk_mult_three(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Multiply by three', in_sig=[np.float32], out_sig=[np.float32])

    def work(self, input_items, output_items):
        output_items[0][0] = 3 * input_items[0][0]
        return 1


class Blk_sink_print(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Print sink', in_sig=[np.float32], out_sig=[])

    def work(self, input_items, output_items):
        print(input_items[0][0])
        time.sleep(0.5)
        return 1


tb = gr.top_block()
source_arb = Blk_source_output_arb_num()
mu = Blk_mult_three()
sink_pri = Blk_sink_print()
tb.connect(source_arb, mu, sink_pri)
tb.run()
```

More coming soon.





```python3
import numpy as np
from gnuradio import gr


class blk_arbitrary_numbers_source(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Arbitrary Numbers Source',
            in_sig=[],
            out_sig=[np.float32, np.float32]
        )

    def work(self, input_items, output_items):
        
        # After we assign the values,
        # output_items looks something like this...
        # [
        #    [65.0, 67.0, 81.0, *, *, *, *, *, *, *],
        #    [3.2,   4.2,  5.2, *, *, *, *, *, *, *],
        # ]
        # (the * indicates an unassigned location in the array.)

        # Assign the output values of port 0
        output_items[0][0] = 65.0
        output_items[0][1] = 67.0
        output_items[0][2] = 81.0
        # Assign the output values of port 1
        output_items[1][0] = 30.2
        output_items[1][1] = 40.2
        output_items[1][2] = 50.2

        ## Alternatively, you could assign output values
        ## like this:
        output_items[0][0:3] = [65.0,  67.0,  81.0]

        ## However, this doesn't work:
        ## output_items[0] = [65.0,  67.0,  81.0]

        ## Returning 3 tells GNU Radio how many values
        ## that we've provided.
        return 3
```
