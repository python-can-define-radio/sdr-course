# Software Defined Radio (SDR) Course

## Table of Contents (TOC)

### Day 1

<div style=float:left>👨🏽‍🏫</div> 

- ~[What is an SDR][What_is_an_SDR]
- ~[GQRX][GQRX]
    - +Demonstrate Aliasing
    - +Outdoor activity
- ~Introduce GNU Radio Companion
    - ~Saving the file first
    - ~Pitfalls:
        - ~Don't use the "Apply" button
        - ~Searching for program blocks: deselect first, or Ctrl+F always
- 🔬 [Spectrum Analyzer][GRC_Spectrum_Analyzer]
- 🔬 [FM Receiver][GRC_FM_Receiver]
- 🔬 [FM Transmitter][GRC_FM_Transmitter]
- 🔬 [Noise Jammer][Noise_Jammer]

### Day 2

- ~Discussion of flowgraphs from Day 1
- +[Digital Jammer][Digital_Jammer]
- **Intro to Python**
    - ~Exercises #1-#20, #28b, #28c, #28d in [ex_2a_print_and_inputs][ex_2a_print_and_inputs]
    - +Exercises #11-#14 in [ex_3a_if_else][ex_3a_if_else]
    - ~Exercise #5 in [ex_6a_for_loops][ex_6a_for_loops]
    - +Exercise #28 in [ex_6b_while_loops][ex_6b_while_loops]

### Day 3

- **Sample rates**
    - ~[Sample Rates: Turtle Ripples][Sample_Rates_turtle_ripples]
    - +Nyquist Theorem / Criterion:
        1. +We'll start with [a lesson from Harvey Mudd][Harvey_Mudd_Sampling].
        2. +We'll look at the images on [this page from allaboutcircuits.com][all_about_circuits_sampling].
        3. +Watch & discuss [Helicoptor blade video][Helicoptor_aliasing]
    - ~Meaning of FFT using the [GRC showing the sum of two pure sine waves][AnalyzeFreq_of_Combined_Signals]<sup>1</sup>.
        
        
- **On-Off Keying Data Transmission using Python**
    - +OOK Class Activity using light and sound signals
    - +[OOK Intro Using Python: 010_pcdr_ook_tx_intro.md][010_pcdr_ook_tx_intro]
    - +Instructor Receive & Demodulate student msg on URH (Universal Radio Hacker) — Demonstration
    - 🔬 OOK tx intro exercises

- **Automated Signal Strength Scanning using Python**
    - ~[PCDR Simple receiver][pcdr_simple]
    - 🔬 Simple receiver exercises

-----

### If time allows...

- [URH exercises](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/010_Install_URH.md)

#### Footnotes

1: For those who would like to dig into the math and history of the FFT, see [this video from Veritasium][veritasium_fft_video]


<!-- Links below -->


[ex_2a_print_and_inputs]: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_2a_print_and_inputs.md
[ex_3a_if_else]: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_3a_if_else.md
[ex_6a_for_loops]: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_6a_for_loops.md
[ex_6b_while_loops]: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_6b_while_loops.md


[What_is_an_SDR]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/060_What_is_an_SDR.md
[GQRX]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/050_gqrx_FM_Receive.md
[Beginnings]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/010_Beginnings.md
[GRC_Spectrum_Analyzer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_GRC_Spectrum_Analyzer.md
[GRC_FM_Receiver]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_GRC_FM_Receiver.md
[GRC_FM_Transmitter]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/040_GRC_FM_Transmitter.md
[Noise_Jammer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch06_Applications/020_Noise_Jammer.md
[Digital_Jammer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch06_Applications/021_Digital_Jammer.md
[Sample_Rates_turtle_ripples]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/022_Sample_Rates_turtle_ripples.md
[AnalyzeFreq_of_Combined_Signals]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/030_AnalyzeFreq_of_Combined_Signals.md
[010_pcdr_ook_tx_intro]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/010_pcdr_ook_tx_intro.md
[pcdr_simple]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/050_pcdr_simple.md


[Harvey_Mudd_Sampling]: https://gallicchio.github.io/learnSDR/lesson06.html
[all_about_circuits_sampling]: https://www.allaboutcircuits.com/technical-articles/nyquist-shannon-theorem-understanding-sampled-systems/
[Helicoptor_aliasing]: https://www.youtube.com/watch?v=yr3ngmRuGUc
[veritasium_fft_video]: https://www.youtube.com/watch?v=nmgFG7PUHfo
