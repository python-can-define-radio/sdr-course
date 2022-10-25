_Note: This exercise isn't finished, but it has some useful parts._

```python3
import numpy as np

## This is the "Integer 8" type in GNU Radio (Purple color).
## It's also called UChar.
outfile = open("mysig.stuff", "wb")
outfile.write(bytes([65, 66, 70]))
outfile.close()

## This is ALSO the "Integer 8" type in GNU Radio (Purple color)
outfile = open("mysig.stuff", "wb")
outfile.write(np.uint8(np.array([65, 66, 70])))
outfile.close()

## This is the "Float 32" type in GNU Radio (Orange color)
outfile = open("mysig.stuff", "wb")
outfile.write(np.float32(np.array([65, 66, 70])))
outfile.close()

## This is the "Complex Float 32" type in GNU Radio (Blue color)
## Notice that the name in Numpy has 64; this is because
##  complex data has a real and an imaginary part, 32 bits each
outfile = open("mysig.stuff", "wb")
outfile.write(np.complex64(np.array([65, 66, 70])))
outfile.close()
```
