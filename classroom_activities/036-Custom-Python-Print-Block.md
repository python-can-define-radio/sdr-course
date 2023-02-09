People sometimes ask "where's the 'print' command in GNU Radio Companion?"

I hypothesize that a "print" block was omitted because the GUI Sinks are most often the best way to view the data, but here's a print block in case you ever find it useful.

How to use: Follow steps 1 through 6 in the "Custom Python Method" exercise.

<details><summary>Use this code: (click to view code) </summary>

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
    
Once you've created the block with that code, save and close the editor.

You'll see that there's a blank "Sleep_Seconds" field in the GNU Radio GUI. `0.5` in that Sleep_seconds.

Then, use a vector source (as in the previous exercise) to test that the print block works.

You'll see that when it runs, the window is empty. The print block only outputs in the built-in GNU Radio "terminal". Ask if you need help finding it.
