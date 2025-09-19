# Interpret a signal using URH 📻

- Launch urh and open your folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github [unknown_signal_1.complex](https://github.com/python-can-define-radio/sdr-course/raw/main/classroom_activities/Ch03_Analyzing_Signals_URH/unknown_signal_1.complex). 

- Put it in your folder.

- It should now look something like this:
    - You may have other files showing than the ones you see here.

![unknown_signal_1.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1.png?raw=true) 

- On the left side you should see the signal you received.

- Click and drag it to the grey space on the right to begin interpretation.

![unknown_signal_1_interpret.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1_interpret.png?raw=true) 

- Looking at the signal try to determine whether it is ASK, FSK, or PSK modulation.

- Looking at the signal try to identify a single `0` or `1` and highlight it.
    - Ensure you highlight the `smallest` section of signal or lack of signal that you can find.
    - You may need to zoom into the signal to see it more clearly.
    - It is actually easier to select just a single `0` or `1` in the bottom window but this may be inaccurate because your Samples/Symbol setting may not be correct. 

![unknown_signal_1_determine_samplerate.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1_determine_samplerate.png?raw=true)

- When you highlight a portion of the signal urh will tell you how many samples you have selected like in the above image it says right below the highlighted portion "50 selected".

- If you actually highlighted a single 1 or 0 then we can now change our settings to 50 Samples/Symbol and 1 Bit(s)/Symbol.
    - ⚠️ Your signal may be different than this example.

- Now ensure your settings are correct:
    - ⚠️ Your settings may be different than this example.

![final_settings.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/final_settings.png?raw=true) 

- If you did everything correctly you should now see your secret message (it will be different than the message shown below).

![final_message.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/final_message.png?raw=true) 

### Additional practice

For additional practice, you can generate a file using this Python code:

```python3
from pcdr.v0_compat import generate_ook_modulated_example_file
generate_ook_modulated_example_file("my_example_ook_file.complex")
```

If you copy and run that, it will create a file named `my_example_ook_file.complex` in your current working directory. You can then try demodulating the message in that file for extra practice. It picks random parameters, so feel free to run it as many times as you like.

For more info on `generate_ook_modulated_example_file`, look at the docstring:

```python3
from pcdr.v0_compat import generate_ook_modulated_example_file
print(generate_ook_modulated_example_file.__doc__)
```

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/030_Generate_a_signal.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md)</p> <!-- pandoc-exclude-line --> 
