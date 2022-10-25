_Note: This exercise isn't finished, but it has some useful parts._

In Python:

```python3
import numpy as np

somedata = np.array([64, 20, 30.5, -20.6])

print("Writing to file...")
outfile = open("mysig.stuff", "wb")
outfile.write(np.float32(somedata))
outfile.close()
```

This will create a file. You won't be able to open the file directly (not easily, anyway).

Instead, we're going to use a GNU Radio flowgraph to read it, but not directly. In other words, DON'T try to do "Open with GNU Radio". Instead, you'll do this:

Open a new GNU Radio flowgraph. Name it `filereader.grc` (or similar).

```
File Source  ->  Throttle  ->  Time Sink
```

### For the File Source:

- File: Pick the file you created.

### For all of the blocks:

- Change the ports to Orange (float) instead of the default Blue (complex).


------------------------

Once you get that working, change `somedata` to be a wave.

------------------------

Then, try this:

```python3
import numpy as np

somedata = np.array([64 + 50j, 20, 30.5, -20.6])

outfile = open("mysig.stuff", "wb")
outfile.write(np.complex64(somedata))
outfile.close()
```

Change your GNU Radio file to have blue ports (for complex data).

-------------------------

Your goal:

- Create a chunk of data in Python.
- Transmit it from your SDR using GNU Radio.
- Receive it. Verify that the data was sent correctly.
