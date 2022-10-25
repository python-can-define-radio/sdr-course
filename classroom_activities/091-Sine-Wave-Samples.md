_Note: This exercise isn't finished, but it is still useful._

## sample_rates_one.grc

```
GUI Range

Signal Source  --->  Throttle  --->  Time Sink
                               --->  Waterfall Sink
                               --->  Frequency Sink
```

### Parameters:

- GUI Range:
  - Id: `sigfreq`
  - Default: `3`
  - Start: `1`
  - Stop: `5`
  - Step: `1`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `30`
- Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `sigfreq`
- Throttle:
  - Type: `float`
  - Sample Rate: `40000`
- Time Sink:
  - "General" Tab:
    - Type: `float`
    - Number of Points: `30`
    - Y min: `-4`
    - Y max: `4`
  - "Trigger" Tab:
    - Trigger Mode: `Normal`
  - "Config" Tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`
- Waterfall Sink:
  - Type: `Float`
  - Spectrum Width: `Half`  (_Note: This option only appears after you've picked Float for the type_)
- Frequency Sink:
  - Type: `Float`
  - Spectrum Width: `Half`
  - Y Min: `-110`


# FAQ

- Q: What does the Throttle do?  
  A: It keeps the processor from maxing-out. GNU Radio tries to run the simulation as quickly as possible, that is, as quickly as the computer is capable. The Throttle tells it to slow down. Feel free to try raising or lowering the Sample Rate in the Throttle. You'll see that for lower rates (say, `200`), the graphical display updates less frequently. The ideal Throttle setting is one that ...  
    (a) is high enough to see display updates frequently, and  
    (b) is low enough that the processor is able to handle the workload.
- Q: What is the difference between `Float` and `Complex`?  
  A: We'll discuss more later, but for now, know this:  
   -  Float has only one part (the real part), while Complex has two parts (real and imaginary). That means that in a Time Sink, Float shows one curve, while Complex would show two.

# Exercises

1. How many total data points are displayed in the Time Sink?
2. How many seconds are shown on the horizontal axis of the Time Sink?
3. When the frequency is 3 Hz, how many cycles do you see in the Time Sink?
4. How many data points (a.k.a. "samples") are there in a single cycle when the frequency is 3 Hz?
