Filename: `OOK_file_source.grc`

```
File  -->  Unpack K  -->  UChar to  --->  OOK Mod  -->  osmocom Sink
Source     Bits           Float      |
                                     |
                                     -->  Time Sink
```

Parameters:

- File Source:
  - File: _Pick your file using the "..."_
  - Output Type: `Byte`
  - Repeat: `No`
- Unpack K Bits:
  - K: `8`
- OOK Mod:
  - Sample Rate: `samp_rate`
  - Symbol Length: `int(1e6)`
- osmocom Sink:
  - Ch0 Frequency (Hz): `2.4e9`
  - Ch0 Frequency Correction: `0`
  - RF Gain: `0`
  - IF Gain: `30`
  - BB Gain: `0`







Ignore this part for now: 

Other notes:

Vector source: `[170] + list(map(ord, "abcd"))`

Unpack K bits 8
