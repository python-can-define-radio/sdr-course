# Cropping a noisy signal using URH 📻

- Launch urh and open your folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github [unknown_signal_3.complex](https://github.com/python-can-define-radio/sdr-course/raw/main/classroom_activities/Ch03_Analyzing_Signals_URH/unknown_signal_3.complex).

- Put it in your folder.

- Click and drag the signal and drop it to the right (On the Interpretation tab).

- Clean up your [`noisy`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md) signal by adding a filter like in the previous lesson

- Determine signals [`Modulation`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md) type as in previous lesson.

- The next thing we need to do is set the [`Center`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md) like the previous lesson.

- Determine signals [`Samples/Symbol`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md) as in previous lesson.

- Crop your signal to eliminate leading zeros.
    - Since we know our preample starts with a `1` now we can highlight everything past the first `1` in the bits window.

    ![highlightfirst1.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/highlightfirst1.png?raw=true)

    - Right-click in the signal window and select `Crop to selection`.
      
    ![crop.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/crop.png?raw=true)
  
- Set Show data as to `ASCII` and verify all settings to reveal your message.

### Additional practice

Yet another option for the `generate_ook_modulated_example_file` function is `message_delay`:

```python3
from pcdr.v0_compat import generate_ook_modulated_example_file
generate_ook_modulated_example_file("my_example_ook_file.complex", noise=True, message_delay=True)
```

### ℹ️ Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/070_Interpret_multiple_noisy_signals.md)</p> <!-- pandoc-exclude-line --> 
