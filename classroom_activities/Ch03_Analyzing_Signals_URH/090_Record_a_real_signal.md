<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 090_Record_a_real_signal.md
</pre>
</details>

# Record a signal using URH 📻

ℹ️ This material coincides with material from SDR slideshow A (slides 7-8, 14, 20, 22, 25, 28-32, 34-39, 40-46).

- The first thing you will need when recording a signal is to know what frequency you want to record.

- Open File>Record signal.

- On the Device dropdown menu select HackRF.
  -  Note: if you do not see HackRF, see the troubleshooting in footnote 1.

- On the Device Identifier click the green refresh button. 🔄 (It is green, I couldn't find a more accurate emoji)

- Set your Frequency (Hz) to 2.45G (GigaHertz).

- Set you Sample Rate (Sps) to 2.0 Million.

- Set your Bandwidth (Hz) to 2.0 Million.

- ⚠️ Do not adjust your RF Gain leave it at 0.

- Set your IF Gain to 24.

- Set your BB Gain to 40.

- It should now look like this:

![record_signal.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/record_signal.png?raw=true) 

- Press start when you are ready to begin recording.
    - Hint: Make sure that whoever is transmitting has their message on repeat.
    - You will only need to record for 3-5 seconds or the file will be large.
 
- Now you can go to the Interpretation tab and use what you learned previously to Demodulate the message.

- Once you have been successful feel free to partner up with a classmate and try to generate and send your own messages that your partner can Demodulate.

### Optional exercise

- Incorporate RC Car with URH:  
  - Simple Record and Replay  
  - Demodulate and generate:  
    - Record (Make sure you're offset to avoid DC Spike)  
    - Demod (Get zeros and ones; use URH's Generate tab to verify)  
    - Generate and Transmit using Python [pcdr OOK transmit][010_pcdr_ook_tx_intro]  
    - Use GUIZero to create up/down/left/right buttons to control car

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh

## <p align="center">[&larr; Previous Lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/080_Interpret_multiple_noisy_signals.md)</p>


### Footnotes

Footnote 1: Troubleshooting: If you do not see the HackRF device option, do the following:
  - Go to the main URH window, and click Edit > Options.
  - Check the checkbox for HackRF.
    - If the checkbox is unavailable, try downgrading to urh version 2.9.4 by running the following command in a terminal: `pip install "urh==2.9.4"`


[010_pcdr_ook_tx_intro]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/010_pcdr_ook_tx_intro.md
