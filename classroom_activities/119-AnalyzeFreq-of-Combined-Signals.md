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
Memos: 
- In addtion to the wiring shown above --- After updating the parameters for QT GUI Time Sink, listed below, wire the 1st and 2nd Signal Sources to separate inputs on the QT GUI Time Sink.
- All ports are be for floating point numbers, i.e., the type "float", which will be orange in color.

Goals:
- Produce two signals, a.k.a. "waves" using the 1st & 2nd Signal Sources and make the frequcnecy of each wave adjustable by including two sliders to pick (adjust) the frequencies you're producing.
- Using the  Multiply block, combine the waves (singals) together to represent a complex waveform that may be received from a piece of local equipment or from broadcast signals.
- Plot the orignal waves and the combined waveform using the Time Sink. 
- Using the Frequency Sink, demonstrate the ability of GNU Radio Companion to analyze the combined waveform, which means extracting (disassociating) and ploting the invidual singals waves that produced the combined waveform.
- (Optional) Use a Variable block to assit with arranging the display blocks on the GUI operation screen.

## How to set the Parameters
Enter the values shown in the bubbles below.  Do not enter the units, e.g., "Hz".  For any parameter not listed, the pre-programmed default value may be used.

### For the First GUI Range:

- Id: `freq1`
- Default Value: `50` Hz
- Start: `0` Hz
- Stop: `5e3`  = 5,000 Hz
- Step: `25`  Hz
- GUI Hint: `(0,0)`  (OPTIONAL. This sets the position of the Range selector on the GUI screen. 1st number is row. 2nd number is the column.)

### For the Second GUI Range:

- Id: `freq2`
- Default Value: `50` Hz
- Start: `0` Hz
- Stop: `5e3`  = 5,000 Hz
- Step: `25`  Hz
- GUI Hint: `(0,1)`  (OPTIONAL. This sets the position of the Range selector on the GUI screen, @ row 0 (1st), col. 1 (2nd))

### For the `samp_rate` variable (Not pictured above):

- Value: `20e3` = 20,000 Hz  
Later, vary this sampling rate  if you want to see more or less data, but remember the Nyquist criteria. Nyquist requires: samp_rate >= 2 * freq1 AND samp_rate >= 2 * freq2)

### For the Variable block:
(OPTIONAL.  May be used for "GUI Hint" of graphing blocks (sinks) to set their width.)

- Id: `GUI_width`
- Value: `int(3)`

### For the Add block:
Use the defalut values, which are shown here.
- IO Type: `Float`
- Num Inputs: `2`
- Vec Length: `1`  

### For the Throttle block:
- No adjustment is need, use default parameters.

### For GUI Frequency Sink (Graph):

- Name: `"Frequency Spectrum from the Added Waves"`
- Y min = `-90` (Note the negative.  This setting crops the lower portion of the data to hide the "noise" in the frequencies)
- Y min = `10`  (10 = The default)
- GUI Hint: `(5,0,2,GUI_width)`  (OPTIONAL. This sets the position on the GUI screen, @ row 5, col. 0, width or span. If row 3 or 4 does not exist, the block will fill a position higher than row 5.)

### For the Time Sink:

"General" Tab
- Autoscale: `Yes`
- Number of Inputs: `3`
- GUI Hint: `(3,0,2,GUI_width)`  (OPTIONAL)
"Trigger" Tab
- Trigger Mode: `Auto`  (This will give the graph the appearance of being "frozen" even as data continues to be fed to it.)

## Discussion

- _______
