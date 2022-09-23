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

`record-rc-car.grc`

```
File Source  -->  osmocom sink
             -->  Time sink
```

Optionally add a selector in the middle.
