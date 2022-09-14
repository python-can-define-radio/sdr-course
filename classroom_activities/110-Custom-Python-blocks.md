Multiply by 2 block

```python3
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Mult by 2: Python Block',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )


    def work(self, input_items, output_items):
        in_zero = input_items[0]
        out_zero = output_items[0]
        out_zero[:] = in_zero[:] * 2
        return len(in_zero)
```


Add block

```python3
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    """Add Python Block.
    Equivalent to the built-in Add block. Remaking for educational purposes."""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Add: Python Block',
            in_sig=[np.complex64, np.complex64],
            out_sig=[np.complex64]
        )


    def work(self, input_items, output_items):
        in_zero = input_items[0]
        in_one = input_items[1]
        out_zero = output_items[0]
        out_zero[:] = in_zero[:] + in_one[:]
        return len(in_zero)
```


Experimenting with Sinks

```python3
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Debug sink that counts',
            in_sig=[np.complex64],
            out_sig=None
        )
        self.the_count_var = 0
        self.millions = 0
        self.groups_proc = 0

    def work(self, input_items, output_items):
        in_zero = input_items[0] 
        self.the_count_var += len(in_zero)
        self.groups_proc += 1
        if self.the_count_var > 1000000:
            self.the_count_var -= 1000000
            self.millions += 1
            print(self.millions, "millions.", self.groups_proc, "groups", in_zero[:5], "dat")
        return len(in_zero)
```
