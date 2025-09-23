# Cropping a noisy signal using URH 📻

### Download file

- Launch urh and open your folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file from github [unknown_signal_3.complex](https://github.com/python-can-define-radio/sdr-course/raw/main/classroom_activities/Ch03_Analyzing_Signals_URH/unknown_signal_3.complex).

- Put it in your folder.

- Click and drag the signal and drop it to the right (On the Interpretation tab).

### Interpret the signal

- Clean up your [`noisy`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md) signal by adding a filter.

- Determine signals [`Modulation`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md) type as in previous lesson.

- The next thing we need to do is set the [`Center`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md).

- Determine signals [`Samples/Symbol`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md).

### Crop the signal

<div class="columns">
<div class="column">

- Crop your signal to eliminate leading zeros.
    - Since we know our preample starts with a `1` now we can highlight everything past the first `1` in the bits window.

</div>
<div class="column">

![highlight from the first 1](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/highlightfirst1.png?raw=true)

</div>
</div>

<!-- pandoc-only ### Crop the signal -->

<div class="columns">
<div class="column">

    - Right-click in the signal window and select `Crop to selection`.

</div>
<div class="column">

![crop to selection](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/crop.png?raw=true)

</div>
</div>

### Get the message

- Set Show data as to `ASCII` and verify all settings to reveal your message.

<!-- ### Additional practice

Yet another option for the `generate_ook_modulated_example_file` function is `message_delay`:

```python3
from pcdr.v0_compat import generate_ook_modulated_example_file
generate_ook_modulated_example_file("my_example_ook_file.complex", noise=True, message_delay=True)
``` -->

### ℹ️ Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/070_Interpret_multiple_noisy_signals.md)</p> <!-- pandoc-exclude-line --> 
