Boilerplate code:

```python3
import numpy as np
from gnuradio import gr
import random
import numba
from typing import Iterable, Any



### INSERT YOUR CODE BELOW THIS LINE

### INSERT YOUR CODE ABOVE THIS LINE



# GNU Radio does some renaming stuff
_blk__block_name = __block_name
_blk__block_in_type = __block_in_type
_blk__block_out_type = __block_out_type

@numba.njit()
def processHelper(inBuf, outBuf):
    # type: (np.ndarray, np.ndarray) -> int
    idx = 0
    for outval in processItems(inBuf):
        outBuf[idx] = outval
        idx += 1
    return idx


class blk(gr.basic_block):

    def __init__(self):
        gr.basic_block.__init__(
            self,
            name=_blk__block_name,
            in_sig=[_blk__block_in_type],
            out_sig=[_blk__block_out_type]
        )

    def general_work(self, input_items, output_items):
        outBuf = output_items[0]
        inPortZero = input_items[0]

        # Only grab as many items as can fit in the output buffer.
        # TODO: This assumes that len(output) <= len(input).
        # That's not always the case; interpolating blocks are one example.
        # For now, the fix for an interpolating block is to manually set this
        # to a smaller amount of samples, such as inPortZero[:len(outBuf)//4]
        # It's always safe to grab fewer data points, but may be slower.
        inBuf = inPortZero[:len(outBuf)]
        
        # Assume all input data will be consumed.
        consumeLen = len(inBuf)
        
        outLen = processHelper(inBuf, outBuf)

        self.consume(0, consumeLen)
        
        return outLen
```

Examples of what you could insert:

```python3
__block_name = "Keep between 68 and 79 Python Block"
__block_in_type = np.uint8
__block_out_type = np.uint8

@numba.njit()
def processItems(inBuf):
    # type: (np.ndarray) -> Iterable[Any]
    for item in inBuf:
        if 68 < item < 79:
            yield item
```

```python3
__block_name = "Multiply by 2 Python Block"
__block_in_type = np.uint8
__block_out_type = np.uint8

@numba.njit()
def processItems(inBuf):
    # type: (np.ndarray) -> Iterable[Any]
    return inBuf * 2
```
