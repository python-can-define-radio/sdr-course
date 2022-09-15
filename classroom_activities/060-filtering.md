Make a copy of the **receiver** from `025-Transmit-and-Receive-Pure-Sine.md`.

Modify it like so:

```
osmocom Source --->  Band Pass Filter  --->  Time Sink
                                       --->  Waterfall Sink
                                       --->  Frequency Sink
```

Keep all settings the same as your original receiver, except this:

- Band Pass Filter:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cutoff Freq: `50e3`
  - High Cutoff Freq: `100e3`
  - Transition Width: `20e3`                                       
