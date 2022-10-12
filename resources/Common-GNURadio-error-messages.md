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

## Firdes check

```
RuntimeError: firdes check failed: 0 < fa <= sampling_freq / 2
```

There are two common causes for this error:
1. Wrong FIR Type (usually in the Band Pass Filter block)
2. Violating Nyquist theorem (usually in one of the Filter blocks)

## ID `default` is blacklisted

How to fix: Open the `Options` block, and set the Id to something other than default

## "must begin with a letter and may contain letters, numbers, and underscores." 

How to fix: Open the `Options` block, and set the Id to something that satisfies the criteria described. The most common issue is spaces: you may accidentally have a space somewhere in your Id. If you're having trouble finding the culprit characters, you can always erase the Id entirely and type a new Id.
