# NOT FINISHED

```python3
"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from queue import SimpleQueue, Empty
from typing import Callable


def __easy_work_helper(queue_in, queue_out):
    # type: (SimpleQueue, SimpleQueue) -> Callable
    # data_container = {}
    def easy_work():
        itema = queue_in.get()
        itemb = queue_in.get()
        proca = itema - 10
        procb = itemb - 10
        queue_out.put(proca)
        queue_out.put(procb)
        # data_container["a"] = item + data_container.get("a", 0)
    return easy_work


## GNU Radio renames stuff
_blk__easy_work_helper = __easy_work_helper


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.queue_in = SimpleQueue()
        self.queue_out = SimpleQueue()
        self.easy_work = __easy_work_helper(self.queue_in, self.queue_out)



    def general_work(self, input_items, output_items):
        first_input_element = input_items[0][0]
        self.queue_in.put(first_input_element)
        self.consume(0, 1)
        
        # TODO: this is terrible because qsize is approximate, 
        # and the threshold of 4 is arbitrary
        if self.queue_in.qsize() < 4:
            return 0
        
        self.easy_work()

        outBuf = output_items[0]
        try:
            outItem = self.queue_out.get_nowait()
            outBuf[0] = outItem
            return 1
        except Empty:
            return 0


    # def work(self, input_items, output_items):
    #     """example: multiply with constant"""
    #     for item in input_items[0]:
    #         self.queue_in.enque(item)
    # result = self.easy_work(self.queue_in)
    #     output_items[0][:] = input_items[0] * self.example_param
    #     return len(output_items[0])
```
