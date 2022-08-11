In Python:

```python3
import numpy as np

somedata = np.array([64, 20, 30.5, -20.6])

print("Writing to file...")
outfile = open("mysig.stuff", "wb")
outfile.write(somedata.astype(np.float32).tobytes())
outfile.close()
```

This will create a file. You won't be able to open the file directly (not easily, anyway).

Instead, we're going to use a GNU Radio flowgraph to read it.

Open a new GNU Radio flowgraph. Name it `filereader.grc` (or similar).

```
File Source  ->  Throttle  ->  Time Sink
```

### For the File Source:

- File: Pick the file you created.

### For all of the blocks:

- Change the ports to Orange (float) instead of the default Blue (complex).

