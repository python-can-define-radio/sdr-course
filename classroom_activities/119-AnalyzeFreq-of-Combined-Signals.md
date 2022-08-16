## Analyze Frequency of Combined Signals/Waves
This is a demonstration of how GNU Radio Companion can evaluate a "complex" signal comprising multiple waveforms (e.g., multiple sine or cosing waves) to determine the frequencies of the multiple waves.

## Summary of the GUI-program

```

GUI Range (1st)

GUI Range (2nd)

Variable  (Optional)

Signal Source (1st) ─┌─⟶  Add ⟶ Throttle ─┌─⟶ QT GUI Frequency Sink 

Signal Source (2nd) ─┴                    ┴⟶ QT GUI Time Sink
                                     

```
Memo: In addtion to the wiring shown above --- After updating the parameters for QT GUI Time Sink, listed below, wire the 1st and 2nd Signal Sources to separate inputs on the QT GUI Time Sink.

Goals:
- Produce two signals, a.k.a. "waves" using the 1st & 2nd Signal Sources and make the frequcnecy of each wave adjustable by including two sliders to pick (adjust) the frequencies you're producing.
- Using the  Multiply block, combine the waves (singals) together to represent a complex waveform that may be received from a piece of local equipment or from broadcast signals.
- Plot the orignal waves and the combined waveform using the Time Sink. 
- Using the Frequency Sink, demonstrate the ability of GNU Radio Companion to analyze the combined waveform, which means extracting (disassociating) and ploting the invidual singals waves that produced the combined waveform.
- (Optional) Use a Variable block to assit with arranging the display blocks on the GUI operation screen.

## How to set the Parameters

### For the First GUI Range:

- Id: `freq1`
- Default Value: `50` Hz
- Start: `0` Hz
- Stop: `5e3`  = 5,000 Hz
- Step: `25`  Hz
- GUI Hint: '(0,0)'  (OPTIONAL. This sets the position of the Range selector on the GUI screen. 1st number is row. 2nd number is the column.)

### For the Second GUI Range:

- Id: `freq2`
- Default Value: `50` Hz
- Start: `0` Hz
- Stop: `5e3`  = 5,000 Hz
- Step: `25`  Hz
- GUI Hint: '(0,1)'  (OPTIONAL. This sets the position of the Range selector on the GUI screen, @ row 0 (1st), col. 1 (2nd))

### For the `samp_rate` variable (Not pictured above):

- Value: `20e3` = 20,000 Hz

### For the Variable block:
(OPTIONAL.  May be used for "GUI Hint" of graphing blocks (sinks) to set their width.)

- Id: 'GUI_width'
- Value: 'int(3)'


 ******** THE CONTENT BELOW THIS LINE NEEDS TO BE EDITTED. ***********
### For the Band Pass Filter:

- FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
- Low Cutoff Freq: `-100e3` (notice the negative)
- High Cutoff Freq: `100e3`
- Transition Width: `100e3`

### For the WBFM Receive:

- Quadrature Rate: `samp_rate`
- Audio Decimation: `1`

### For the Rational Resampler:

- Type: `Float -> Float (Real Taps)`
- Interpolation: `int(48e3)`
- Decimation: `int(samp_rate)`

### For the Audio Sink:

- Sample Rate: `48 kHz` (Pick from drop-down menu)

### For BOTH Waterfall Sinks:

- Leave all as defaults.

### For the Time Sink:

- Leave all as defaults.


## Discussion

- You'll notice that sometimes you need to move the antenna to ensure good reception. Watching the Waterfall can help with seeing how good your reception is.
