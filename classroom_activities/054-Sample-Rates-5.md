## Sample rate GNU Radio practice

Make this flowgraph:

```
Vector Source  -->  Time Sink
```

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `40`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0.0, 2.3, 5, 10.3, 12.2, 12.5, 13.5, 15, 14, 4, 0, -9, -11, -12.5, -15, -16, -14.2, -12.5, -10, -5]`
  - Repeat: `Yes`
- Time Sink:
  - General tab:
    - Type: `float`
    - Number of Points: `80`
    - Y min: `-20`
    - Y max: `20`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

You'll see the same messy sine wave from the previous exercise, but repeated four times.

Exercises:
1. Change the Number of Points to 40. Then try 160.
2. What should the Number of Points be to show only one cycle of the wave?
3. How much time does a full cycle take?

Answers:

TODO
