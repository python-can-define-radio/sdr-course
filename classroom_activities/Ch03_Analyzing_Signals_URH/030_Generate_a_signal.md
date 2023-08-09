<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 030_Generate_a_signal.md
</pre>
</details>

# Generate a signal using URH 📻

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

- Now add the « character which will serve as a preamble of 10101011 in the first slot so we will know when our useful data begins.  
  Here's How:
    - The Ubuntu keyboard shortcut for this symbol would be Ctl + Shift + u then release and type 00ab then press enter.
    - The Windows keyboard shortcut if your interested would be Alt + 0171 then release.
    - Or you can just copy and paste the character above.
 
- The next step would be to add a simple 3 letter word in the remaining slots.

- It should now look like this

![catscreenshot.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/catscreenshot.png?raw=true) 

- Select the Pauses tab as shown.

![pauses.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/pauses.png?raw=true) 

- Right click and select Edit on the pause in the window, change the Pause Length to 0 and hit ok.

- Click the Generate file button at the bottom and navigate to your project folder and save the file.
    - It is not necessary to rename the file, if you do ensure it is still a `.complex` file.

- Now change tabs to the Interpretation tab.
    - Click and drag the file `generated.complex` (or whatever you renamed it) to the grey space on the right.
 
![generated_file.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/generated_file.png?raw=true) 

- Now ensure your settings match the picture above and change the  `Show data as` dropdown menu to `ASCII` and you should see your message in the window.
    - In the next lesson we will learn how to do the same thing without already knowing all the settings.

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
