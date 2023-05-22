<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 12: 119-AnalyzeFreq-of-Combined-Signals.md
2022 Aug 30: 219-AnalyzeFreq-of-Combined-Signals.md
2023 May 22: 030_AnalyzeFreq_of_Combined_Signals.md
</pre>
</details>

## Analyze Frequency of Combined Signals/Waves
This is a demonstration of how GNU Radio Companion can evaluate a signal comprising multiple waveforms (e.g., multiple sine or cosine waves) to determine the frequencies of the individual waves.

## Summary of the GUI-program

```

GUI Range (1st)

GUI Range (2nd)

Variable

Signal Source (1st) ─┌─⟶  Add ⟶ Throttle ─┌─⟶ QT GUI Frequency Sink 

Signal Source (2nd) ─┴                    ┴⟶ QT GUI Time Sink
                                     

```
Memos: 
- In addition to the wiring shown above --- After updating the parameters for QT GUI Time Sink, listed below, wire the 1st and 2nd Signal Sources to separate inputs on the QT GUI Time Sink.
- All ports should be floating point numbers, i.e., the type "float", which will be orange in color.

Goals:
- Produce two signals, a.k.a. "waves" using the 1st & 2nd Signal Sources and make the frequency of each wave adjustable by including two sliders to pick (adjust) the frequencies you're producing.
- Using the Add block, combine the waves (signals) together to represent a combined waveform that may be received from a piece of local equipment or from broadcast signals.
- Plot the orignal waves and the combined waveform using the Time Sink. 
- Using the Frequency Sink, demonstrate the ability of GNU Radio Companion to analyze the combined waveform, which means extracting (disassociating) and ploting the individual waves that produced the combined waveform.
- Use a Variable block to assist with arranging the display blocks on the GUI operation screen.

## How to set the Parameters
Enter the values shown in the bubbles below.  Do not enter the units, e.g., "Hz".  For any parameter not listed, the pre-programmed default value may be used.

### For the `samp_rate` variable (_already in the flowgraph_):

- Value: `20e3` = 20,000 Hz  
Later, try varying this sampling rate and watch the maximum x-value on the GUI Frequency Sink graph.  You will need to stop and restart the GUI.  What is the relationship is between the `samp_rate` parameter an the max. x-value?  Why did the programmers establish that relationship?

### For the First GUI Range selector:

- Id: `freq1`
- Default Value: `50` Hz
- Start: `0` Hz
- Stop: `samp_rate/2` Hz  (What is the motivation for this relationship?)
- Step: `25`  Hz
- GUI Hint: `(0,0)`  (This sets the position of the Range selector on the GUI screen. 1st number is the row. 2nd number is the column.)

### For the Second GUI Range selector:

- Id: `freq2`
- Default Value: `2000` Hz
- Start: `0` Hz
- Stop: `5e3`  = 5,000 Hz
- Step: `25`  Hz
- GUI Hint: `(0,1)`  (This sets the position of the Range selector on the GUI screen, @ row 0 (1st), col. 1 (2nd))

### For the Variable block:
(Used for "GUI Hint" of graphing blocks (sinks) to set their width.)

- Id: `GUI_width`
- Value: `3`

### For the First Signal Source:

- Frequency: `freq1`

### For the Second Signal Source:

- Frequency: `freq2`

### For the Add block:
Use the defalut values, which are shown here.
- IO Type: `Float`
- Num Inputs: `2`
- Vec Length: `1`  

### For GUI Frequency Sink (Graph):

- Name: `"Frequency Spectrum from the Added Waves"`
- Spectrum Width: `Half` (The Spectrum Width option only appears after you've changed the ports to Orange as indicated in the Memos section above.)
- Y min = `-90` (Note the negative.  This setting crops the lower portion of the data to hide the "noise" in the frequencies)
- Y max = `10`
- GUI Hint: `(5, 0, 2, GUI_width)`  (This sets the position on the GUI screen, @ row 5, col. 0, width or span. If row 3 or 4 does not exist, the block will fill a position higher than row 5.)

### For the Time Sink:

"General" Tab
- Autoscale: `Yes`
- Number of Inputs: `3`
- GUI Hint: `(3, 0, 2, GUI_width)`

"Trigger" Tab
- Trigger Mode: `Auto`  (This will give the graph the appearance of being "frozen" even as data continues to be fed to it.)

"Config" Tab
- Control Panel: `yes`
- Line 1 Label: `Signal 1`   (The default value)
- Line 2 Label: `Signal 2`   (The default value)
- Line 3 Label: `Sum(Sig1, Sig2)` 

## Discussion

- You may remember, to accurately represent or reproduce a signal (a wave), the Nyquist Criteria requires: sample rate >= 2 * frequency of the signal.  Otherwise, with too few samples per second, the plot or the sound produced by the data will be distorted as compared to the orignal signal. 
- Try this: In one or more GUI Range selector, change the Stop value to be greater than the Nyquist Criteria allows, e.g., Stop: `samp_rate` Hz.   Then, while the program runs, adjust that frequency to be higher than the previous limit allowed.  What do you observe?
