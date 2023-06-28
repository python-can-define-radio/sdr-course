<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 020_Modulation.md
</pre>
</details>

You may remember that we introduced the idea of [Modulation](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/020_Sample_Rates_Intro.md#what-is-modulation). 

In this section, we'll will visually show you what those modulation techniques look like using urh.


# Demonstrate Modulation

- First select the Generator tab at the top of urh window.

- Then select `Edit` at the bottom of the urh window.

- This opens a popup showing a carrier signal, some raw data, and what the signal would look like combined with the data.

- Set it up something like this to start:

    ### `Carrier`
    - Frequency: 10.0K
    - Phase: 0.000°  
    ### `Data (raw bits)`
    - Data: 1010110010101100
    - Samples per Symbol: 200
    - Sample Rate (Sps): 2.0M
    ### `Modulation`
    - Amplitude Shift Keying (ASK)
    - Bits per Symbol: 1
    - Amplitudes in %: 0/100

- It should look something like this:  
[ASK_modulated_signal.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/ASK_modulated_signal.png?raw=true)

- Now on the modulated signal click and drag to try to highlight a single bit (1 or 0).
    - Notice the Samples selected should be around 200 which lines up with our Samples per Symbol setting above.

- You can also adjust the Amplitudes in % value which essentially changes the value/height/amplitude of a "0".

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
