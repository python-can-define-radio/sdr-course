# <!-- pandoc-only LSA 2: --> Demonstrate Modulation using URH 📻

### Types of Modulation

- There are 3 basic types of modulation we will demonstrate.
    - Amplitude Shift Keying (ASK)
    - Frequency Shift Keying (FSK)
    - Phase Shift Keying (PSK)

### Instructions

- Open a terminal window.
- Type `urh` to launch the program.
- Select the Generator tab at the top of urh window.
- Then select `Edit` at the bottom of the urh window.
- This opens a popup showing a carrier signal, some raw data, and what the signal would look like combined with the data.

### Modulation settings

  | | |
  |-------|-----|
  |Frequency:| 10.0|
  |Phase:| 0.000°|  
  |Data:| 1010110010101100|
  |Samples per Symbol:| 200000|
  |Sample Rate (Sps):| 2.0M| 
  |dropdown menu ▾|Amplitude Shift Keying (ASK)|
  |Bits per Symbol:| 1|
  |Amplitudes in %:| 0/100|

### ASK Modulation

<div class="columns">
<div class="column">

- What is the difference between a 1 and a 0?

</div>
<div class="column">

![ASK modulated signal](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/ASK_modulated_signal.png?raw=true)

</div>
</div>

<!-- pandoc-only ### ASK Modulation -->

<div class="columns">
<div class="column">

- Now on the modulated signal click and drag to try to highlight a single bit (1 or 0).
- Notice the Samples selected should be around 200000 which lines up with our Samples per Symbol setting above.

</div>
<div class="column">

![single bit highlighted](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/singlebithighlighted.png?raw=true)

</div>
</div>

<!-- pandoc-only ### ASK Modulation -->

<div class="columns">
<div class="column">

- You can also adjust the Amplitudes in % value which essentially changes the value/height/amplitude of a "0".

</div>
<div class="column">

![percentage of amplitude](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/amplitude25%25.png?raw=true)

</div>
</div>

### New Modulation settings

  | | |
  |-------|-----|
  |dropdown menu ▾|Frequency Shift Keying (FSK)|
  |Bits per Symbol:| 1|
  |Frequencies in Hz:|20/200|
  
### FSK Modulation

<div class="columns">
<div class="column">

- What do you see different?

</div>
<div class="column">

![FSK modulated signal](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/fsk_modulation.png?raw=true)

</div>
</div>

<!-- pandoc-only ### FSK Modulation -->

<div class="columns">
<div class="column">

- To determine Samples per Symbol of FSK highlight the smallest section of a single frequency that you can find.
- This becomes harder and harder the closer the frequencies are to each other.

</div>
<div class="column">

![single bit highlighted](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/fsk_highlight.png?raw=true)

</div>
</div>

### New Modulation settings:

  | | |
  |-------|-----|
  |dropdown menu ▾|Phase Shift Keying (PSK)|
  |Bits per Symbol:| 1|
  |Phases in degree:|0/180 or 180/0|
  
### PSK Modulation

<div class="columns">
<div class="column">

- In Phase Shift Keying the change of phase marks the shift between a 1 and a 0.

</div>
<div class="column">

![PSK modulated signal](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/psk_modulation.png?raw=true)

</div>
</div>

<!-- pandoc-only ### PSK Modulation -->

<div class="columns">
<div class="column">

- To determine Samples per Symbol of PSK highlight the smallest portion of the signal between phase changes that you can find.

</div>
<div class="column">

![single bit highlighted](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/psk_highlight.png?raw=true)

</div>
</div>

<!-- pandoc-only ### PSK Modulation -->

- This simple example is known as Binary Phase Shift Keying or BPSK.
    - Other examples of PSK:
        - QPSK (2 bits per symbol)
        - 8PSK (3 bits per symbol)
        - 16QAM (4 bits per symbol)
          - ℹ️ Note: 16QAM involves modulating both the phase and the amplitude. This is currently outside of urh's capability.

### Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/010_Install_URH.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/030_Generate_a_signal.md)</p> <!-- pandoc-exclude-line --> 
