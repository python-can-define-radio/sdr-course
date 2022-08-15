# Transmitting side:

## First, write the file. Call this `filewriter.py`.

```python3
f = open("myfile.txt", "wb")

# At the beginning of the file, write three special characters:
# 128:    in binary, this is 10000000, which is easy to notice on the receiving end.
# 32, 32:  this is the ASCII code for "space".
f.write(bytes([128, 32, 32]))
f.write(bytes("Put your words here"))
f.close()
```

## Second, send it with GNU Radio. Call this `filesender.grc`.

```
File Source  -->  Unpack K Bits  -->  Repeat  -->  (Continued below)

(Continued from above) -->  UChar to Float  -->  Float to Complex  -->  Rational Resampler  -->  Osmocom Sink
                                                 (the "re" port)                            -->  Time Sink

```

Parameters:

- File Source:
  - File: Pick the `myfile.txt` that you created. Don't just type `myfile.txt`.
- Unpack K Bits:
  - K: `8`
- Repeat:
  - Interpolation: 500
- Float to Complex:
  - _Ensure you have the `re` port connected, not the `im` port.
- Rational Resampler:
  - Interpolation: `int(samp_rate)`
  - Decimation: 500
- Osmocom Sink:
  - Sample Rate: `samp_rate`
  - Ch0: Frequency (Hz): _Pick something_
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `32`
  - Ch0: BF Gain (dB): `0`


# Receiving Side

## Call this `filereceiver.grc`.

You'll need this to be running before you start the file sender so that it receives the entirety of the message.

```
                                       -->  Waterfall Sink
Osmocom Source  -->  Band Pass Filter  -->  Complex to Mag  -->  Moving Average  -->  (Continued below)

                      
                      
(Continued from above) --> Rational Resampler  -->  File Sink
                                               -->  Time Sink
```
