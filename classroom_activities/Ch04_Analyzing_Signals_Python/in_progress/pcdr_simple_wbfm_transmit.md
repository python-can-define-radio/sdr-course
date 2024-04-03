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
##   https://github.com/adafruit/Adafruit-Sound-Samples/tree/master/sonic-pi
## Note: For the file to play at the proper speed, you must
##  set the audio_sample_rate based on the properties of
##  the wav file. You can view that in a  GUI file browser,
##  or using the `file` terminal command on GNU Linux:
##     file drum_cowbell.wav
##          ^^^^^^^^^^^^^^^^ replace this part with your wav file's name.
## Alternatively, set the audio_sample_rate to 60_000 and
## then adjust based on how it sounds.
import pcdr.simple
import time

player = pcdr.simple.AudioPlayer(
    wavfile="drum_cowbell.wav",
    audio_sample_rate=22050
)
player.start()
player.wait()


## 2
## Try this variation. What is different?
import pcdr.simple
import time

player = pcdr.simple.AudioPlayer(
    wavfile="drum_cowbell.wav",
    audio_sample_rate=22050,
    repeat=True
)
player.start()
time.sleep(3)
player.stop_and_wait()
```

Now, using the hardware:

```
## 3
## Try this.
import pcdr.simple
import time
transmitter = pcdr.simple.OsmosdrWBFMTransmitter(
    "hackrf=0",
    freq=2.45e9,
    wavfile="drum_cowbell.wav",
    repeat=True,
    audio_sample_rate=22050
)
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(10)
transmitter.stop_and_wait()


## 4
## Try changing the transmission frequency by
## changing the 2.45e9 in the above example.


## 5
## Try this. What is different?
import pcdr.simple
import time
transmitter = pcdr.simple.OsmosdrWBFMTransmitter(
    "hackrf=0",
    freq=2.45e9,
    wavfile="drum_cowbell.wav",
    repeat=True,
    audio_sample_rate=22050
)
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(2)
transmitter.set_center_freq(2.4501e9)
time.sleep(2)
transmitter.stop_and_wait()


## 6
## Using Python, do the following:
##  - Set the frequency to an FM broadcast station
##  - Jam it for half a second
##  - Set the frequency to a different FM broadcast station
##  - Jam it for half a second


## 7
## Copy and modify the previous exercise:
##  Loop the actions forever using a `while` loop.


## 8
## Copy and modify the previous example.
## In this version, instead of cycling between the two stations,
## randomly pick every half second.
## Then, try the same exercise with three stations.
```

Now that you've seen how to transmit a `.wav` file, here's how to use the "pulse_monitor" source to transmit whatever is currently playing on your computer.

Note that this method only works on a GNU Linux OS, and only after doing [this configuration](https://wiki.gnuradio.org/index.php?title=ALSAPulseAudio#Monitoring_the_audio_input_of_your_system_with_PulseAudio).

Also, if you have multiple output devices (for example, if you have headphones plugged in), you may have to either unplug the headphones or change your `~/.asoundrc` file.

```python3
## 8
## Try this.
import pcdr.simple
import time
transmitter = pcdr.simple.OsmosdrWBFMTransmitter("hackrf=0", 2.45e9, audio_device="pulse_monitor")
transmitter.start()
transmitter.set_if_gain(37)
time.sleep(1)
transmitter.set_center_freq(2.4501e9)
time.sleep(1)
transmitter.set_center_freq(2.4502e9)

```
