
<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 050_Interpret_unknown_noisy_signal.md
</pre>
</details>

# Interpret a signal using URH 📻

- Launch urh and open your project folder.

- Click on the Interpretation tab at the top of the urh window.

- Download the following file (link provided) from github ![unknown_signal_2.complex](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_URH/unknown_signal_2.complex).

- Put it in your urh project folder.

- Click and drag the signal and drop it to the right (On the Interpretation tab).

- The first thing we need to do is clean up the `noisy` signal by adding a filter.

- Change the Signal View to `Spectrogram`. (You should see something like this)

![unknown_signal_2_spectrogram.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_2_spectrogram.png?raw=true) 

- Now highlight the signal vertically as shown.

![unknown_signal_2_spectrogram_highlight.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_2_spectrogram_highlight.png?raw=true)

- Now somewhere in the reddish area right-click and select `Apply bandpass filter (filter bw=0.08)`.

- Now you should see both signals in the window like this (don't worry if your filtered signal looks different).

![unknown_signal_2_with_filtered.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_2_with_filtered.png?raw=true)

- Now you can close the first unfiltered signal by clicking the red ✖️ on the top signal.

- Its probably a good idea to save this new filtered signal, click the 💾 icon in the Interpretation tab window.

- Give it a new name like `unknown_signal_2_filtered.complex` do not save over your original signal in case you need to start over for any reason.

- Go back to Signal View `Analog` and determine signals `Modulation` type as in previous lesson.

- Now we need to adjust the `Center` setting.

- Initially set your `Noise` and your `Center` settings to `0` if it isn't already.

- Change the Signal View to `Demodulated`.

- It should look something like the following picture.
    - If the signal is "weak" you may need to adjust the Y-Scale, with the slider on the right, to get a better look at the signal in order to set the Center.

![unknown_signal_2_demodulated.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_2_demodulated.png?raw=true)

- You can click and drag the line (between purple and green) so that it rests somewhere between your high `1` and your low `0` like this.
    

![unknown_signal_2_centerset.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/unknown_signal_2_centerset.png?raw=true)

- Determine signals `Samples/Symbol` as in previous lesson.

- Set Show data as to `ASCII` and verify all settings to reveal your message.


### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
