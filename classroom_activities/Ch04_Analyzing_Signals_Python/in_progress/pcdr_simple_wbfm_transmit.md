## Disclaimer

Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## WBFM Transmitting

This lesson shows how to use the pcdr module to transmit Wide-Band-Frequency-Modulated audio.

However, before we use the SDR hardware, let's verify that we can play an audio file locally.

```python3
## 1
## Try this. It will play audio locally.
## You must provide a wav file.
## One possible wav file is drum_cowbell.wav from here:
## https://github.com/adafruit/Adafruit-Sound-Samples/tree/master/sonic-pi
import pcdr.simple
TODO


## 2
import pcdr.simple
import time
transmitter = pcdr.simple.OsmosdrWBFMTransmitter("hackrf=0", 2.45e9)
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(10)
transmitter.stop_and_wait()


## 2
## Try setting the frequency to a commercial FM broadcast.
## How does it impact the broadcast?


## 3
## Try this.
## You'll still need the imports from above.
transmitter = pcdr.simple.OsmosdrWBFMTransmitter("hackrf=0", 2.45e9, "pulse_monitor")
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(1)
transmitter.set_center_freq(2.4501e9)
time.sleep(1)
transmitter.set_center_freq(2.4502e9)

## 4
## Using Python, loop the following:
##  - Set the frequency to an FM broadcast station
##  - Jam it for half a second
##  - Set the frequency to a different FM broadcast station
##  - Jam it for half a second




## 5
## Copy and modify the previous example.
## In this version, instead of cycling between the two stations,
## randomly pick every half second.
## Then, try the same exercise with three stations.
```
