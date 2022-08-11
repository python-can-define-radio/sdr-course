In Python:

```python3
import numpy as np

somedata = np.array([64, 20, 30.5, -20.6])

print("Writing to file...")
outfile = open("mysig.stuff", "wb")
outfile.write(somedata.astype(np.float32).tobytes())
outfile.close()
```

This will create a file.

You'll then read that file in GNU Radio:

```
File Source  ->  Throttle  ->  Time Sink
```

### For the File Source:

- File: Pick the file you created.

