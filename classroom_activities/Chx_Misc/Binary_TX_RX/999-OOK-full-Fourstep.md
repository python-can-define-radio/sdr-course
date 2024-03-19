_Note: This exersise is fairly complicated. Feel free to skip it._

# Transmitting side:

## First, write the file. Call this `filewriter.py`.

```python3
f = open("myfile.txt", "wb")

# At the beginning of the file, this code writes three special characters: 128, 32, 32.
# Here's why:
#   128:    in binary, this is 10000000, which is chosen because it is
#           easy to notice on the receiving end.
#   32:     this is the ASCII code for "space".
#   32:     this is the ASCII code for "space".
f.write(bytes([128, 32, 32]))
f.write("Put your words here".encode("ascii"))
f.close()
```

Once you have finished making that python file, run it. It will create a text file called `myfile.txt`.

## Second, we'll be using GNU Radio. Call this `filesender.grc`.

```
File Source  -->  Unpack K Bits  -->  Repeat  -->  (Continued below)

(Continued from above) -->  UChar to Float  -->  Float to Complex  -->  Rational Resampler  -->  Osmocom Sink
                                                 (the "re" port)                            -->  Time Sink

```

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- File Source:
  - File: _Pick the `myfile.txt` that you created. Don't just type `myfile.txt`. Also, don't pick a `.py` file or a `.grc` file._
- Unpack K Bits:
  - K: `8`
- Repeat:
  - Interpolation: `500`
- Float to Complex:
  - _Ensure you have the `re` port connected, not the `im` port._
- Rational Resampler:
  - Interpolation: `int(samp_rate / 10)`
  - Decimation: `500`
- Osmocom Sink:
  - Sample Rate: `samp_rate`
  - Ch0: Frequency (Hz): _Pick something_
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BB Gain (dB): `0`
- Time Sink:
  - Number of points: `int(samp_rate)`


# Receiving Side

## Call this `filereceiver.grc`.

You'll need this to be running before you start the file sender so that it receives the entirety of the message.

```
                                       -->  Waterfall Sink
Osmocom Source  -->  Band Pass Filter  -->  Complex to Mag  -->  Moving Average  -->  (Continued below)

                      
                      
(Continued from above) --> Rational Resampler  -->  File Sink
                                               -->  Time Sink
```

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Osmocom Source:
  - Ch0: Frequency (Hz): _Tune to 250 kHz below your transmit freq._
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BB Gain (dB): `32`
- Band Pass Filter:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cutoff Freq: `200e3`
  - High Cutoff Freq: `300e3`
  - Transition Width: `100e3`
- Moving Average:
  - Length: `2000`
- Rational Resampler:
  - Interpolation: `1`
  - Decimation: `100`
- File Sink:
  - File: _Pick a NEW, NOT YET EXISTING FILE. If it asks you if you want to replace the file, DO NOT PRESS YES._
- Time Sink:
  - Number of points: `8192`
  - Sample Rate: `samp_rate / 100`


## Call this `process_received.py`.

```python3
import numpy as np
import matplotlib.pyplot as plt
from math import ceil


def withoutLeadingZeros(arry):
    # first nonzero position
    dataStart = arry.nonzero()[0][0]
    return arry[dataStart:]


def splitIntoGroups(arry, groupSize):
    return np.array_split(arry, ceil(len(arry) / groupSize))

def verifyFirstGroup(groups):
    firstGroup = groups[0]
    boolArray = (firstGroup == [1, 0, 0, 0, 0, 0, 0, 0])
    if not all(boolArray):
        raise ValueError("The first byte must be [1, 0, 0, 0, 0, 0, 0, 0], but it wasn't. Ask an instructor for help.")


dat = np.fromfile("binaryReceived.data",
                  dtype=np.float32)

# If it's greater than the threshold, make it a 1,
# else, make it a zero.
aboveBelow = dat > 50

# Grab every nth
decimated = aboveBelow[::2000]

intified = decimated.astype(np.int)

realData = withoutLeadingZeros(intified)

groupsOf8 = splitIntoGroups(realData, 8)

verifyFirstGroup(groupsOf8)

for g8 in groupsOf8:
    packed = np.packbits(g8)
    packedNotInArray = packed[0]
    aschr = chr(packedNotInArray)
    print(aschr, end="")


```
