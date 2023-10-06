# Introduction to Receving in Python

ℹ️ This material coincides with material from python slideshows B (slides 1-11, 16, 24, 39, 54-63, 69) C (slides 30-38) and D (slides 4-15, 31-37), and SDR slideshow A (slides 22, 25, 28-32, 40-42).

There are at least three challenges that arise on the receiving end:

- Noise
- Signal strength variation
- Timing

We'll address each of these in more detail, but first, we'll examine a minimal simulated receiver. Then, for those who have SDR hardware, we'll receive some data from the air.

```python3
receiver = gnuradio_
while True:
    TODO: get some data

```

- TODO: Plot FFT
- TODO: What is maximum frequency in FFT?
- TODO: Which frequencies in FFT surpass some threshold?

-------

TODO: discuss harmonics and reflections (note that the latter is not the proper term. Referring to a signal appearing in multiple locations on an FFT.)
