# Transmitting side:

First, write the file:

```python3
f = open("myfile.txt", "wb")

# At the beginning of the file, write three special characters:
# 128:    in binary, this is 10000000, which is easy to notice on the receiving end.
# 32, 32:  this is the ASCII code for "space".
f.write(bytes([128, 32, 32]))
f.write(bytes("Put your words here"))
f.close()
```

Second, send it with GNU Radio:

```
File Source  -->  Unpack K Bits  -->  Repeat  -->  (Continued below)

(Continued from above) -->  UChar to Float  -->  Float to Complex  -->  Rational Resampler  -->  Osmocom Sink
                                                 (the "re" port)                            -->  Time Sink

```


