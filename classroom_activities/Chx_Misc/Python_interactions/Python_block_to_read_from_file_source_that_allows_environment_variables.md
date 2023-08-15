```python3
import numpy as np
from gnuradio import gr
import os


class blk(gr.sync_block):

    def __init__(self, path_that_may_have_vars=""):
        gr.sync_block.__init__(
            self,
            name='Python Block: File Source\n that can handle\n environment variables\n but inefficiently loads entire file \n into RAM. Repeats.',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64]
        )
        self.path = os.path.expandvars(path_that_may_have_vars)

    def start(self):
        print(f"Expanded path: {self.path}")
        self.filedata = np.fromfile(self.path, dtype=np.complex64)
        self.currentFilePosition = 0
        return super().start()
    
    def work(self, input_items, output_items):
        sliceStart = self.currentFilePosition
        sliceEnd = sliceStart + len(output_items[0])
        _slice = self.filedata[sliceStart:sliceEnd]
        output_items[0][:len(_slice)] = _slice
        self.currentFilePosition += len(_slice)
        if self.currentFilePosition >= len(self.filedata):
            self.currentFilePosition = 0
        return len(_slice)
```
