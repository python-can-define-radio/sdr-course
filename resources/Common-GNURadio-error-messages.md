```
File "/..../stuff.py", line 83
    ,
    ^
SyntaxError: invalid syntax
```

Most often, this means that you left a parameter blank that should not be blank. 

**Solution**:

- Open the .py file that is mentioned.
- Look at (or above) the mentioned line to figure out which block is the issue.


------------------------

```
RuntimeError: firdes check failed: 0 < fa <= sampling_freq / 2
```

There are two common causes for this error:
1. Wrong FIR Type
2. Violating Nyquist theorem

