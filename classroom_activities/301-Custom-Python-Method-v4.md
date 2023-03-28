There may be times when you want to add some custom Python code to your flowgraph.

The way to do this in GNU Radio Companion is somewhat tricky, so we've made an approach that is slightly easier.

Step 1: Create a custom Python block, and paste this code:

```python3
import numpy as np
from gnuradio import gr


name = "Python Block: Run Function v4"
in_sig_port_0 = np.float32
out_sig_port_0 = np.uint8


### THIS IS THE PART THAT DOES THE ACTUAL MATH.
def use_func(datum, state_container):
    return datum + 1


### EVERYTHING BELOW THIS LINE IS "BOILERPLATE CODE".
class blk(gr.basic_block):

    def __init__(self, state_var_1=0.0, state_var_2=0.0, state_var_3=0.0):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[in_sig_port_0],
            out_sig=[out_sig_port_0]
        )
        
        self.use_func = use_func
        
        self.state_var_1 = state_var_1
        self.state_var_2 = state_var_2
        self.state_var_3 = state_var_3
        self.state_container = {}


    def general_work(self, input_items, output_items):
        inOneP = input_items[0][0]
        self.consume(0, 1)
        self.state_container["state_var_1"] = self.state_var_1
        self.state_container["state_var_2"] = self.state_var_2
        self.state_container["state_var_3"] = self.state_var_3
        outval = self.use_func(inOneP, self.state_container)
        self.state_var_1 = self.state_container["state_var_1"]
        self.state_var_2 = self.state_container["state_var_2"]
        self.state_var_3 = self.state_container["state_var_3"]
        if outval == None:
            return 0
        else:
            dt = output_items[0][0].dtype
            npified = np.array(outval, dtype=dt)
            output_items[0][0] = npified
            return 1
```

Step 2: Back in GNU Radio...
- Verify that you see three text fields: State_Var_1, State_Var_2, State_Var_3.
- Type 0 in each of the State_Var fields.
- Press OK.

Step 3: In the flowgraph, verify that the block's name is now "Python Block: Run Function v4".

Step 4: Let's rename the block:  
Reopen the code using the "Open in Editor" button.  
- On the line that says `name = "Python Block: Run Function v4"`, change it to `name = "Python Block: Add 1"`.
- On the line that says `out_sig_port_0 = np.uint8`, change it to `out_sig_port_0 = np.float32`.
Save.

Step 5: Your block is ready to use. Now, make this flowgraph to test it:

```
Vector source  ->  Python Block: Add 1  ->  Time Sink
```

- Vector Source:
  - Type: `Float`
  - Vector: [0.3, -0.9, -1.5]
- Python Block: Add 1:
  - Use the specs from above
- Time Sink:
  - General tab:
    - Type: `Float`
    - Number of Points: `30`
  - Config tab:
    - Line 1 Marker: `Circle`

You should see a zig-zag pattern that touches 1.3, 0.1, and -0.5. 

In future exercises, we'll abreviate these steps by simply saying "Create a Python Block using the v4 method".

_Practice exercise about how to change name and types, and how to use with `vec to stream` and `stream to vec` blocks. (work in progress)_
