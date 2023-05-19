_Note: This exercise isn't finished, but it has some useful parts._

## The Python Part:

```python
import numpy as np

myword = "AbC"

## Convert each letter to a number
numberified = list(map(ord, myword))

## Make the list into a numpy array with 
## the type `uint8` (unsigned 8-bit integer)
numpyified = np.array(numberified, dtype=np.uint8)

## Open a file using the "wb" (write bytes) mode
f = open("generatedData.uint8", "wb")

## Write zero at the beginning (this is 8-bits which are all zero)
f.write(bytes([0]))

## Write the actual data
f.write(binarified)

## Write 255 at the end (this is 8-bits that are all 1)
f.write(bytes([255]))

f.close()

```


## The GNU Radio Companion Part:

```
File Source  ⟶  Unpack K Bits  ⟶  UChar to Float  ⟶  Time Sink

```

### For the File Source:

File: `/home/username/wherever/generatedData.uint8` (set this to your actual path to the data file that Python creates)

### For the Unpack K Bits:

K: 8


