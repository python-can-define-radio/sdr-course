<!-- pandoc-only % SDR: Transmitting -->

# GRC FM Transmitter  <!-- pandoc-exclude-line -->

<!-- pandoc-only ### Purpose -->
### Summary  <!-- pandoc-exclude-line -->

GNU Radio Companion (GRC) is an SDR program that can transmit, receive, view, and demodulate signals. This lesson provides basic familiarity with GRC.

<!-- pandoc-only ### Outcome -->

<!-- pandoc-only By the end of this lesson, students will be able to: -->  
<!-- pandoc-only - Launch GRC -->  
<!-- pandoc-only - Configure flowgraph parameters in GRC -->  
<!-- pandoc-only - Transmit FM Radio using GRC -->

<!-- pandoc-only ### Learning Step Activities -->

<!-- pandoc-only - LSA 1: Launch GRC -->  
<!-- pandoc-only - LSA 2: Configure flowgraph parameters in GRC -->  
<!-- pandoc-only - LSA 3: Transmit FM Radio using GRC -->

# <!-- pandoc-only LSA 1: --> Launch GRC

### Disclaimer

Broadcasting without a license is illegal in most countries. This should only be used for research purposes in an environment that is sufficiently radio-shielded from other electronics.

### Flowgraph Diagram

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

# <!-- pandoc-only LSA 2: --> Configure flowgraph parameters in GRC

### Parameters

<!-- pandoc-only ::: notes -->

<!-- pandoc-only sample rate variable is already in the flowgraph -->

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
    - _NOTE: You can use a Audio Source instead if you'd like. See notes at the bottom of this page._
    - File: Pick a file by pressing the "..." button. It must be a wav file, not an mp3, etc. You can find wav files [here](https://github.com/adafruit/Adafruit-Sound-Samples/tree/master/sonic-pi).
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

- Using an `Audio Source` block allows you to use a microphone.  
    - `Audio Source -> Device Name -> empty`
    - `Audio Source -> Sample Rate -> 48000`
    - `Rational Resampler -> Decimation -> 48000`
- You can also use an `Audio Source` block to broadcast whatever is currently playing on your computer.
    - Do the setup described on the [GNU Radio Wiki](https://wiki.gnuradio.org/index.php?title=ALSAPulseAudio#Monitoring_the_audio_input_of_your_system_with_PulseAudio).
    - `Audio Source -> Device Name -> "pulse_monitor"`
    - `Audio Source -> sample rate -> 48000`
    - `Rational Resampler -> Decimation -> 48000`
