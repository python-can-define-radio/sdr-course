_Note: This overlaps significantly with exercise 270. We plan to merge the two, but for now, we recommend reading both.
       To work here, you can copy, modify, and use the record and replay .grc files created in exercise 270._
## Summary
This project requires the user to have a functional remote-controled (RC) vehicle and its remote controller.  Optionaly, you may use another remote controlled device and an appropriate remote control sending unit.  Other devices that may be used include a television and remote controlled light(s), as examples.  Of course, Both must be tuned to the same communication frequency.

This involves building two flowgraphs.  One program to record data from the remote control.  A second to transmit the data to the vehicle (or other device).  You can copy and modify the record and replay .grc files created in exercise 270.

It is necessary to know the frequency of your devices.  You might find the frequency written on your device, in the documentation for your device, or you may perform a web-search using the name and model number of your device.  Otherwise, you can look for it using **GNU Radio Companion** or **GQRX Radio software** Finding the frequency is not discussed any further in this exercise/lesson.

## Record:

`record-rc-car.grc`

```
GUI Range

GUI Range

osmocom source  -->  DC Blocker  -->  Time Sink
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
