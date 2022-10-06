# Sample rates: GNU Radio practice

## Practice problem set A

Make this flowgraph. Name it `messy_sine_vector_source.grc`.

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

## Practice problem set B

Copy and modify the previous flowgraph. Save the new copy as `square_vector_source.grc`.

1. Change the `Vector` in the Vector Source so that it outputs a square wave. It should look like this:

```
     •••••     •••••     •••••

•••••     •••••     •••••     
```

(Since the Vector Source repeats, you only need to type the Vector for a single cycle.)

2. Change the square wave so that it has a frequency of 2 Hz.
3. For this square wave with a frequency of 2 Hz, how many seconds does it take to complete a full cycle?
4. Given that the sample rate is 40 sps (samples per second), then how many **samples** does this 2 Hz square wave require to complete a full cycle?
