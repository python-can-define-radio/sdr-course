This is an activity scanner that uses both Python and GNU Radio Companion. We plan to write more thorough directions in the next few months.

```
osmocom   -->  Band pass   -->  Complex   -->  Moving   -->  Keep 1 in N  -->  Python Block: 
source         filter           to Mag         Average                         Data Receiver
```

slideable IF and BB gain

Code for Python Block: Data Receiver
```python3
import numpy as np
from gnuradio import gr
import queue


class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Data Receiver',
            in_sig=[np.float32],
            out_sig=[]
        )
        self.data_queue = queue.SimpleQueue()

    def work(self, input_items, output_items):
        dataPoint = input_items[0][0]
        self.data_queue.put(dataPoint)
        return 1

```

Then run a separate controller with this code:

```python3
import time

from qt_block_init_PYPURE import set_up_qt_top_block_and_run_func_in_thread

from name_of_the_flowgraph_above import name_of_the_flowgraph_above


def doActions(tb):
    # type: (name_of_the_flowgraph_above) -> None
    
    for freq in range(int(88e6), int(108e6), int(10e3)):
        tb.osmosdr_source_0.set_center_freq(freq)
        dataPoint = tb.epy_block_0.data_queue.get()
        print(f"{freq:14} {dataPoint:20}")


set_up_qt_top_block_and_run_func_in_thread(name_of_the_flowgraph_above, doActions)
```
