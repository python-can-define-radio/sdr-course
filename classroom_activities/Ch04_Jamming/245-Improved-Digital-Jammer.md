This digital jammer is more effective than the original because it can match the symbol rate of the target.

```

GUI Range

Constellation Object

Variable


Random source  ⟶  Constellation  ⟶  Rational     ⟶  Osmocom sink
                  modulator         Resampler    ⟶  Waterfall sink
                                                 ⟶  Time sink
```

- Variable `samp_rate`: Same as usual
- Variable (a new variable block):
  - Id: `symbol_rate`
  - Value: `100e3`
- Rational Resampler:
  - Interpolation: `int(samp_rate)`
  - Decimation: `int(symbol_rate)`
- Time Sink:
  - Y min: `-2`
  - Y max: `2`
- All other parameters:
  - Same as the normal digital jammer.
