<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Sep 23: 075-RC-Car.md
2022 Oct 17: 275-RC-Car.md
2023 May 22: 030_RC_Car.md
</pre>
</details>

## Disclaimer

Many uses of this are illegal. Stay legal, ethical, moral, honorable, and kind.

## Summary

This project requires the user to have a functional remote-controled (RC) vehicle and its remote controller.  Optionally, you may use another remote controlled device and an appropriate remote control sending unit.  Other devices that might work include a television and remote controlled light(s), as examples.  Of course, both must be tuned to the same communication frequency.

This involves building two .grc flowgraph programs in **GNU Radio Companion** software.  One program records data from the remote control sending unit.  A second program transmits the data to the vehicle (or other device) to command it.  You can copy and modify the record and replay .grc files created in Exercise 270.  As an option, a method for removing unwanted portions of the recorded data is suggested, at least for Linux-OS users.

This excercise assumes the data is exchanged between the remote control and the vehicle using a fixed communication frequency, without encryption.  The method of frequency hopping spread-sectrum (FHSS) is not addressed.

It is necessary to know the frequency of your devices.  You might find the frequency written on your device, in the documentation for your device, or you may perform a web-search using the name and model number of your device.  Otherwise, you can look for it using **GNU Radio Companion** or **GQRX**. Finding the frequency is not discussed any further in this exercise/lesson.

## Record:

`rc_car_record.grc`

```
GUI Range

GUI Range

osmocom source  -->  Band pass filter  -->  Time Sink
                                       -->  File Sink
                                       -->  Waterfall Sink
```

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6` _(You may need more depending on whether the signal fits in the waterfall.)_
- osmocom Source:
  - Ch0: Frequency (Hz): For the in-class example, `50e6`. In general, you'll have to figure this out based on the device you're working with. I highly recommend tuning off-center from the signal that you are intending to record. Whatever frequency you pick for recording should match the frequency you pick for replaying.
  - Ch0: Frequency Correction (ppm): `0`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): Will depend on your situation. Try to adjust so that the signal you're recording is approximately -0.6 to 0.6 on the Time Sink.
  - Ch0: BB Gain (dB): See note on IF Gain.
- GUI Range (First):
  - Id: `IFGain`
  - 0 to 40, steps of 8
- GUI Range (Second):
  - Id: `BBGain`
  - 0 to 62, steps of 2
- Band pass filter:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cut: `-300e3`
  - High Cut: `-50e3`        (Note: the pass-through region will be off-set from the center frequency)
  - Transition Width: `50e3`
- File sink:
  - File name: Pick using the "...". Make sure to pick a file that does NOT exist. One good name could be `my_car_recording.iqdata`. Do NOT pick a `.grc` file. <details><summary>Details if you're curious:</summary> When faced with a file-picking dialog, beginners will often navigate to the current `.grc` file. This is definitely not what you want -- as soon as you run the flowgraph, it will overwrite the saved flowgraph file with the data that you're recording.
       
       Instead, I recommend picking a directory for your file, and naming it `my_gnu_recording.iqdata`. The file extension can be anything you want (GNU Radio will treat it the same regardless), but `.iqdata` seems somewhat common in the SDR community.  
        A good example may look like this:  
        `/home/yourusername/Desktop/my_gnu_recording.iq`
</details>

## Replay:

`rc_car_replay.grc`

```
GUI Range

File Source  -->  osmocom sink
             -->  Time sink
             -->  Waterfall Sink
```

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: _match your recording sample rate_
- osmocom Sink:
  - Ch0: Frequency (Hz): _match your recording Ch0 Freq`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `IFGain`
  - Ch0: BB Gain (dB): `0`
- GUI Range:
  - Id: `IFGain`
  - 0 to 47, steps of 1
- File Source:
  - Pick your `.iqdata` file (must make the recording first).
  
Optionally, you can add a selector in the middle on to allow choosing from multiple recordings.

## To edit the data file prior to replay (Optional)
Linux OS users might find and use **"inspectrum"** software to edit the data file(s) recorded from the RC vehicled remote control unit.  The software may be available on github.com or another source.  Other software might be found having suitable capabilitiees.  The student or end-user will need to determine the suitability and appropriateness of any software he or she loads.
