There may be times when you want to add some custom Python code to your flowgraph.

The way to do this in GNU Radio Companion is somewhat tricky, so we've made an approach that is slightly easier.

Step 1: Ctrl F, Python Block.

Step 2: Double click the Python Block that you just created.

Step 3: Click "Open in Editor". If the computer becomes unresponsive, press Esc a few times, and go back to step 2.

Step 4: Click "Use Default Editor".

Step 5: Erase all of the code that is there.

Step 6: Paste the code shown below, SAVE, and close the editor.

Step 7: You should now see four text fields: Func_To_Use, State_Var_1, State_Var_2, State_Var_3. Unless otherwise directed, type 0 in each of the State_Var fields.

Here's the code you will paste in Step 6:

```python3
import numpy as np
from gnuradio import gr


name = 'Python Block: Run Function v4'
in_sig = np.float32
out_sig = np.float32


class blk(gr.basic_block):
    def __init__(self, func_to_use="", state_var_1=0.0, state_var_2=0.0, state_var_3=0.0):
        gr.basic_block.__init__(
            self,
            name=name,
            in_sig=[in_sig],
            out_sig=[out_sig]
        )
        self.use_func_str = func_to_use
        self.state_var_1 = state_var_1
        self.state_var_2 = state_var_2
        self.state_var_3 = state_var_3
        self.state_container = {}

    def start(self, *args, **kwargs):
        import my_gnuradio_custom_python_helpers
        self.use_func = eval(self.use_func_str)
        return super().start(*args, **kwargs)

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

In future exercises, we'll abreviate these steps like so: "Create a Python Block using the v4 method."

Practice exercise about how to change name and types, and how to use with `vec to stream` and `stream to vec` blocks. (_work in progress_)



