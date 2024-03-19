## Transmitting

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
  - RF Gain: `0`
  - IF Gain: `30`
  - BB Gain: `0`

<details><summary> another way to test</summary>
 Vector source: `[170] + list(map(ord, "abcd"))` 
  TODO: explain this more
  </details>

## Receiving

```
          -->  Time Sink (First)
          |
          -->  Waterfall sink
          |
osmocom  --->  OOK Demod  --> Keep after data      --->  Pack K Bits  -->  File Sink
Source                        equals 1 Hier Block   |
                                                    --> UChar to Float  -->  Time Sink
                                                                             (second)
```

Note: You'll need the `Keep after data equals 1 Hier Block` block from [here](https://github.com/python-can-define-radio/sdr-course/blob/main/misc/grc_files/keep_after_data_equals_1_hier_block.grc)

Parameters:
- osmocom Source:
  - _use the same parameters as an osmocom source from a previous flowgraph_
- OOK Demod:
  - Symbol Length: `int(1e6)`
  - Threshold: _make a slider between 0 and 1_
- Pack K Bits:
  - K: `8`
- Time Sink (second):
  - Number of Points: `10`
  - Sample Rate: `2`
- File Sink:
  - File: _pick a NON-EXISTENT file_
  - Unbuffered: `on`


At the beginning of your file, make sure you have a character that starts with a 1 in binary.
You can copy paste this one: "¡"

