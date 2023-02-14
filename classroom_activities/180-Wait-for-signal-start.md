TODO: Write an explanation

```python3
import numpy as np
from gnuradio import gr
import time


name = "Python Block:\nKeep N data points\nafter threshold surpassed"
in_sig_port_0 = np.float32
out_sig_port_0 = np.float32


def use_func(datum, state_container, block_self):
    listen_count = state_container["listen_count"]
    if listen_count > 0:
        listen_count = listen_count - 1
        state_container["listen_count"] = listen_count
        return datum

    elif datum >= block_self.threshold:
        listen_count = block_self.points_to_keep - 1
        state_container["listen_count"] = listen_count
        return datum
    else:
        return None



class blk(gr.basic_block):

    def __init__(self, threshold=0.1, points_to_keep=7):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[in_sig_port_0],
            out_sig=[out_sig_port_0]
        )
        
        self.use_func = use_func
        self.threshold = threshold
        self.points_to_keep = points_to_keep
        self.state_container = { "listen_count": 0 }


    def general_work(self, input_items, output_items):
        inOneP = input_items[0][0]
        self.consume(0, 1)

        outval = self.use_func(inOneP, self.state_container, self)
        if outval == None:
            return 0
        else:
            dt = output_items[0][0].dtype
            npified = np.array(outval, dtype=dt)
            output_items[0][0] = npified
            return 1

```
