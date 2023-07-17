<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 090_Record_a_real_signal.md
</pre>
</details>

# Record a signal using URH 📻

- The first thing you will need when recording a signal is to know what frequency you want to record.

- Open File>Record signal.

- On the Device dropdown menu select HackRF.

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

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
