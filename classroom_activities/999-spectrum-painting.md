Source: https://www.gkbrk.com/2021/02/spectrum-drawing/

Our modified version is below. 

After running the program, you'll have a file named `waterpaint.iqdata`. You can use GNU Radio to transmit the file using a flowgraph containing `File Source --> osmocom Sink`.


```python3
from PIL import Image
import math
import numpy as np


in_filename = "hi.jpeg"
out_filename = "waterpaint.iqdata"

RATE = 2000000  # sample rate
TRANSMIT_TIME = 5  # Seconds
FREQ_DEV = 1000000  # Hz

parameters_info = f"""
Sample rate: {RATE} samples per second
Time for one full picture transmission: {TRANSMIT_TIME} seconds
Bandwidth of transmission: {FREQ_DEV} Hz
"""


def write(i, q):
    # i = int(i * 127)
    # q = int(q * 127)
    # i = int(i * 31)
    # q = int(q * 31)
    ## TODO next time: what type is bb? gnu radio needs to interpret it correctly
    # data = struct.pack("bb", i, q)
    outfile.write(np.complex64(q + 1j*i).tobytes())


outfile = open(out_filename, "wb")
im_raw = Image.open(in_filename)
im = im_raw.convert("1")  # 1 means 1-bit image


print(f"Generating '{out_filename}' with these parameters:")
print(parameters_info)
print("Progress countdown starting now.")

t = 0

## y loops backwards (presumably because we want to transmit
##  the bottom of the image first)
for y in range(im.height)[::-1]:
    print(y)
    target = t + TRANSMIT_TIME / im.height

    line = [im.getpixel((x, y)) for x in range(im.width)]
    while t < target:
        i = 0
        q = 0

        for x, pix in enumerate(line):
            if not pix:
                continue
            offs = x / im.width
            offs *= FREQ_DEV
            i += math.cos(2 * math.pi * offs * t) * 0.01
            q += math.sin(2 * math.pi * offs * t) * 0.01
        write(i, q)
        t += 1.0 / RATE

print(f"File '{out_filename}' is ready. You can now transmit the iqdata file using GNU Radio.")
print("Reminder of parameters:")
print(parameters_info)
```
