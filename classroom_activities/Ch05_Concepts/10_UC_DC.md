## Upconversion and Downconversion

### Transmitting a pure sine wave (again)

Let's say you wanted to transmit a pure frequency (that is, a pure sine wave) of `100.2 MHz`.

You can actually do this without GNU Radio. In the terminal, type

```
osmocom_siggen_nogui --const --tx-freq=100.2e6 --gain=0
```

To verify that it is indeed transmitting, ask a classmate to receive this signal using the method of their choice, for example, GQRX. (Incidentally, another way to recieve the signal is using this: `osmocom_fft -W`.)

You'll need to tune the receiver to near the transmitter's frequency. Make sure to tune a little bit above or below the transmit frequency due to the DC spike that is always in the center of the spectrum. (We'll discuss that more later.)

ℹ️ Sidenote: To see the full list of options for either of these commands, type `man osmocom_siggen_nogui` or `man osmocom_fft`. This will open the manual. Press `q` to quit.

## Transmitting in GNU Radio

Now, let's do this in GNU Radio. We know that we'll be sending some sort of **signal** to the Hack RF. We also know that the **osmocom Sink** is used to tell the Hack RF to transmit. So, it would make sense to do  `Signal Source  -->  osmocom Sink`.

Two questions arise:

- What should we pick for the osmocom's center frequency?
- What should we pick for the Signal Source frequency?

It's tempting to set both to `100.2e6`, but that actually won't work. Let's do some experiments to see why.

Reopen the flowgraph `transmit_pure_sine.grc` from exercise `030`. Make the following change:

- osmocom Sink:
  - Ch0: Frequency (Hz): `100e6`

Try sliding the `sigfreq` slider to 200 thousand. You'll see that the frequency you receive is the sum of the two frequencies: `100e6 + 200e3 = 100.2e6`.

This is a fairly important concept. Try a few different combinations of frequencies to make sure you feel comfortable with it. Make sure that in every case, the signal is received at the expected frequency.

## Receiving in GNU Radio

Reopen the flowgraph `receiver.grc` from exercise `030`. Make the following changes:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `8e6`
- osmocom Source:
  - Ch0: Frequency (Hz): `100e6`
  
On a different device, transmit a pure sine wave at 100.2e6 using `osmocom_siggen_nogui`. At what frequency is the wave received? You'll see that it's `0.2e6`, or, equivalently, `200e3`.

Again, this is important. The frequency that is received by the computer is _far lower_ than the waves that were actually in the air. The HackRF (or any other similar device) does _downconversion_ using a _mixer_. We'll be discussing this as a class.

Your task: Practice using different transmit and receive frequency combinations to see what happens.

_Note:_ Unfortunately, you may see more than one spike. Ask an instructor which one is the one you should see.
