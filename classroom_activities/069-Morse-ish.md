In an earlier section, we discussed communicating zeros and ones like this:


```
    ____    ____    ________    ____        ____
____    ____    ____        ____    ________    ____
0   1   0   1   0   1   1   0   1   0   0   1   0
```

This is equivalent to any two-letter alphabet, such as

```
    ____    ____    ________    ____        ____
____    ____    ____        ____    ________    ____
A   B   A   B   A   B   B   A   B   A   A   B   A
```


For our implementation with the Hack RF, we're going to explore a different approach, which is similar to Morse Code.

_Note: the "s" stands for "separator". It's not a standard abbreviation as far as I know._

```
____            ____________    
    ____________            ____
A   s           B           s   
```

Before, we did off = zero and on = one.  
Now, we're doing short-on = zero, long-on = one, and off = nothing (a separator).

To discuss:

- How does the new approach affect our data transmission rate?
- Does the new approach require an indication of begin-transmission or end-transmission?

## Custom Python block

We're going to use this Python code. It's not production-ready, but it's great for proof-of-concept.

Make a new directory called `ex_069`. Create a new flowgraph, and save it in there with the name `morse_demo_1.grc`.

In that flowgraph, create a Python Block. Put this in the contents.

```python3
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self, func_to_use="my_gnuradio_custom_python_helpers.convert_to_morse_ish"):
        gr.sync_block.__init__(
            self,
            name='Modulate Morse-ish',
            in_sig=[np.uint8],
            out_sig=[(np.uint8, 4)]
        )
        self.use_func_str = func_to_use

    def start(self, *args, **kwargs):
        import my_gnuradio_custom_python_helpers
        # self.my_gnuradio_custom_python_helpers = my_gnuradio_custom_python_helpers
        self.use_func = eval(self.use_func_str)
        return super().start(*args, **kwargs)

    def work(self, input_items, output_items):
        inOneP = input_items[0][0]
        outval = self.use_func(inOneP)
        if outval == None:
            return 0
        else:
            dt = output_items[0][0].dtype
            npified = np.array(outval, dtype=dt)
            output_items[0][0][:] = npified
            return 1
```

In the Func_To_Use blank, put "my_gnuradio_custom_python_helpers.convert_to_morse_ish" WITH QUOTES.

Then, create a python file in the same directory named `my_gnuradio_custom_python_helpers.py`. It must be named to match the name in the code you just copy/pasted.

In `my_gnuradio_custom_python_helpers.py`, put this:

```python3
def convert_to_morse_ish(datapoint):
    if datapoint == 0:
        return [1, 0, 0, 0]
    elif datapoint == 1:
        return [1, 1, 1, 0]
    else:
        print("ERROR")
```

Here's how we'll test it:

```
Vector Source  ->  Modulate Morse-ish  ->  Vector to Stream  ->  Repeat  ->  UChar to Float  -> Time Sink
```

Then, we'll make the receiver.

## Morse-ish receiver

Discuss: How to demod? Describe algorithm, then discuss Python.

```
Demod Morse-ish  ->  Throttle  ->  File Sink
```

### Exercises:

Later, after making it wavey, try changing the Repeat amount to see how it impacts the bandwidth (i.e. the width of the required space on the spectrum).

### Also

Do average of fourths-of-a-chip.
