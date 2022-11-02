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



## Improved version:

```python3

__chunk_length = 3   # type: int

def easy_work(chunk):
    # type: (list[int]) -> iterable[int]
    """the length of `chunk` is `chunk_length`."""
    resu = []
    for item in chunk:
        resu.append(item * 2)
    return resu


def __init__(self):
    self.in_accumulator = []
    self.out_queue = queue.SimpleQueue()

def general_work(self, inp, out):
    
    ## If there's any data available to push out, do that.
    try:
        item = self.out_queue.get_no_wait()
        out[0][0] = item
        return 1
    except queue.Empty:
        pass
    
    ## Process accumulated data if there's enough.
    if len(self.in_accumulator) == __chunk_length:
        result = easy_work(self.in_accumulator)
        for elem in result:
            self.out_queue.put(elem)
        self.in_accumulator = []
        return 0
    
    ## Accumulate more data for processing later.
    self.in_accumulator.append(inp[0][0])
    self.consume(0, 1)
    return 0
```


------------------

```python3
import numpy as np
from gnuradio import gr
import queue
from typing import Callable, Iterable



__chunk_length = 3   # type: int


def __easy_work_helper():
    # type: () -> Callable
    # data_container = {}

    def easy_work(chunk):
        # type: (list[int]) -> Iterable[int]
        """the length of `chunk` is `chunk_length`."""
        resu = []
        for item in chunk:
            resu.append(item * 2)
        return resu

    return easy_work


## GNU Radio Companion renames stuff, so we have to do this
_blk__easy_work_helper = __easy_work_helper


class blk(gr.basic_block):

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        self.in_accumulator = []
        self.out_queue = queue.SimpleQueue()
        self.easy_work = __easy_work_helper(self.queue_in, self.queue_out)


    def general_work(self, inp, out):
        
        ## If there's any data available to push out, do that.
        try:
            item = self.out_queue.get_no_wait()
            out[0][0] = item
            return 1
        except queue.Empty:
            pass
        
        ## Process accumulated data if there's enough.
        if len(self.in_accumulator) == __chunk_length:
            result = easy_work(self.in_accumulator)
            for elem in result:
                self.out_queue.put(elem)
            self.in_accumulator = []
            return 0
        
        ## Accumulate more data for processing later.
        self.in_accumulator.append(inp[0][0])
        self.consume(0, 1)
        return 0
```
