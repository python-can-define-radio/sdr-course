<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 030_Generate_a_signal.md
</pre>
</details>

# Generate a signal using URH 📻

ℹ️ This material coincides with material from SDR slideshow A (slides 7-8, 14, 20, 22, 25, 28-32, 34-39, 40-46).

- Click on the Generator tab at the top of the urh window.

- Make sure your defaults are set by clicking the `Edit` button and using the following information:  

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

- Close the `Edit` window.

- On the right side under "Generated Data" in the white space right-click and select `add empty message`.

- Type in 32 and hit `ok`.

- At the bottom right of the window select `ASCII` from the `viewtype` dropdown menu.

- This is what your generated data window should now look like.

![generated_data.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/generated_data.png?raw=true) 

- Notice that the 32 bit message we selected is now showing up as 4 bytes in the generated data window.

- Now, add the « character which will serve as a preamble of 10101011 in the first slot, so we will know when our useful data begins.  
  Here's how:
    - The Ubuntu keyboard shortcut: Ctl + Shift + u, then release. Type `00ab`. Press enter.
    - The Windows keyboard shortcut: Alt + 0171 then release.
    - Alternatively, you can just copy and paste the character above.
 
- The next step would be to add a simple 3 letter word in the remaining slots. The cursor control is unconventional: you must press `Tab` after each character to move the focus to the next character slot.

- It should now look like this

![catscreenshot.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/catscreenshot.png?raw=true) 

- Select the Pauses tab as shown.

![pauses.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/pauses.png?raw=true) 

- Right click and select Edit on the pause in the window, change the Pause Length to 0 and hit ok.

- Click the Generate file button at the bottom and navigate to your folder and save the file.
    - It is not necessary to rename the file, if you do ensure it is still a `.complex` file.

- Now change tabs to the Interpretation tab.
    - Click and drag the file `generated.complex` (or whatever you renamed it) to the grey space on the right.
 
![generated_file.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/generated_file.png?raw=true) 

- Now ensure your settings match the picture above and change the  `Show data as` dropdown menu to `ASCII` and you should see your message in the window.
    - In the next lesson we will learn how to do the same thing without already knowing all the settings.

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md)</p>
