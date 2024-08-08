# Additional Practice

_The instructor may choose to incorporate these exercises._

### Sampling basics

1. Draw an arbitrary function, i.e., a hand-drawn curve that isn't based on a formula. 
2. Have a student take samples of the function with a given sample rate. 
3. New student and new sample rate.
4. Change the number of seconds shown on the time axis (the x-axis) after a few students. Change more often as the exercise progresses.

### Frequency domain

1. Draw a sinusoidal function.
2. Have a student draw the frequency domain.
3. Repeat with other students.
4. As before, change the time axis (of the time domain representation) during the exercise.

### Frequency domain, multiple components

1. Do the previous exercise again with a function that has two frequency components.
   - To ensure that the frequencies will be visually distinguishable, the lower frequency should be either 2 Hz or 3 Hz, and the higher frequency should be an integer multiple at least 5 times larger. Examples:
     - 2 Hz and 10 Hz; 2 Hz and 12 Hz; 2 Hz and 14 Hz, etc
     - 3 Hz and 15 Hz, 3 Hz and 18 Hz; 3 Hz and 21 Hz, etc

### Minimum sample rate

1. Draw a sinusoidal function.
2. Have students take samples at a sample rate that is at least 20 times the frequency of the wave.
3. Erase the original wave, and reconstruct the wave from the samples.
4. Draw the original and the reconstruted in the frequency domain. (They should be the same until you reach the point of aliasing).
5. Repeat the process for lower and lower sample rates.
6. Point out that even when the wave is very roughly represented, it still has the right _frequency_ as long as `samp_rate > 2*signal_freq`.

### Downconversion

1. Draw a sinusoidal function with a frequency of 12 Hz.
2. Ask a student to draw the function downconverted by 10 Hz.
  - For simplicity, let's assume the downconverted wave starts at the origin. <sup>footnote 1</sup>
3. Repeat with a frequency of 13 Hz, 14 Hz, and as many examples as desired. Make sure to try 10 Hz to show that it downconverts to 0 Hz.

### Upconversion

1. Draw a sinusoidal function with a frequency of 2 Hz.
2. Ask a student to draw the function upconverted by 10 Hz.
3. Repeat with a frequency of 3 Hz, 4 Hz, and as many examples as desired. Make sure to try 0 Hz (i.e., a non-zero constant) to show that it upconverts to 10 Hz.

### Downconversion and the basics of IQ data

Ask the class what happens if you try to downconvert 9 Hz by 10 Hz. They may say you can't do it. This leads us IQ data.

1. Draw a sinusoidal function with a frequency of 12 Hz.
2. Ask a student to draw the function downconverted by 10 Hz using a real wave and an imaginary wave, with the imaginary wave 90 degrees behind the real wave.
   - Ideally, use different colors to distinguish, but you can use a dotted line if necessary.
   - As before, let's assume the real wave starts at the origin. <sup>footnote 1</sup>
   - The real wave is called the "in-phase" (I) part of the signal, and the imaginary wave is called the "quadrature" (Q) part of the signal. This is the origin of the name "IQ data".
3. Repeat with a frequency of 13 Hz, 14 Hz, and as many examples as desired.
4. Downconvert a 8 Hz wave. (It will become a negative 2 Hz wave, which is expressed with the imaginary part 90 degrees **before** the real part.)

Footnote 1: For this beginner level, we're ignoring any phase shifts caused by downconversion. If you go deeper into learning SDRs, know that the IQ wave that we draw may be phase-shifted from what really happens inside of the SDR peripheral. However, the downconversion result is otherwise accurate.
