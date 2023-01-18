What if, instead of this...


```
    ____    ____    ________    ____        ____
____    ____    ____        ____    ________    ____
0   1   0   1   0   1   1   0   1   0   0   1   0
```

...we did this?...


```
    ____    ____________    ____
____    ____            ____    ____
s   0   s   1           s   0   s
```

_The 's' stands for separator. It's not a standard abbreviation as far as I know._

Pros and cons:

- (todo)

## Custom Python block

We're going to use this Python code. It's not production-ready, but it's great for proof-of-concept.

In GNU Radio, create a Python Block. Put this in the contents.

```python3
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Test 1',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def start(self, *args, **kwargs):
        import my_gnuradio_custom_python_helpers
        self.my_gnuradio_custom_python_helpers = my_gnuradio_custom_python_helpers
        return super().start(*args, **kwargs)

    def work(self, input_items, output_items):
        inOneP = input_items[0][0]
        outval = self.my_gnuradio_custom_python_helpers.processOneSample(inOneP)
        if outval == None:
            return 0
        else:
            output_items[0][0] = outval
            return 1
```

Then, create a python file in the same directory named `my_gnuradio_custom_python_helpers.py`. It must be named to match the name in the code you just copy/pasted.

In `my_gnuradio_custom_python_helpers.py`, put this:

```python3
def processOneSample(x):
    if x > 0.5:
        return 1
    else:
        return 0
```
