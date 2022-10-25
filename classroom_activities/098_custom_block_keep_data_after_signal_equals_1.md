_Note: This exercise isn't finished, but it is still useful._

This is a custom block. Ctrl+F "Python Block" and copy paste.


```python3
import numpy as np
from gnuradio import gr


class blk(gr.basic_block):

    def __init__(self):
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='Keep all data after signal equals 1',
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        self.has_reached_one = False


    def general_work(self, input_items, output_items):
        #buffer references
        outpt = output_items[0]
        inpt = input_items[0][:len(outpt)]
        

        #process data
        if self.has_reached_one:
            outpt[:] = inpt[:]
        else:
            hitOne = np.where(input_items[0] == 1)[0]
            
            ## if it hit one
            if len(hitOne) > 0:
                self.has_reached_one = True
                hitOneIndx = hitOne[0]
                outpt[:] = inpt[hitOneIndx:]


        #consume the inputs
        self.consume(0, len(inpt))  #consume port 0 input

        #return produced
        return len(outpt)




    # def work(self, input_items, output_items):
    #     """example: multiply with constant"""
    #     outpt = output_items[0]
    #     inpt = input_items[0]

        
    #     output_items[0][:] = input_items[0] * self.example_param
    #     return len(output_items[0])
```
