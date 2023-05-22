<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Mar 07: 999-spectrum-painting.md
2023 May 22: 040_Spectrum_Painting.md
</pre>
</details>

## Frequency Spectrum Painting using Python & Software-Defined Radio (SDR).
See Python program, below, for description.
Page updated April 25, 2023.

### Resources required for full functionality:
```
- Software to run a Python program, 
- "GNU Radio Companion" or equivalent software, 
- One SDR device to transmit (TX), and 
- A second SDR device to receive (RX) signals.  
Optionally, a single SDR device running in TX+RX duplex mode.
```

Source: https://www.gkbrk.com/2021/02/spectrum-drawing/

Our modified version is below. 

After running the program, you'll have a file in your working directory named `waterpaint.iqdata`. You can use GNU Radio Companion to transmit the file using a flowgraph containing `File Source --> osmocom Sink`.

### Python program to create a broadcast-capable data file for spectrum painting:
```python3
"""
This Python3 program reads a black and white .jpg or .jpeg image file and converts it to
   an "iqdata" file, for broadcast (TX) through an SDR such as a HackRF device + GNU Radio Companion (GRC).
   A separte program is required to perform the broadcast in GRC. 
The painted image will be visible on a second SDR in the receiving (RX) mode (or one SDR with duplex TX/RX) 
   with a GRC program having a waterfall display for vieiwing a freqeuncy spectrum.

source: https://github.com/python-can-define-radio/sdr-course/edit/main/classroom_activities/999-spectrum-painting.md
based on https://www.gkbrk.com/2021/02/spectrum-drawing/
"""

from PIL import Image
import math
import numpy as np


in_filename = "hi.jpeg"   # Update this to point to a B&W image stored in JPG or JPEG format.
out_filename = "waterpaint.iqdata"

RATE = 2000000  # sample rate
TRANSMIT_TIME = 5  # Seconds
FREQ_DEV = 1000000  # Hz  The image will extend this many HZ lower than your broadcast's tuned or center frequency.

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

    # Read the line backwards to paint forwards, by including: [::-1] 
    line = [im.getpixel((x, y)) for x in range(im.width)[::-1]]
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

print(f"File '{out_filename}' is ready. You can now transmit the iqdata file using GNU Radio Companion.")
print("Reminder of parameters:")
print(parameters_info)
```
