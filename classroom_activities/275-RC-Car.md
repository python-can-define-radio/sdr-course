_Note: This overlaps significantly with Exercise 270. We plan to merge the two, but for now, we recommend reading both.
       To work here, you can copy, modify, and use the record and replay .grc files created in Exercise 270._
## Summary
This project requires the user to have a functional remote-controled (RC) vehicle and its remote controller.  Optionaly, you may use another remote controlled device and an appropriate remote control sending unit.  Other devices that might work include a television and remote controlled light(s), as examples.  Of course, Both must be tuned to the same communication frequency.

This involves building two .grc flowgraph programs in **GNU Radio Companion** software.  One program records data from the remote control sending unit.  A second program transmits the data to the vehicle (or other device) to command it.  You can copy and modify the record and replay .grc files created in Exercise 270.  As an option, a method for removing unwanted portions of the recorded data is suggested, at least for Linux-OS users.

This excercise assumes the data is exchanged between the remote control and the vehicle using a fixed communication frequency, without incription.  The method of frequency hopping spread-sectrum (FHSS) is not addressed.

It is necessary to know the frequency of your devices.  You might find the frequency written on your device, in the documentation for your device, or you may perform a web-search using the name and model number of your device.  Otherwise, you can look for it using **GNU Radio Companion** or **GQRX Radio software** Finding the frequency is not discussed any further in this exercise/lesson.

## Record:

`record-rc-car.grc`

```
GUI Range

GUI Range

osmocom source  -->  Band pass filter  -->  Time Sink
                                       -->  File Sink
```

Parameters:

GUI Range (First):
- Id: `IFGain`
- 0 to 40, steps of 8

GUI Range (Second):
- Id: `BBGain`
- 0 to 62, steps of 2

osmocom source:
- 49.5e6

File sink:
- File name: something like my_car_recording.iqdata



## Replay:

`replay-rc-car.grc`

```
File Source  -->  osmocom sink
             -->  Time sink
```

Optionally add a selector in the middle.

## To edit the data file prior to replay (Optional)
Linux OS users might find and use **"inspectrum"** software to edit the data file(s) recorded from the RC vehicled remote control unit.  The software may be available on github.com or another source.  Other software might be found having suitable capabilitiees.  The student or end-user will need to determine the suitability and appropriateness of any software he or she loads.
