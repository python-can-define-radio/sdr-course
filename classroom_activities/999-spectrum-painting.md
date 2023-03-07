Source: https://www.gkbrk.com/2021/02/spectrum-drawing/

Our modified version (with some cruft

```python3
from PIL import Image
import math
import numpy as np

# dsp = os.fdopen(1, "wb")
outfile = open("waterpaint.iqdata", "wb")


def write(i, q):
    # i = int(i * 127)
    # q = int(q * 127)
    # i = int(i * 31)
    # q = int(q * 31)
    ## TODO next time: what type is bb? gnu radio needs to interpret it correctly
    # data = struct.pack("bb", i, q)
    outfile.write(np.complex64(q + 1j*i).tobytes())


RATE = 2000000  # sample rate
TRANSMIT_TIME = 5  # Seconds
FREQ_DEV = 1000000  # Hz

im_raw = Image.open("hi.jpeg")
# im = Image.open(sys.argv[1])
im = im_raw.convert("1")  # 1 means 1-bit image

# for x in range(100, 110):
#     for y in range(100, 110):
#         print(im.getpixel((x, y)), end=" ")
#     print()

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
```
