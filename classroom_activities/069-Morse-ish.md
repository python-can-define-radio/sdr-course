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
_Incidentally, this could be thought of as sending E (a "dit" in Morse) and T (a "dah" in Morse)._

To discuss:

- How does the new approach affect our data transmission rate?
- Does the new approach require an indication of begin-transmission or end-transmission?

## Setup

Make a new directory called `ex_069`. You'll want this because we'll be creating a few files.

Create a new flowgraph, and save it in that directory with the name `morse_demo_1.grc`.

Create this flowgraph:
```
Vector 
Source  ->  Python Block  ->  Vector to   ->  Virtual Sink
                              Stream      ->  Repeat ->  UChar to 
                                                         Float  -> Time 
                                                                   Sink
                                               
```

- Vector source:
  - Output type: byte
  - Vector: [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
  - Repeat: Yes
- Python block:
  - _First, you'll need to do the v4 method setup described in an earlier exercise. Then, type the following in the blanks:_
  - Func_to_use: "my_gnuradio_custom_python_helpers.modulate_morseish"  
     _with quotes_
  - State Var 1: 0
  - State Var 2: 0
  - State Var 3: 0
- Vector to stream:
  - IO Type: byte
  - Num Items: 4
  - Vec Length: 1
- Repeat:
  - Type: byte
  - Interp: 10
- Time Sink:
  - Type: Float
  - Number of points: 200 

Also, in `my_gnuradio_custom_python_helpers.py` (which you created in an earlier exercise), put this:

```python3
def modulate_morseish(datapoint, state_container):
    if datapoint == 0:
        return [1, 0, 0, 0]
    elif datapoint == 1:
        return [1, 1, 1, 0]
    else:
        print("ERROR")
``` 

We're going to try varying the repeat interpolation.

Then, we'll make the receiver.

## Morse-ish receiver

Discuss: How to demod? Describe algorithm, then discuss Python.

```
{ This part is from before }
Vector 
Source  ->  Run Python  
            Function v4  ->  Vector to
                           Stream    ->  Virtual Sink

{ This part is new }
Virtual Source -> Stream to Vec -> Run Python Function v4  ->  Throttle  -> Pack K bits -> File Sink
```

- Virtual sink:
  - Id: pretend_tx_rx
- Virtual source:
  - Id: pretend_tx_rx
- Stream to Vec:
  - Byte
  - 4
  - 1
- Run Python Function v4 (the first one)
  - No change from before.
- Run Python Function v4 (the second one)
  - Func_to_use: "my_gnuradio_custom_python_helpers.demod_morseish"  
     _with quotes_
- Pack K Bits:
  - K: 8

You'll also have to open the code on the second Run Python Function block, and (carefully) swap the in sig and out sig:  

```python3
## Before:
name='Run Python Function v4',
in_sig=[(np.uint8, 1)],
out_sig=[(np.uint8, 4)]

## After:
name='Run Python Function v4',
in_sig=[(np.uint8, 4)],
out_sig=[(np.uint8, 1)]
```

In the aforementioned python file (`my_gnuradio_custom_python_helpers.py`), add this (keep your other function too):

```python3
def demod_morseish(chunk, state_container):
    if chunk.tolist() == [1, 0, 0, 0]:
        return 0
    elif chunk.tolist() == [1, 1, 1, 0]:
        return 1
    else:
        print("Invalid sequence detected. Treating as no data.")
        return None
```

Finally, I recommend changing the names of the custom python blocks to "Run Python: modulate_morseish" and "Run Python: demod_morseish".  To do this, double click on each block to open its Properties window.  In the Code field, press "Open in Editor" again.  Locate the line that starts as, "name=" and replace the current name with the suggested name.


### Average 

Adding fake noise:

```
        (original)          (diff position)  (new)        (new)    (original)
... ->  Vector to Stream  -> Repeat ->    UChar to Float ->  Add  ->  Virtual Sink
                                         Noise Source   ->
                                         (new)
             

(original)          (new)              (new)            (new)        (original)
Virtual Source  ->  Moving Average  -> Keep 1 in N  -> Binary Slicer -> Stream to Vec 
```

- Noise Source:
  - Type: Float
- Add:
  - Type: Float
- Moving Average:
  - Type: Float
- 


```python3
def my_average(chunk, state_container):
    return np.average(chunk)
```

### Slice

```python3
def my_binary_slice(chunk, state_container):
    # will need to experiment with the threshold
    # after experimenting with the AGC
    thresh = state_container["state_var_1"]
    if avg > thresh:  
        return 1
    else:
        return 0
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

### Improved demod given fuzzy symbol length

```python3
def demod_morseish(chunk, state_container):
    s = sum(chunk)
    
    ## We'll have to experiment with this too.
    thresh = state_container["state_var_1"]
    
    if s > thresh:
        return 1
    elif s > thresh / 3:
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
