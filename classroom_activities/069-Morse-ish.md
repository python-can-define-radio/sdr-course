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

Before, we did off = A and on = B.  
Now, we're doing short-on = A, long-on = B, and off = nothing (a separator).

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


class blk(gr.basic_block):
    def __init__(self, func_to_use="", state_var_1=0.0, state_var_2=0.0, state_var_3=0.0):
        gr.basic_block.__init__(
            self,
            name='Run Python Function v4',
            in_sig=[(np.uint8, 1)],
            out_sig=[(np.uint8, 4)]
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
            output_items[0][0][:] = npified
            return 1
```

In the Func_To_Use blank, put "my_gnuradio_custom_python_helpers.modulate_morseish" WITH QUOTES.

Then, create a python file in the same directory named `my_gnuradio_custom_python_helpers.py`. It must be named to match the name in the code you just copy/pasted.

In `my_gnuradio_custom_python_helpers.py`, put this:

```python3
def modulate_morseish(datapoint, state_container):
    if datapoint == 0:
        return [1, 0, 0, 0]
    elif datapoint == 1:
        return [1, 1, 1, 0]
    else:
        print("ERROR")
```

Here's how we'll test it:

```
Vector 
Source  ->  Run Python  
            Function v4  ->  Vector to
                           Stream    ->  Repeat ->  UChar to 
                                                    Float  -> Time 
                                                              Sink
                                               
```

- Vector source:
  - Vector: [0, 0, 1]
  - Repeat: Yes
- Run Python Function v4
  - Func_to_use: "my_gnuradio_custom_python_helpers.modulate_morseish"  
     _with quotes_
- Vector to stream:
  - 4, 1
- Repeat:
  - 1
- Time Sink:
  - Number of points: 30 

Then, we'll make the receiver.

## Morse-ish receiver

Discuss: How to demod? Describe algorithm, then discuss Python.

```
Run Python Function v4  ->  Throttle  ->  File Sink
```

- Run Python Function v4
  - Func_to_use: "my_gnuradio_custom_python_helpers.demod_morseish"  
     _with quotes_


In the same helper file:

```python3
def demod_morseish(chunk, state_container):
    if all(chunk == [1, 0, 0, 0]):
        return 0
    elif all(chunk == [1, 1, 1, 0]):
        return 1
    else:
        print("ERROR")
```

### Keep after first 1

_TODO - details_

```python3
def keep_after_first_1(datapoint, state_container):
    if state_container.get("seen_1") == True:
        return datapoint
    elif datapoint == 0:
        return None
    elif datapoint == 1:
        state_container["seen_1"] = True
        return datapoint
    else:
        print("ERROR")
```

### Average and slice

```python3
def average_and_slice(chunk, state_container):
    avg = np.average(chunk)
    
    # will need to experiment with the threshold after experimenting with the AGC
    thresh = state_container["state_var_1"]
    if avg > thresh:  
        return 1
    else:
        return 0
```

### Improved demod given fuzzy symbol length

```python3
def demod_morseish(chunk, state_container):
    numberOfOnes = chunk.tolist().count(1)
    
    ## We'll have to experiment with this too.
    thresh = state_container["state_var_1"]
    if numberOfOnes > thresh:
        return 1
    elif numberOfOnes > thresh / 3:
        return 0
    else:
        print("ERROR")
```

### Band pass filter

Useful

### Complex to Mag

Will need this

### AGC

Very useful, but let's get the pure simulation and basic real transmission working first.

Experiment with the rate parameter: try numbers between 0.00001 and 1. As far as I can tell, we want the amplitude variation during a single symbol to be no more than about 20% (but let's experiment to make sure that makes sense).

### Exercises:

Later, after making it wavey, try changing the Repeat amount to see how it impacts the bandwidth (i.e. the width of the required space on the spectrum).
