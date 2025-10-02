<!-- pandoc-only % SDR: Fundamentals -->
# Fundamentals  <!-- pandoc-exclude-line --> 

<!--
Note regarding what goes in the quad chart:

Action: Discuss the fundamentals of Software Defined Radios (SDRs).
Standard: Students will be able to explain fundamentals of SDRs.


Evaluation: Check on Learning
-->

<!-- pandoc-only ### Purpose -->

<!-- pandoc-only The purpose of this lesson is to discuss the fundamentals of Software Defined Radios (SDRs). -->

<!-- pandoc-only ### Outcome -->

<!-- pandoc-only Students will be able to explain fundamentals of Software Defined Radios (SDRs). -->

### Introduction

For thousands of years, people have been trying to communicate information across long distances. Today, radio waves are how we commonly solve the long distance communication problem, but how they work is a mystery to most people. In this SDR class, we'll explore foundational concepts and then apply these concepts by transmitting and receiving signals.

<!-- pandoc-only ### Learning Step Activities -->
### Topics outline: <!-- pandoc-exclude-line --> 

- <!-- pandoc-only LSA 1: --> Binary
- <!-- pandoc-only LSA 2: --> Modulation: ASK, FSK, PSK
- <!-- pandoc-only LSA 3: --> Sample rates

<!-- pandoc-only # LSA 1: Binary -->

### Binary

Computers store data using binary, which is the simplest possible number system: everything is either "zero" or "one". There are lots of ways to communicate zeros and ones:

- Sound / beeps (similar to Morse code)
- Printed dark and light dots (QR codes)
- Printed dark and light stripes (Bar codes)

<!-- pandoc-only ### Binary -->

In the case of a QR code, the process looks like this:

- Modulation: the binary data (zeros and ones) are turned into an image using a QR code generator, and possibly printed on paper.
- Demodulation: a camera captures the light and dark spots, converting them back into bits (zeros and ones).

<!-- pandoc-only ### Binary -->

Exercise: Can you identify the zeros and ones in this QR code?

![QR Code](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/qrcode.png?raw=true)

<!-- pandoc-only # LSA 2: Modulation -->

### ASK, FSK, and PSK Modulations

When trying to communicate bits using an Electromagnetic (EM) wave, there are three common approaches, as shown in this video.

