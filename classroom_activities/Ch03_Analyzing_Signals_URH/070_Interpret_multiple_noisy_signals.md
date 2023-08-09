<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 060_Interpret_multiple_noisy_signals.md
2023 July 10: 070_Interpret_multiple_noisy_signals.md
</pre>
</details>

# Interpret a signal using URH 📻

- Launch urh and open your project folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github ![unknown_signal_4.complex](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_URH/unknown_signal_4.complex).

- Put it in your urh project folder.

- The first thing we need to do is seperate and save each signal.

- The second thing we need to do is clean up each `noisy` signal by adding a filter like in the previous lesson

- Go back to Signal View `Analog` and determine signals `modulation` type as in previous lesson.

- The next thing we need to do is set the `Center` like the previous lesson.

- Determine signals `Samples/Symbol` as in previous lesson.

- Crop your signal to eliminate leading zeros.

- Set Show data as to `ASCII` and verify all settings to reveal your message.


### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh

### General order of operations for analyzing an ASK signal:
|    | Step |
|-----|-----------|
|1|  Separate signals.|
|2|  Apply a bandpass filter to eliminate unwanted signal (noise).|
|3|  Determine the signal's modulation scheme.|
|4|  Determine and set the "Center" between a `1` and a `0`.|
|5|  Determine the signal's Sample per Symbol.|
|6|  Crop the signal to eliminate the portion without data.|
|7|  Verify all settings.|
