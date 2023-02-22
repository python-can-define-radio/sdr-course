People sometimes ask "where's the 'print' command in GNU Radio Companion?"

I hypothesize that a "print" block was omitted because the GUI Sinks are most often the best way to view the data, but there are cases in which a print block can help with exploring data.

Here's the code which you'll use in other flowgraphs.

<details><summary>Code: (click to view code) </summary>

```python3
    
import numpy as np
from gnuradio import gr
import time


name = "Python Block: Print"
in_sig_port_0 = np.float32


class blk(gr.sync_block):

    def __init__(self, sleep_seconds=0.5):
        gr.sync_block.__init__(
            self,
            name=name,
            in_sig=[in_sig_port_0],
            out_sig=[]
        )
        self.sleep_seconds = sleep_seconds
        
    def work(self, input_items, output_items):
        singleDataPoint = input_items[0][0]
        
        print("{:.3f}".format(singleDataPoint))
        time.sleep(self.sleep_seconds)

        return 1
```

</details>

Here's a flowgraph to test the code.

`print_block_testing.grc`

```
Vector Source  -->  Python Block
```

Parameters:
- Vector Source:
  - Vector: 
- Python Block:
  - <i>Follow the steps described in the previous exercise to edit the Python Block code. Copy the code given above. After saving and closig the editor, you'll see the Sleep_Seconds field.</i>
  - Sleep_Seconds: `0.5`

You'll see that when it runs, the window is empty. The print block only outputs in the built-in GNU Radio "terminal". Ask if you need help finding it.
