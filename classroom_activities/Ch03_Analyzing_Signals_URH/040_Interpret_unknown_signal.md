
<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 040_Interpret_unknown_signal.md
</pre>
</details>

# Interpret a signal using URH 📻

- Launch urh and open your project folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github ![unknown_signal_1.complex](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_URH/unknown_signal_1.complex). (click to go to the linked page, and download from there.)

- Put it in your urh project folder.

- It should now look something like this:
    - You may have other files showing than the ones you see here.

![unknown_signal_1.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_1.png?raw=true) 

- On the left side you should see the signal you received.

- Click and drag it to the grey space on the right to begin interpretation.

![unknown_signal_1_interpret.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_1_interpret.png?raw=true) 

- Looking at the signal try to determine whether it is ASK, FSK, or PSK modulation.

- Looking at the signal try to identify a single `0` or `1` and highlight it.
    - You may need to zoom into the signal to see it more clearly.
    - It is actually easier to select just a single `0` or `1` in the bottom window but this may be inaccurate because your Samples/Symbol setting may not be correct. 

![unknown_signal_1_determine_samplerate.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_1_determine_samplerate.png?raw=true)

- When you highlight a portion of the signal urh will tell you how many samples you have selected like in the above image it says right below the highlighted portion "50 selected".

- If you actually highlighted a single 1 or 0 then we can now change our settings to 50 Samples/Symbol and 1 Bit(s)/Symbol.
    - ⚠️ Your signal may be different than this example.

- Now ensure your settings are correct:
    - ⚠️ Your settings may be different than this example.

![final_settings.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/final_settings.png?raw=true) 

- If you did everything correctly you should now see your secret message (it will be different than the message shown below).

![final_message.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/final_message.png?raw=true) 

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