[Digital modulation: ASK, FSK, and PSK](https://www.yout-ube.com/watch?v=qGwUOvErR8Q) (5:29)

### Exercises: Modulation

For all of the following exercises, the instructor will provide four blank graphs with the time axes aligned.  

_Recommendation: use vertical dotted lines to help with aligning in time._

<!-- pandoc-only ### Exercises: Modulation -->

Using time as your x-axis, draw the following:  

- On the first graph, draw the carrier wave.
- On the second graph, draw the message using a square wave whose amplitude is either 50% or 100%.
  - Use 100% amplitude for ones, and 50% amplitude for zeros.
- On the third graph, modulate your message onto the carrier wave using ASK.
- On the fourth graph, draw the message on a waterfall/spectrogram.

### Exercise: Modulate using ASK

1. - Carrier wave's frequency: 2 cycles per second (Hz)
   - Message: 10110
   - Time per bit: 1 second

<!-- pandoc-only ### Exercise: Modulate using ASK -->

2. - Carrier wave's frequency: 3 Hz
   - Message: 110100
   - Time per bit: 1 second

<!-- pandoc-only ### Exercise: Modulate using ASK -->

3. - Carrier wave's frequency: 4 Hz
   - Message: 01011
   - Time per bit: 0.5 seconds

<!-- pandoc-only ### Exercise: Modulate using ASK -->

4. - Carrier wave's frequency: 0.5 Hz
   - Message: 10010001
   - Time per bit: 2 seconds

<!-- pandoc-only ### Exercise: Modulate using ASK -->

5. - Carrier wave's frequency: 4 Hz
   - Message: 0011010
   - Time per bit: 1 second
   - Question: what is the special name for this type of ASK when the low amplitude is the same as not transmitting (0% of the carrier)? (Answer in teacher notes)

### Purpose?

Before we move on, let's review: **Why are we doing this?**

<!--- pandoc-only ### Purpose! -->

Answer: tomorrow, we're going to record a signal from an RC Car and manipulate it. These exercises provide a framework for understanding the signal.

### Exercise: Modulate using FSK

6. - Carrier wave's frequency: 1.5 Hz
   - Message: 10110
   - Use the high frequency to represent ones.
   - High frequency: 2 Hz
   - Low frequency: 1 Hz
   - Time per bit: 1 second
   
<!-- pandoc-only ### Exercise: Modulate using FSK -->

7. - Carrier wave's frequency: 2 Hz
   - Message: 0100110
   - Use the high frequency to represent ones.
   - High frequency: 3 Hz
   - Low frequency: 1 Hz
   - Time per bit: 1 second

<!-- pandoc-only ### Exercise: Modulate using FSK -->

8. - Carrier wave's frequency: 7 Hz
   - Message: 00101
   - Use the high frequency to represent ones.
   - High frequency: 10 Hz
   - Low frequency: 4 Hz
   - Time per bit: 0.5 seconds

<!-- pandoc-only ### Exercise: Modulate using FSK -->

9. - Carrier wave's frequency: 1.75 Hz
   - Message: 101001
   - Use the high frequency to represent ones.
   - High frequency: 3 Hz
   - Low frequency: 0.5 Hz
   - Time per bit: 2 seconds

<!-- pandoc-only ### Exercise: Modulate using FSK -->

10. - Carrier wave's frequency: 15 Hz
    - Message: 1010101
    - Use the high frequency to represent ones.
    - High frequency: 20 Hz
    - Low frequency: 10 Hz
    - Time per bit: 0.1 seconds

### Exercise: Modulate using PSK

11. - Carrier wave's frequency: 2 cycles per second
    - Message: 1011011
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 1 second

<!-- pandoc-only ### Exercise: Modulate using PSK -->

12. - Carrier wave's frequency: 6 Hz
    - Message: 01101
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.5 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

13. - Carrier wave's frequency: 5 Hz
    - Message: 101100
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.2 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

14. - Carrier wave's frequency: 10 Hz
    - Message: 01101
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.1 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

15. - Carrier wave's frequency: 30 Hz
    - Message: 01101
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.1 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

16. - Carrier wave's frequency: 100 Hz
    - Message: 110100
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.01 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

17. - Carrier wave's frequency: 200 Hz
    - Message: 110100
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 0.01 seconds

<!-- pandoc-only ### Exercise: Modulate using PSK -->

18. - Carrier wave's frequency: 1 kHz
    - Message: 01011
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 1 millisecond

<!-- pandoc-only ### Exercise: Modulate using PSK -->

19. - Carrier wave's frequency: 2 kHz
    - Message: 10100
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 1 millisecond

<!-- pandoc-only ### Exercise: Modulate using PSK -->

20. - Carrier wave's frequency: 3 MHz
    - Message: 10100
    - Phase for zeros: 180°
    - Phase for ones: 0°
    - Time per bit: 1 microsecond

<!-- pandoc-only # LSA 3: Sample rates -->

### Sample rates

We have been drawing these signals as continuous waves. This is an accurate way to portray them while they are in transit, but on a computer, the waves are represented as a sequence of measurements or "samples".

### Why learn about sample rates?

When a Software Defined Radio (SDR) measures signals, it takes a certain number of measurements every second. The number of measurements per second is called the **sample rate**. For example, the Hack RF One is able to measure as many as `20 Million samples per second`, or `20 Msps`. Understanding the idea of sampling will guide us when choosing our sample rate. 

### Exercises

- The instructor will provide two vertically-stacked plots.
  - Then for the given parameters,
    - In the first plot, draw the wave, and draw some evenly-spaced dots on the wave to represent sampling the wave.
    - Determine the sample rate.
    - In the second plot, reconstruct the wave using only the dots.
    - Repeat each exercise with three students (different sample rates)
       - At least one of the chosen sample rates should demonstrate **undersampling** (taking too few samples per second) and **aliasing** (measuring the wrong frequency as a result of undersampling).

### Exercises

1. Draw 1 second of a 1 Hz wave. 
2. Draw 0.1 seconds of a 20 Hz wave.
3. Draw 0.01 seconds of a 300 Hz wave.
4. Draw 1 millisecond of a 2 kHz wave.
5. Draw 1 microsecond of a 4 MHz wave.
6. Draw 1 nanosecond of a 2 GHz wave.

### Endnotes

#### Regarding the term ASK:

- Since the exercises in this lesson use one bit per symbol, it would be more precise to say "BASK" or "2ASK" rather than simply "ASK". The "B" ("Binary") refers to the use of only two amplitudes. It is possible to do 4-ASK, as shown on the table that follows.

<!-- pandoc-only ### Endnotes: 4-ASK Table -->

| Strength | Bit sequence |
|----------|--------------|
| 25%      | 00           |
| 50%      | 01           |
| 75%      | 10           |
| 100%     | 11           |

<!-- pandoc-only ### Endnotes: Regarding the term ASK -->

- Using four different transmission strengths doubles the amount of data sent per second, but makes it more difficult for the receiver to demodulate in the presence of noise. In practice, "ASK" usually refers to "2ASK"; we believe that this is because 2ASK is far more common than other ASK variants.

### Regarding FSK:

**Terminology**: For the FSK exercises in this lesson, it would be more precise to say "BFSK" or "2FSK", but just as 2ASK is almost always abbreviated to simply ASK, 2FSK is usually called just FSK.  

**Regarding the FSK carrier wave frequency:** FSK uses multiple frequencies.it's not obvious which one should be called the "carrier". We chose to refer to the median. Be aware of this ambiguity when using software to work with FSK.

<!-- pandoc-only ### Summary -->

<!-- pandoc-only In summary, you learned: -->

<!-- pandoc-only - Binary -->
<!-- pandoc-only - Modulation: ASK, FSK, PSK -->
<!-- pandoc-only - Sample rates -->

<!-- pandoc-only ### References -->

<!-- pandoc-only - https://gallicchio.github.io/learnSDR/ -->
