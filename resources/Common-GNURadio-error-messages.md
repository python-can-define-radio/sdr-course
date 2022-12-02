## Expression None is invalid

```
Expression None is invalid for type 'real'.
```

Most often, this means you have a typo in your variable name.

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
2. Violating Nyquist theorem (usually in one of the Filter blocks)

## <=

```
Assertion "start <= value <= stop" failed.
```

In GUI Ranges, the Start and Stop are the left and right limits of the slider. The Default Value is where the slide-piece is placed when the flowgraph runs. 

- The left limit (the "Start") must be the lowest value. 
- The right limit (the "Stop") must be the highest value. 
- The Default Value must be somewhere in between.

## ID `default` is blacklisted

How to fix: Open the `Options` block, and set the Id to something other than default

## "must begin with a letter and may contain letters, numbers, and underscores." 

How to fix: Open the `Options` block, and set the Id to something that satisfies the criteria described. The most common issue is spaces: you may accidentally have a space somewhere in your Id. If you're having trouble finding the culprit characters, you can always erase the Id entirely and type a new Id.
