# Error correction

All data transmissions are subject to error, though the chances of error vary by situation (shouting in a cavernous room vs. normal conversation).

One way to reduce the chance of errors is to use error correction codes. [This video from 3Blue1Brown](https://www.youtube.com/watch?v=X8jsijhllIA) gives a great introduction to error correcting codes, and also describes how to use a Hamming code. Another approach (less common in practice, but great for learning) is [Two dimensional parity](https://thecsemonk.com/two-dimensional-parity/).

## One Dimensional Parity

`OneD_validate.py`

```python3
data = input("What is the binary data?")
numberOfOnes = data.count("1")
## If the data has an even number of ones, it's valid.
remainder = numberOfOnes % 2
if remainder == 0:
    print("Valid")
else:
    print("Invalid")
```

`OneD_create.py`

```python3
data = input("What is the binary data?")
numberOfOnes = data.count("1")

remainder = numberOfOnes % 2
if remainder == 0:
    newdata = data + "0"
else:
    newdata = data + "1"
print(newdata)
```
