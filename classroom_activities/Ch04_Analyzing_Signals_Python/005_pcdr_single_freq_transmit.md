## Disclaimer

Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

## Transmitting on a Single Frequency

This lesson demonstrates the `OsmoSingleFrequencyTransmitter`, which transmits a pure sine wave on a specified frequency. It provides an introduction to methods such as `set_center_freq` which we will use in the Wide-Band-Frequency-Modulator (WBFM).

```python3
## 1
## Try this.
import time
from pcdr.flow import OsmoSingleFreqTransmitter
transmitter = OsmoSingleFreqTransmitter("hackrf=0", 2.45e9)
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(1)
transmitter.set_center_freq(2.4501e9)
time.sleep(1)
transmitter.set_center_freq(2.4502e9)
time.sleep(1)
transmitter.stop_and_wait()


## 2
## Try setting the transmitter to the following frequencies:
##  2.4503 GHz
##  2.4505 GHz
##  2450.4 MHz


## 3
## Try using set_if_gain with a variety of numbers.
## What are the highest and lowest allowable gains?


## 3
## Try changing the sleep time to adjust how long the
## transmitter spends on each frequency.
## You'll notice that stop_and_wait takes a noticeable amount of extra time,
## about 1 second at time of writing.
## We, the authors, do not know a way to quickly
## stop a transmission, but one alternative option
## is to lower the IF gain --
## for example, set_if_gain(0).
## This is not truly OFF, but it makes the
## transmission relatively low power.


## 4
## Try transmitting on top of a commercial FM broadcast.
## How does it impact the broadcast?


## 5
## Using Python, loop the following:
##  - Set the frequency to an FM broadcast station
##  - Jam it for half a second
##  - Set the frequency to a different FM broadcast station
##  - Jam it for half a second


## 6
## Copy and modify the previous example.
## In this version, instead of cycling between the two stations,
## randomly pick one every half second.
## Then, try the same exercise with three stations.
```
