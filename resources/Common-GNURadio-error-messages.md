## Expression None is invalid

```
Expression None is invalid for type 'real'.
```

Most often, this means...

- You have a typo in your variable name.
- You used a keyword, such as `if`, as a variable. Variables must not be keywords (`if`, `else`, `while`, etc)

## Expression ... is invalid

```
Expression 200.0 is invalid for type 'int'.
```

If you're using `2e6`, for example, you may need to type `int(2e6)`.

## NameError

```
NameError: name '...' is not defined
```

Also usually a typo.

## Can't open file

```
RuntimeError: can't open file
```

Most often, this means you omitted the `File` in the `File Source` block.

## Syntax error involing a comma

```
File "/..../stuff.py", line 9999
    ,
    ^
SyntaxError: invalid syntax
```

Most often, this means that you left a parameter blank that should not be blank. 

**Solution**:

- Open the .py file that is mentioned.
- Look at (or above) the mentioned line to figure out which block is the issue.

## "Done"

```
>>> Done (return code -11)
```

Usually your HackRF is not plugged in.

## Resource Busy

```
Device or resource busy.
```

Usually you have another program open that is using the HackRF, such as GQRX or another GNU Radio program.

If you don't see anything else open, then press the "Reset" button on the HackRF.

## Firdes check

```
RuntimeError: firdes check failed: 0 < fa <= sampling_freq / 2
```

There are two common causes for this error:
1. Wrong FIR Type (usually in the Band Pass Filter block)
2. Violating Nyquist theorem (usually in one of the Filter blocks).  
   Example: If you have the `samp_rate` set too low, or if you have the `low_cut` or `high_cut` set outside of the allowed boundaries.

## Assertion...

```
Assertion "start <= value <= stop" failed.
```

In GUI Ranges, the Start and Stop are the left and right limits of the slider. The Default Value is where the slide-piece is placed when the flowgraph runs. 

- The left limit (the "Start") must be the lowest value. 
- The right limit (the "Stop") must be the highest value. 
- The Default Value must be somewhere in between.

One common cause is forgetting the `e3`, `e6`, etc. For example:

This is incorrect: Start: `88e6`, Stop: `108e6`, Default Value: `95`  
_Notice: 95 is not between the given start and stop values_  
This is correct: Start: `88e6`, Stop: `108e6`, Default Value: `95e6`


## ID `default` is blacklisted

How to fix: Open the `Options` block, and set the Id to something other than default

## "must begin with a letter and may contain letters, numbers, and underscores." 

How to fix: Open the `Options` block, and set the Id to something that satisfies the criteria described.  
For example:

- `my cool flowgraph` won't work because it has spaces. You could change it to `my_cool_flowgraph` or `mycoolflowgraph` or similar.
- `my-cool-flowgraph` won't work because of the hyphens.
- `030_flowgraph` won't work because it starts with a number. You could change it to `exercise_030_flowgraph` or `my030` or similar.
- `my_flowgraph ` won't work because it ends with a space. Those are especially hard to see!
- `my_flowgraph.grc` won't work because it has a period in it. Simply remove the ".grc" part in the Id.

If you're having trouble finding the culprit characters, you can always erase the Id entirely and type a new Id.

## Topology

```
RuntimeError: check topology failed on time_sink_f(1) using ninputs=1, noutputs=0
```

This means the Time Sink has more available inputs than incoming data. For example, this error will occur if your time sink has three input ports, but only one is connected.

On our exercises, we used text-based diagrams to express the flowgraphs due to time constraints, so in some cases, we couldn't express all of the connecting arrows. We indicated any missing connection-arrows in the "Memos" section of each exercise.
