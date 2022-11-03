_Note: This overlaps significantly with Exercise 270. We plan to merge the two, but for now, we recommend reading both.
       To work here, you can copy, modify, and use the record and replay .grc files created in Exercise 270._
       
## Disclaimer

Many uses of this are illegal. Stay legal, ethical, moral, honorable, and kind.

## Summary

This project requires the user to have a functional remote-controled (RC) vehicle and its remote controller.  Optionaly, you may use another remote controlled device and an appropriate remote control sending unit.  Other devices that might work include a television and remote controlled light(s), as examples.  Of course, both must be tuned to the same communication frequency.

This involves building two .grc flowgraph programs in **GNU Radio Companion** software.  One program records data from the remote control sending unit.  A second program transmits the data to the vehicle (or other device) to command it.  You can copy and modify the record and replay .grc files created in Exercise 270.  As an option, a method for removing unwanted portions of the recorded data is suggested, at least for Linux-OS users.

This excercise assumes the data is exchanged between the remote control and the vehicle using a fixed communication frequency, without encryption.  The method of frequency hopping spread-sectrum (FHSS) is not addressed.

It is necessary to know the frequency of your devices.  You might find the frequency written on your device, in the documentation for your device, or you may perform a web-search using the name and model number of your device.  Otherwise, you can look for it using **GNU Radio Companion** or **GQRX**. Finding the frequency is not discussed any further in this exercise/lesson.

## Record:

`record-rc-car.grc`

```
GUI Range

GUI Range

osmocom source  -->  Band pass filter  -->  Time Sink
                                       -->  File Sink
```

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6` _(You may need more depending on whether the signal fits in the waterfall.)_
- osmocom Source:
  - Ch0: Frequency (Hz): For the in-class example, `49.5e6`. In general, you'll have to figure this out based on the device you're working with. I highly recommend tuning off-center from the signal that you are intending to record. Whatever frequency you pick for recording should match the frequency you pick for replaying.
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
- File sink:
  - File name: Pick using the "...". Make sure to pick a file that does NOT exist. One good name could be `my_car_recording.iqdata`.

## Replay:

`replay-rc-car.grc`

```
GUI Range

File Source  -->  osmocom sink
             -->  Time sink
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
  - Pick your file (must make the recording first).
  
Optionally add a selector in the middle.

## To edit the data file prior to replay (Optional)
Linux OS users might find and use **"inspectrum"** software to edit the data file(s) recorded from the RC vehicled remote control unit.  The software may be available on github.com or another source.  Other software might be found having suitable capabilitiees.  The student or end-user will need to determine the suitability and appropriateness of any software he or she loads.
