_Disclaimer_: Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Python Control

At this point, we've seen multiple ways to use GUI controls (Range, Button, etc) to adjust parameters (Frequency, Gain, etc). How could you automate this using Python?

### A basic example

To start, we'll use a flowgraph that just transmits a pure sine wave.

```
Constant Source  -->  osmocom Sink
```

(Rest of steps are described here: https://github.com/python-can-define-radio/sdr-course/tree/main/misc/gnu_python_integration/constant_source_to_osmo_sink )
