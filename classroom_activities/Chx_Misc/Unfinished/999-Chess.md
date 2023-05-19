Transmitter step 1:

```
GUI Chooser


Sig source --> Osmo sink
           --> waterfall sink
```

- samp rate:
  - 2e6
- Chooser:
  - id: freq
  - type: float
  - Num Oprtion: List
  - Options: [0, 100e3, 200e3, 300e3]
  - Labels: ["No choice", "One", "Two", "Three"]
  - Widget: Radio
  - Orien: Horiz
- Sig source:
  - frequency: freq
- osmocom sink:
  - freq: 2.4e9
  - Rf Gain: 0
  - IF : 24
  - BB: 0
