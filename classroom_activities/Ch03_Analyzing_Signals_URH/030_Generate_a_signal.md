# <!-- pandoc-only LSA 3: --> Generate a signal 📻

### Modulation settings

<div class="columns">
<div class="column">

- Click on the Generator tab at the top of the urh window.

- Verify your defaults are set by clicking the `Edit` button and using the table information.

- Close the `Edit` window.

</div>
<div class="column">

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

</div>
</div>

### Generated Data

<div class="columns">
<div class="column">

- In the white space under "Generated Data":
  - right-click and select `add empty message`.
  - Type in 32 and hit `ok`.
  - Type `10101011` in the first 8 boxes as your preamble.
    - The preamble serves as a special character that is used to identify when the message begins.
  - At the bottom right select `ASCII` from the `viewtype` dropdown menu.
  - This is what your generated data window should now look like with this character `«` as our preamble.

</div>
<div class="column">

![generated data](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/generated_data.png?raw=true) 

</div>
</div>

<!-- pandoc-only ### Generated Data -->

<div class="columns">
<div class="column">

- Notice that the 32 bit message we selected is now showing up as 4 bytes in the generated data window.

</div>
<div class="column">
 
<!-- pandoc-only ![generated data](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/generated_data.png?raw=true) -->

</div>
</div>
 
### Add the message

<div class="columns">
<div class="column">

- The next step would be to add a simple 3 letter word in the remaining slots. 
- The cursor control is unconventional, you must press `Tab` after each character to move the focus to the next character slot.

</div>
<div class="column">

![cat message](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/catscreenshot.png?raw=true) 

</div>
</div>

### Remove pause

<div class="columns">
<div class="column">

- Select the Pauses tab as shown.
- Right click and select `Edit` on the pause in the window, change the Pause Length to 0 and hit `ok`.

</div>
<div class="column">

![pauses](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/pauses.png?raw=true) 

</div>
</div>

### Generate the file

<div class="columns">
<div class="column">

- Click the Generate file button
  - navigate to your folder and save.
  - Ensure it is still a `.complex` file.

- Select the Interpretation tab.
    - Click and drag the file to the grey space on the right.
    - Ensure your settings match the picture.
    - Change the  `Show data as` dropdown menu to `ASCII`.

</div>
<div class="column">

![generated.complex](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/generated_file.png?raw=true) 

</div>
</div>


### ℹ️ Some useful resources <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md)</p> <!-- pandoc-exclude-line --> 
