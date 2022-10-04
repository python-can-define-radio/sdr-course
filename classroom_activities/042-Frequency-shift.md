## Transmitting a pure sine wave

Let's say you wanted to transmit a pure frequency (that is, a pure sine wave) of `100.2 MHz`.

You can actually do this without GNU Radio. In the terminal, type

```
osmocom_siggen_nogui --const --tx-freq=100.2e6 --gain=0
```

To see the full list of options, type

```
man osmocom_siggen_nogui
```

This will open the manual for the osmocom signal generator. Press `q` to quit.

## In GNU Radio

(unfinished)

