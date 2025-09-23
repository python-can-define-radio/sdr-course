# Interpret multiple noisy signals using URH 📻 <!-- pandoc-exclude-line -->

### Download the file

- So far all we have evaluated are ASK signals lets change that up.

- Launch urh and open your folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github [unknown_signal_5.complex](https://github.com/python-can-define-radio/sdr-course/raw/main/classroom_activities/Ch03_Analyzing_Signals_URH/unknown_signal_5.complex).

- Put it in your folder.

- The first thing we need to do is seperate and save each signal.

### Interpret the signal

- The second thing we need to do is clean up each [`noisy`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md) signal by adding a filter.
    - Before adding a filter to each signal right-click and select `Configure filter bandwidth` and select `Narrow` at 0.01Hz then click ok.
    - The closer your signals are to each other the narrower your filter bandwidth should be.

- Go back to Signal View `Analog` and determine signals [`modulation`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md).

<!-- pandoc-only ### Interpret the signal -->

- The next thing we need to do is set the [`Center`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md).

- Determine signals [`Samples/Symbol`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md).

- [`Crop`](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/060_Cropping_a_signal.md) your signal to eliminate leading zeros.

- Set `Show data as` to `ASCII` and verify all settings to reveal your message.

### Order of operations for analyzing a signal

|    | Step |
|----|------|
|  1 |  Separate signals.|
|  2 |  Apply a bandpass filter to eliminate unwanted signal (noise).|
|  3 |  Determine the signal's modulation scheme.|
|  4 |  Determine and set the "Center" between a `1` and a `0`.|
|  5 |  Determine the signal's Sample per Symbol.|
|  6 |  Crop the signal to eliminate the portion without data.|
|  7 |  Verify all settings.|

### ℹ️ Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/070_Interpret_multiple_noisy_signals.md)  --------  [Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/090_Record_a_real_signal.md)</p> <!-- pandoc-exclude-line --> 
