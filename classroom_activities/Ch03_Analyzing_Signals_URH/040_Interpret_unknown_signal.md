# <!-- pandoc-only LSA 4: --> Interpret a signal 📻

### Download signal

<div class="columns">
<div class="column">

- Launch urh to your folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file from github [unknown signal 1](https://github.com/python-can-define-radio/sdr-course/raw/main/classroom_activities/Ch03_Analyzing_Signals_URH/unknown_signal_1.complex). 

- Put it in your folder.
    - You may have other files showing than the ones you see here.

</div>
<div class="column">

![unknown signal 1](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1.png?raw=true) 

</div>
</div>

### View signal

<div class="columns">
<div class="column">

- On the left side you should see the signal you downloaded.

- Click and drag it to the grey space on the right to begin interpretation.

</div>
<div class="column">

![unknown signal 1](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1_interpret.png?raw=true) 

</div>
</div>

### Determine Samples/Symbol

<div class="columns">
<div class="column">

- Determine whether it is ASK, FSK, or PSK modulation.

- Try to identify a single `0` or `1` and highlight it.
    - Ensure you highlight the `smallest` section of signal.
    - You may need to zoom into the signal to see it more clearly.
    - urh will tell you how many samples are selected.
    - Look where it says "50 selected".

</div>
<div class="column">

![unknown signal 1](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/unknown_signal_1_determine_samplerate.png?raw=true)

</div>
</div>

<!-- pandoc-only ### Determine Samples/Symbol -->

<div class="columns">
<div class="column">

- If you actually highlighted a single 1 or 0 then we can now change our settings to 50 Samples/Symbol and 1 Bits/Symbol.

- Now ensure your settings are correct.
    - ⚠️ Your settings may be different.

</div>
<div class="column">

![final settings](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/final_settings.png?raw=true) 

</div>
</div>

<!-- pandoc-only ### Determine Samples/Symbol -->

<div class="columns">
<div class="column">

- If you did everything correctly you should now see your secret message (it will be different than the message shown here).

</div>
<div class="column">

![final message](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/final_message.png?raw=true) 

</div>
</div>

<!-- ### Additional practice

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
``` -->

### ℹ️ Some useful resources <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/030_Generate_a_signal.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md)</p> <!-- pandoc-exclude-line --> 
