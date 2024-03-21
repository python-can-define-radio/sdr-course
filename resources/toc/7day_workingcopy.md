# Software Defined Radio (SDR) Course

### Table of Contents (TOC)

#### Day 1

<div style=float:left>👨🏽‍🏫</div> 

- [Beginnings][010_Beginnings]

<div style=float:left>🔬</div>

- [FM Receiver][030_GRC_FM_Receiver]
- [FM Transmitter][040_GRC_FM_Transmitter]

### Day 2

- [GQRX][050_gqrx_FM_Receive.md]
- [Spectrum Analyzer][020_GRC_Spectrum_Analyzer]

- Go outside

### Day 3

<div style=float:left>👨🏽‍🏫</div> 

- Review / continue discussion of Spectrum Analyzer
- 🧠 PE 1: Spectrum Analyzer
- Discuss [FM Receiver][030_GRC_FM_Receiver]
  - Sub-point: discuss how the hardware filter helps to avoid aliasing

- Independent work time to experiment with what we've learned so far.
  For those who wish to work ahead, look at these. Start from the top of whichever chapter you find interesting.
    - [Ch03 URH][Ch_URH]
    - [Ch04 Python][Ch_Python]
    - [Ch06 Applications][Ch_Applic]

### Day 4

- B1:  
  Review of FM Receiver  
  🧠 PE 2: FM Receiver
- B2: Go outside
- B3: (Same)
- B4: (Same)

### Day 5

- B1: Discuss [Noise Jammer][020_Noise_Jammer]
- B2: URH
    - Incorporate RC Car with URH:
         1. Simple Record and Replay
         2. Demodulate and generate:
             - Record (Make sure you're offset to avoid DC Spike)
             - Demod (Get zeros and ones; use URH's Generate tab to verify)
             - Generate and Transmit using Python [pcdr OOK transmit][010_pcdr_ook_tx_intro]
             - Use GUIZero to create up/down/left/right buttons to control car
- B3: (Same)
- B4: (Same)

### Day 6

- B1:  
  Review of Noise jammer  
  🧠 PE 3: Noise Jammer
- B2: Discuss [PSK Digital Jammer][021_Digital_Jammer] 
- B3:
  Review Digital Jammer  
  🧠 PE 4: Digital Jammer
- B4: Independent work time

### Day 7

- B1: Test Preparation; AAR
- B2: Independent work time
- B3: 🧠 SDR Exam
  

[010_Beginnings]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/010_Beginnings.md
[050_gqrx_FM_Receive.md]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/050_gqrx_FM_Receive.md
[060_What_is_an_SDR]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/060_What_is_an_SDR.md
[020_GRC_Spectrum_Analyzer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_GRC_Spectrum_Analyzer.md
[030_GRC_FM_Receiver]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/030_GRC_FM_Receiver.md
[040_GRC_FM_Transmitter]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/040_GRC_FM_Transmitter.md
[010-Transmit-and-Receive-Pure-Sine]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/010-Transmit-and-Receive-Pure-Sine.md
[011_numpy]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/011_numpy.md
[012_matplotlib]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/012_matplotlib.md
[020_Sample_Rates_Intro]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/020_Sample_Rates_Intro.md
[021_Sample_Rates_CPU_temps]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/021_Sample_Rates_CPU_temps.md
[022_Sample_Rates_turtle_ripples]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/022_Sample_Rates_turtle_ripples.md
[023_Sample_Rates_py_practice]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/023_Sample_Rates_py_practice.md
[024_Sample_Rates_grc_practice]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/024_Sample_Rates_grc_practice.md
[025_Sample_Rates_RepeatBlock]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/025_Sample_Rates_RepeatBlock.md
[026_Sample_Rates_RealisticData]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/026_Sample_Rates_RealisticData.md
[027_Interpolation_and_Decimation]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/027_Interpolation_and_Decimation.md
[030_Oversampling_Undersampling]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/030_Oversampling_Undersampling.md
[040_Unicode_and_File_Source]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/040_Unicode_and_File_Source.md
[099_Additional_Practice]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/099_Additional_Practice.md
[Ch_URH]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/

[010_Install_URH]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/010_Install_URH.md
[020_Modulation]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md
[030_Generate_a_signal]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/030_Generate_a_signal.md
[040_Interpret_unknown_signal]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/040_Interpret_unknown_signal.md
[050_Interpret_unknown_noisy_signal]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/050_Interpret_unknown_noisy_signal.md
[060_Cropping_a_signal]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/060_Cropping_a_signal.md
[070_Interpret_multiple_noisy_signals]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/070_Interpret_multiple_noisy_signals.md
[080_Interpret_multiple_noisy_signals]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/080_Interpret_multiple_noisy_signals.md
[090_Record_a_real_signal]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/090_Record_a_real_signal.md
[020_Noise_Jammer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch06_Applications/020_Noise_Jammer.md
[Ch_Python]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/
[010_pcdr_ook_tx_intro]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/010_pcdr_ook_tx_intro.md
[020_pcdr_ook_waves]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/020_pcdr_ook_waves.md
[030_pcdr_frequency_domain_Real]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/030_pcdr_frequency_domain_Real.md
[040_pcdr_frequency_domain_Complex]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/040_pcdr_frequency_domain_Complex.md
[050_pcdr_simple]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/050_pcdr_simple.md
[Ch_Applic]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch06_Applications/
[021_Digital_Jammer]: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch06_Applications/021_Digital_Jammer.md
