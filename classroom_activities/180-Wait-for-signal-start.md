## Waiting for the start of the signal

Usually, the receiver will be listening before the transmission starts. The recevier needs to know whether or not there is data being transmitted so it knows whether to save the data or discard it (assuming that nothing is being transmitted).

This block keeps a given number of data points after a threshold is surpassed. Try various vector sources to see if you can determine how it works.

```python3
import numpy as np
from gnuradio import gr
from typing import Optional, Type
import time


name = "Python Block:\nKeep N data points\nafter threshold surpassed"
in_sig_port_0 = np.float32
out_sig_port_0 = np.float32



def use_func(datum, block_self):
    # type: (Type[in_sig_port_0], blk) -> Optional[Type[out_sig_port_0]]

    ## This is the case in which we've already
    ## seen a value that surpasses the threshold:
    ## Pass the data to the next block, and 
    ## count down.
    if block_self.keep_counter > 0:
        block_self.keep_counter -= 1
        return datum

    ## If it meets the threshold:
    elif datum >= block_self.threshold:
        ## Start the counter at one less than the number to keep,
        ## because we're returning one data point in this iteration.
        block_self.keep_counter = block_self.points_to_keep - 1
        return datum
    else:
        ## didn't meet threshold: throw away the data.
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
        self.keep_counter = 0

    def general_work(self, input_items, output_items):
        inOneP = input_items[0][0]
        self.consume(0, 1)

        outval = self.use_func(inOneP, self)
        if outval == None:
            return 0
        else:
            dt = output_items[0][0].dtype
            npified = np.array(outval, dtype=dt)
            output_items[0][0] = npified
            return 1


```
