# <!-- pandoc-only LSA 8: --> RC Car

### Disclaimer

Many uses of this are illegal. Stay legal, ethical, moral, honorable, and kind.

### Summary

This project requires the user to have a functional remote-controlled (RC) vehicle and its remote controller.  Optionally, you may use another remote controlled device and an appropriate remote control sending unit.  Other devices that might work include a television and remote controlled light(s), as examples.  Of course, both must be tuned to the same communication frequency.

<!-- pandoc-only ### Summary -->

This involves building two .grc flowgraph programs in **GNU Radio Companion** software.  One program records data from the remote control sending unit.  A second program transmits the data to the vehicle (or other device) to command it.  You can copy and modify the record and replay .grc files created in Exercise 270.  As an option, a method for removing unwanted portions of the recorded data is suggested, at least for Linux-OS users.

<!-- pandoc-only ### Summary -->

This excercise assumes the data is exchanged between the remote control and the vehicle using a fixed communication frequency, without encryption.  The method of frequency hopping spread-sectrum (FHSS) is not addressed.

<!-- pandoc-only ### Summary -->

It is necessary to know the frequency of your devices.  You might find the frequency written on your device, in the documentation for your device, or you may perform a web-search using the name and model number of your device.  Otherwise, you can look for it using **GNU Radio Companion** or **GQRX**. Finding the frequency is not discussed any further in this exercise/lesson.

### rc_car_record.grc:

```
GUI Range
GUI Range
osmocom source  -->  Band pass filter --> 
                      -->  Time Sink  
                      -->  File Sink  
                    -->  Waterfall Sink
```

### Parameters

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6` <!-- pandoc-only _(You may need more depending on whether the signal fits in the waterfall.)_ -->

<!-- pandoc-only ### Parameters -->

- osmocom Source:
  - Device Arguments: `"hackrf=0"`
  - Ch0: Frequency (Hz): For the in-class example, `50e6`. 
    - In general, you'll have to figure this out based on the device.
    - I highly recommend tuning off-center from the recorded signal.
    - The frequency for recording should match the frequency for replaying.
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): _situational_: Try to adjust so that the signal you're recording is approximately -0.6 to 0.6 on the Time Sink.
  - Ch0: BB Gain (dB): See note on IF Gain.

<!-- pandoc-only ### Parameters -->

- GUI Range (First):
  - Id: `IFGain`
  - `0` to `40`, steps of `8`
- GUI Range (Second):
  - Id: `BBGain`
  - `0` to `62`, steps of `2`

<!-- pandoc-only ### Parameters -->

- Band pass filter:
  - FIR Type: `Complex -> Complex (Complex Taps) (Decim)`
  - Low Cut: `-300e3`
  - High Cut: `-50e3`        (Note: the pass-through region will be off-set from the center frequency)
  - Transition Width: `50e3`

<!-- pandoc-only ### Parameters -->

- File sink:
  - File name: Pick using the "...". Make sure to pick a file that does NOT exist. One good name could be `my_car_recording.iqdata`. Do NOT pick a `.grc` file.
  <details><summary>Details if you're curious:</summary> When faced with a file-picking dialog, beginners will often navigate to the current `.grc` file. This is definitely not what you want -- as soon as you run the flowgraph, it will overwrite the saved flowgraph file with the data that you're recording. <!-- pandoc-exclude-line -->
  - Instead, I recommend picking a directory for your file, and naming it `my_gnu_recording.iqdata`. <!-- pandoc-exclude-line -->
  - The file extension can be anything you want (GNU Radio will treat it the same regardless), but `.iqdata` seems somewhat common in the SDR community. <!-- pandoc-exclude-line -->
        A good example may look like this:  <!-- pandoc-exclude-line -->
        `/home/yourusername/Desktop/my_gnu_recording.iq` <!-- pandoc-exclude-line -->
</details> <!-- pandoc-exclude-line -->

### rc_car_replay.grc:

```
GUI Range
File Source  -->  osmocom sink
             -->  Time sink
           -->  Waterfall Sink
```

### Parameters

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: _match your recording sample rate_

<!-- pandoc-only ### Parameters -->

- osmocom Sink:
  - Device Arguments: `"hackrf=0"`
  - Ch0: Frequency (Hz): `match your recording Ch0 Freq`
  - Ch0: RF Gain (dB): `0`
  - Ch0: IF Gain (dB): `IFGain`
  - Ch0: BB Gain (dB): `0`

<!-- pandoc-only ### Parameters -->

- GUI Range:
  - Id: `IFGain`
  - 0 to 47, steps of 1
- File Source:
  - Pick your `.iqdata` file (must make the recording first).
  
Optionally, you can add a selector in the middle to allow choosing from multiple recordings.

### ℹ️ Some useful resources for urh  <!-- pandoc-exclude-line --> 

<!-- pandoc-only ### Summary -->

<!-- pandoc-only In summary, you learned: -->

<!-- pandoc-only - How to install Universal Radio Hacker (URH) -->
<!-- pandoc-only - How to demonstrate Modulation using URH -->
<!-- pandoc-only - How to generate a signal using URH -->
<!-- pandoc-only - How to interpret a signal using URH -->
<!-- pandoc-only - How to interpret a noisy signal using URH -->
<!-- pandoc-only - How to cropp a noisy signal using URH -->
<!-- pandoc-only - How to interpret multiple noisy signals using URH -->
<!-- pandoc-only - How to record a signal using URH -->

<!-- pandoc-only ### References -->

- https://github.com/jopohl/urh