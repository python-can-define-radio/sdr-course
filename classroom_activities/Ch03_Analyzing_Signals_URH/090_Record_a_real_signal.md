# <!-- pandoc-only LSA 8: --> Record a signal using URH 📻

### Record a signal 

- Open File>Record signal.

- On the Device dropdown menu, select HackRF.
- If you do not see the HackRF device option, do the following:
    - Go to the main URH window, and click Edit > Options.
    - Check the checkbox for HackRF.
    - Downgrade your urh version to 2.9.4 if HackRF is unavailable.
        - Run this command in a terminal: `pip install "urh==2.9.4"`.

<!-- pandoc-only ### Record a signal -->

- On the Device Identifier, click the green refresh button.
    - It resembles this, but is green. 🔄

- Set your Frequency (Hz) to 2.45G (GigaHertz).

- Set your Sample Rate (Sps) to 2.0 Million.

- Set your Bandwidth (Hz) to 2.0 Million.

- ⚠️ Do not adjust your RF Gain; leave it at 0.

- Set your IF Gain to 24.

- Set your BB Gain to 40.

<!-- pandoc-only ### Record a signal -->

<div class="columns">
<div class="column">

- It should now look like this:

- Press start when you are ready to begin recording.
    - Hint: Make sure that whoever is transmitting has their message set to repeat so that you can capture it more easily.
    - The file grows quite quickly, so don't record for longer than about 3-5 seconds.

</div>
<div class="column">

![Record Signal View](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/record_signal.png?raw=true) 

</div>
</div>

<!-- pandoc-only ### Record a signal -->

- Now you can go to the Interpretation tab and use what you learned previously to Demodulate the message.

- Once you have been successful, feel free to partner up with a classmate and try to generate and send your own messages that your partner can Demodulate.

### ℹ️ Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh <!-- pandoc-exclude-line --> 

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/080_Interpret_multiple_noisy_signals.md)</p> <!-- pandoc-exclude-line --> 

[010_pcdr_ook_tx_intro]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/010_pcdr_ook_tx_intro.md
