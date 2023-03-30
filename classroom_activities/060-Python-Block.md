It is sometimes useful to create a Python Block. This exercise will present the process which will be used in later exercises.

In the "GNU Radio Companion" computer program, create a flowgraph named `python_block_intro.grc`.

```
Python Block  -->  Time Sink
```

- Follow these steps:
  1. Double click the Python Block.
  2. Click "Open in Editor". If the computer becomes unresponsive, press Esc a few times, and go back to step 2.
  3. Click "Use Default" editor program.
  4. Erase all of the code that is there.
  5. Paste the code given below.
  6. Save (press button or {ctrl}{s})
  7. Close the editor.

Given code:

```python3
import numpy as np
from gnuradio import gr
import random


name = "Practice Signal"
out_sig_port_0 = np.complex64


class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name=name,
            in_sig=[],
            out_sig=[out_sig_port_0]
        )


    def work(self, input_items, output_items):
        output_items[0][0] = random.random() + random.random()*1j 
        return 1
```

When you run the *.grc file in GNU Radio Companion, you should see random noise in the Time Sink.
