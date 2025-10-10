# SDR: Transmitting

<!--
Note regarding what goes in the quad chart:

Action: Discuss the fundamentals of Software Defined Radios (SDRs).
Standard: Students will be able to explain fundamentals of SDRs.


Evaluation: Check on Learning
-->

<!-- pandoc-only ### Purpose -->
### Summary  <!-- pandoc-exclude-line -->

GNU Radio Companion (GRC) is an SDR program that can transmit, receive, view, and demodulate signals. This lesson provides basic familiarity with GRC.

<!-- pandoc-only ### Outcome -->

<!-- pandoc-only By the end of this lesson, students will be able to: -->  
<!-- pandoc-only - Launch the software -->  
<!-- pandoc-only - Configure flowgraph parameters for transmission -->  

<!-- pandoc-only ### Learning Step Activities -->

<!-- pandoc-only - LSA 1: Launch the software -->  
<!-- pandoc-only - LSA 2: Configure flowgraph parameters for transmission -->  

# <!-- pandoc-only LSA 1: --> Launch the software

### Disclaimer

Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

The hardware which we use is sufficiently low power to not interfere with transmissions outside the classroom.

### What is GNU Radio?

"GNU Radio is a free & open-source software development toolkit ... to implement software radios. It can be used with readily-available low-cost external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in research, industry, academia, government, and hobbyist environments to support both wireless communications research and real-world radio systems."  
_(Source: gnuradio.org/about)_

### What is GNU Radio Companion?

GNU Radio Companion (GRC) is the Graphical User Interface (GUI) that we'll be using to build GNU Radio programs, which are called Flowgraphs.

- GRC generates Python code that is executed to control the radio hardware.
- It's possible to use GNU Radio by writing Python code directly, but the GRC GUI is used more often in the SDR community.

### How to use GRC

When using GRC, this is the usual workflow:

1. Find blocks using Ctrl + F
2. Connect blocks by clicking on the in and out ports
3. Adjust parameters by double-clicking blocks

For practice, you may try the "Your First Flowgraph" tutorial found here: https://wiki.gnuradio.org/index.php/Tutorials

### GRC Flowgraph for an FM Transmitter

Build this in GRC:

```
GUI Range
WFS -> RR -> WBFM T -> Os S
                    -> WS
```
&nbsp;  
WFS = Wav File Source  
RR = Rational Resampler  
WBFM T = WBFM Transmit  
Os S = Osmocom sink  
WS = Waterfall sink

# <!-- pandoc-only LSA 2: --> Configure flowgraph parameters

### Parameters

<!-- pandoc-only ::: notes -->

Note: the samp_rate variable is already in the flowgraph.

<!-- pandoc-only ::: -->

- `samp_rate` variable 
    - Value: `2e6`

- GUI Range:
    - Id: `center_freq_slider`
    - Default Value: `98.5e6`
    - Start: `88e6`
    - Stop: `108e6`
    - Step: `10e3`

<!-- pandoc-only ### Parameters -->

- Wav File Source:
    - _NOTE: You can use a Audio Source instead if you'd like. See endnotes._
    - File: Pick a file by pressing the "..." button. It must be a wav file (not an mp3, etc). You can find wav files [here](https://github.com/adafruit/Adafruit-Sound-Samples/tree/master/sonic-pi).
    - Repeat: Up to you; do you want it to repeat?

<!-- pandoc-only ### Parameters -->

- Rational Resampler:
    - Type: `Float -> Float (Real Taps)`
    - Interpolation: `int(samp_rate)`
    - Decimation: This should match the sample rate that you'll find in the properties of the wav file. If you can't find the sample rate, put `int(60e3)` (which is 60000 Hz, or 60 kHz). The song will probably play too fast; adjust to make the song sound normal. 

- Waterfall Sink:
    - Leave all as defaults.

<!-- pandoc-only ### Parameters -->

- WBFM Transmit:
    - Audio Rate: `int(samp_rate)`
    - Quadrature Rate: `int(samp_rate)`

- Osmocom Sink:
    - Device Arguments: `"hackrf=0"`
    - Ch0: Frequency (Hz): `center_freq_slider`
    - Ch0: RF Gain (dB): `0`
    - Ch0: IF Gain (dB): `32`
    - Ch0: BB Gain (dB): `0`


### Discussion

- Try different audio files, different IF Gains, and different broadcast frequencies.

### Using an Audio Source

You can replace the Wav File Source with an Audio Source in order to...

- Transmit from a microphone
- Transmit the audio that your computer is playing

### Transmitting from the microphone

- Audio Source:
    - Device Name: ""
    - Sample Rate: 48000
- Rational Resampler:
    - Decimation: 48000

### Transmitting what the computer is playing

- First, do the setup described on the [GNU Radio Wiki](https://wiki.gnuradio.org/index.php?title=ALSAPulseAudio#Monitoring_the_audio_input_of_your_system_with_PulseAudio).
- Then, set these parameters:
    - Audio Source:
        - Device Name: "pulse_monitor"
        - Sample Rate: 48000
    - Rational Resampler:
        - Decimation: 48000

<!-- pandoc-only ### Summary -->

<!-- pandoc-only In summary, you learned: -->

<!-- pandoc-only - How to launch the software -->  
<!-- pandoc-only - How to configure flowgraph parameters for transmission -->  

<!-- pandoc-only ### References -->

<!-- pandoc-only - https://wiki.gnuradio.org/index.php/Main_Page -->
