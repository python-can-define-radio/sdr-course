# SDRangel

Start with this video: [One to rule them all - Crossplatform SDR decoder - SDRANGEL - short review and examples](https://www.youtube.com/watch?v=zrhBcy8L-dA)

### Basics of Hack RF receiving:

1. Launch SDR Angel.
2. Set up a Hack RF in Receive mode.
3. Tune in to a broadcast FM station.
4. Try a variety of sample rates. What does this setting do?
5. Try adjusting the gains (they are named __ and __).
6. Try a variety of bandwidths. What does this setting do?
    1. Why would you want to adjust the bandwith? Answer: to avoid aliasing.

### Receiving Broadcast FM
7. Create a broadcast FM receiving channel.
8. Try adjusting the frequency on which you are receiving.
9. Try adjusting the band-pass filter.
10. Try the Radio Data Service (RDS).

### Receiving Narrow FM
11. Create a Narrow FM receiving channel.
12. ...

### Saving a Workspace
13. ...

### Preparing to Transmit
13. Close all subwindows, but keep SDRAngel open.
14. Set up a Hack RF in Transmit mode.

### Transmitting Wide FM
15. Create a Wide FM transmit channel.
16. Try the Morse Code (CW) feature.
17. Try setting the audio device.

### Transmitting Wide FM from an audio file
18. First, you'll need to convert the audio file of interest to `.raw`,  which is documented [here](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch03_Misc_examples/soundFile.md#convert-a-wav-file-to-raw) in the Python course.  
19. After converting the file, pick it in the [WFM Modulator](https://github.com/f4exb/sdrangel/blob/master/plugins/channeltx/modwfm/readme.md) subwindow.

### Transmitting two Wide FM channels simultaneously
20. Create another Wide FM transmit channel.
21. Pick another sound file, or set it to transmit Morse.
22. Set it to a different frequency.

### Transmitting text using ChirpChat
23. Create a ChirpChat transmit channel.
24. ...

### Receiving text using ChirpChat
25. Create a ChirpChat receive channel.
26. ...


----

### Other videos

https://www.youtube.com/watch?v=kBuGDshziMg
