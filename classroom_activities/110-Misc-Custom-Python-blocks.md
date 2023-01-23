_Note: This file isn't finished, but it has some useful parts._


Length of data so far; useful for checking speed
```python3
import numpy as np
from gnuradio import gr
import random


class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Length stuff',
            in_sig=[np.float32],
            out_sig=[]
        )
        self.totlen = 0
        
    def work(self, input_items, output_items):
        onelen = len(input_items[0])
        self.totlen += onelen
        if random.random() > 0.9999:
            print(onelen, self.totlen)
        return 0
```


```python3
import numpy as np
from gnuradio import gr

class output_1_forever_once_input_equals_1(gr.sync_block):
    """Example:
    if the input stream is 0, 0, 1, 0, 0
    the output will be 0, 0, 1, 1, 1.
    """

    def __init__(self):
        gr.sync_block.__init__(self,
            name="Output 1 forever once input equals 1",
            in_sig=[np.uint8],
            out_sig=[np.uint8])
        self.reachedOne = False

    def work(self, input_items, output_items):
        inBuf = input_items[0]
        outBuf = output_items[0]
        if self.reachedOne:
            outBuf[:] = 1
        else: 
            for idx, item in enumerate(inBuf):
                justAfterOneLoc = idx + 1
                if item == 1:                
                    self.reachedOne = True
                    break
            outBuf[:justAfterOneLoc] = 0
            outBuf[justAfterOneLoc:] = 1
        
        return len(outBuf)
```

Keep first stream where second is 1

```python3
import numpy as np
from gnuradio import gr

class keep_first_stream_where_second_is_1(gr.basic_block):
    """Example:
    if the first stream (in0) is 7.0, 2.0, -3.0, 5.0, -8.0
    and the second stread is 1,  1,  0,  0,  1
    the output will be 7.0, 2.0, -8.0.
    
    Feel free to modify the `copy_type` variable inside the block definition
    according to your needs -- `np.float32`, `np.uint8`, etc
    """

    def __init__(self):
        
        # Feel free to change this according to the type you need to copy.
        copy_type = np.float32
        
        gr.basic_block.__init__(self,
            name="Keep first stream where second is 1",
            in_sig=[copy_type, np.uint8],
            out_sig=[copy_type])

    def general_work(self, input_items, output_items):
        #buffer references
        in0 = input_items[0][:len(output_items[0])]
        in1 = input_items[1][:len(output_items[0])]
        outBuffer = output_items[0]

        #process data
        outData = in0[in1 == 1]
        outBuffer[:len(outData)] = outData

        #consume the inputs
        self.consume(0, len(in0)) #consume port 0 input
        self.consume(1, len(in1)) #consume port 1 input

        #return produced
        return len(outData)
```


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


Not correct yet: an on-off block

```python3
import numpy as np
from gnuradio import gr
from gnuradio import analog
from numba import njit


@njit
def numba_work(SAMPLES_TILL_SWITCH, current_sample_count, out_buffer):
    print(SAMPLES_TILL_SWITCH)
    currentPosition = 0
    currentlyOn = False
    for i in range(len(out_buffer)):
        if currentlyOn:
            out_buffer[i] = np.float32(1)
        else:
            out_buffer[i] = np.float32(0)

        currentPosition += 1

        if currentPosition == SAMPLES_TILL_SWITCH:
            currentlyOn = not currentlyOn
            currentPosition = 0
        


## A hier block is one that has other blocks inside of it
class blk(gr.sync_block):

    def __init__(self, Sample_Rate=1, period=0.5):

        gr.sync_block.__init__(self, 
                                "on_off_sig_period",
                                in_sig=None,
                                out_sig=[np.float32]
                                )
        
        samples_per_cycle = Sample_Rate * period
        # We switch twice per period (on, off)
        samples_till_switch = samples_per_cycle / 2
        assert samples_till_switch == int(samples_till_switch)
        self.SAMPLES_TILL_SWITCH = int(samples_till_switch)
        self.current_sample_count = 0

    def work(self, input_items, output_items):
        out_zero = output_items[0]
        
        numba_work(self.SAMPLES_TILL_SWITCH, self.current_sample_count, out_zero)
        # TODO update # block_ref.current_sample_count = 
        return len(out_zero)


```
