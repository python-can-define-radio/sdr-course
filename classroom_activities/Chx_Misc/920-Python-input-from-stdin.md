If it's text, you can just use `input()`. Example:

```python
## this file is called dostuff.py.
firstline = input()
secondline = input()
print("first:", firstline)
print("second:", secondline)
```

Then run  
`cat fileWithTwoLines.txt > python3 dostuff.py`

## Binary:

Here's how to create some binary data in python:
```python
## bincreator.py
with open("mystuff.bindata", "wb") as f:
    f.write(bytes(range(65,150)))

```

And to read it:
```python
## readbin.py
import sys
data = sys.stdin.buffer.read()
print(repr(data))
```

To test:

- Create the binary data: `python3 bincreator.py`
- Pipe it: `cat mystuff.bindata | python3 readbin.py`