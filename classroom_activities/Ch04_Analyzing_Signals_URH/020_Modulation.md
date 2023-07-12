<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 020_Modulation.md
</pre>
</details>

You may remember that we introduced the idea of [Modulation](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/020_Sample_Rates_Intro.md#what-is-modulation) in a previous lesson. 

In this section, we will visually show you what those modulation techniques look like using urh.

# Demonstrate Modulation using URH 📻

- There are 3 basic types of modulation we will demonstrate.
    - Amplitude Shift Keying (ASK)
    - Frequency Shift Keying (FSK)
    - Phase Shift Keying (PSK)

- Open a terminal window.
  
- Type `urh` to launch the program.
  
- Select the Generator tab at the top of urh window.

- Then select `Edit` at the bottom of the urh window.

- This opens a popup showing a carrier signal, some raw data, and what the signal would look like combined with the data.

- Set it up something like this to start:

### Carrier section:

  | | |
  |-------|-----|
  |Frequency:| 10.0|
  |Phase:| 0.000°|  

### Data (raw bits) section:

  | | |
  |-------|-----|
  |Data:| 1010110010101100|
  |Samples per Symbol:| 200000|
  |Sample Rate (Sps):| 2.0M| 

### Modulation section:

  | | |
  |-------|-----|
  |dropdown menu ▾|Amplitude Shift Keying (ASK)|
  |Bits per Symbol:| 1|
  |Amplitudes in %:| 0/100|

- It should look something like this:
    - ASK should be pretty easy determining the difference between a 1 and a 0.
   
![ASK_modulated_signal.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/ASK_modulated_signal.png?raw=true)

- Now on the modulated signal click and drag to try to highlight a single bit (1 or 0).
    - Notice the Samples selected should be around 200000 which lines up with our Samples per Symbol setting above.

![singlebithighlighted.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/singlebithighlighted.png?raw=true)

- You can also adjust the Amplitudes in % value which essentially changes the value/height/amplitude of a "0".

![amplitude25%.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/amplitude25%25.png?raw=true)

- Try changing the modulation.

  ### Modulation section:

  | | |
  |-------|-----|
  |dropdown menu ▾|Frequency Shift Keying (FSK)|
  |Bits per Symbol:| 1|
  |Frequencies in Hz:|20/200|
  
- What do you see different?

![fsk_modulation.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/fsk_modulation.png?raw=true)

- To determine Samples per Symbol of FSK highlight the smallest section of a single frequency that you can find.
    - This becomes harder and harder the closer the frequencies are to each other.

![fsk_highlight.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/fsk_highlight.png?raw=true)

- The last thing we are going to look at is Phase Shift Keying (PSK).

- Try this:

  ### Modulation section:

  | | |
  |-------|-----|
  |dropdown menu ▾|Phase Shift Keying (PSK)|
  |Bits per Symbol:| 1|
  |Phases in degree:|0/180 or 180/0|
  
- It should look something like this:
  
![psk_modulation.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/psk_modulation.png?raw=true)

- To determine Samples per Symbol of PSK highlight the smallest portion of the signal between phase changes that you can find.

![psk_modulation.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/psk_highlight.png?raw=true)

- In Phase Shift Keying the change of phase marks the shift between a 1 and a 0.

- This simple example is known as Binary Phase Shift Keying or BPSK.
    - Other examples of PSK
        - QPSK (2 bits per symbol)
        - 8PSK (3 bits per symbol)
        - 16QAM (4 bits per symbol)
          - ℹ️ Note: 16QAM involves modulating both the phase and the amplitude. This is currently outside of urh's capability.

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
