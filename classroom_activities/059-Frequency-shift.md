## Transmitting a pure sine wave

Let's say you wanted to transmit a pure frequency (that is, a pure sine wave) of `100.2 MHz`.

You can actually do this without GNU Radio. In the terminal, type

```
osmocom_siggen_nogui --const --tx-freq=100.2e6 --gain=0
```

Ask a classmate to receive this signal to verify that it is indeed transmitting.

To see the full list of options, type

```
man osmocom_siggen_nogui
```

This will open the manual for the osmocom signal generator. Press `q` to quit.

## In GNU Radio

Now, let's do this in GNU Radio. We know that we'll be sending some sort of **signal** to the Hack RF. We also know that the **osmocom Sink** is used to tell the Hack RF to transmit. So, it would make sense to do  `Signal Source  -->  osmocom Sink`.

Two questions arise:

- What should we pick for the osmocom's center frequency?
- What should we pick for the Signal Source frequency?

It's tempting to set both to `100.2e6`, but that actually won't work. Let's do some experiments to see why.

Reopen the flowgraph `transmit_pure_sine.grc` from exercise `030`. Make the following change:

- osmocom Sink:
  - Ch0: Frequency (Hz): `100e6`

Try sliding the `sigfreq` slider to 200 thousand. You'll see that the frequency you receive is the sum of the two frequencies: `100e6 + 200e3 = 100.2e6`.

Try a few different combinations of frequencies to make sure you feel solid about the concept.