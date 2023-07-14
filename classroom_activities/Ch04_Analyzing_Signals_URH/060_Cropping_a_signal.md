
<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 July 11: 060_Cropping_a_signal.md
</pre>
</details>

# Interpret a signal using URH 📻

- Launch urh and open your project folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github ![unknown_signal_3.complex](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_URH/unknown_signal_3.complex).

- Put it in your urh project folder.

- Click and drag the signal and drop it to the right (On the Interpretation tab).

- Clean up your `noisy` signal by adding a filter like in the previous lesson

- Determine signals `modulation` type as in previous lesson.

- The next thing we need to do is set the `Center` like the previous lesson.

- Determine signals `Samples/Symbol` as in previous lesson.

- Crop your signal to eliminate leading zeros.
    - Since we know our preample starts with a `1` now we can highlight everything past the first `1` in the bits window.

    ![highlightfirst1.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/highlightfirst1.png?raw=true)

    - Right-click in the signal window and select `Crop to selection`.
      
    ![crop.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/crop.png?raw=true)
  
- Set Show data as to `ASCII` and verify all settings to reveal your message.


### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
