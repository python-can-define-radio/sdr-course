# Software Defined Radio (SDR) Course

## Table of Contents (TOC)

### Day 1

- Overview slides
- Distribute equipment
- Terminal tutorial
- Set up Thonny and VS Code on laptops
- Verify GQRX and GRC can start on laptops
- Python print and inputs exercises: #1-#20, #28b, #28c, #28d

### Day 2

- Demo: Turning on a HackRF transmitter using pcdr module (and GQRX to receive)
- Do: (same) (show GQRX on board)
- GQRX FM Receive
- SDR Angel
- Discussion: Underworkings of Python, libraries
  - What happens when an "import" is done
  - the logics of different Python "things"
- take turns transmitting / receiving to each other on the Broadcast FM band.
- Check out waveforms if possible, WiFi, Bluetooth, GSM? CDMA?

### Day 3
- Python if-else exercises 6 through 16c
  - For students who are ahead, do the for-loops exercises
- "cool": Gpredict
- GQRX Keyfob demo. Talk about non-standardized dB units (it's not dBm)
- Python Keyfob
- Python pcdr basic Rx strength: reiterate non-standardized unit
- Python while loop to repeatedly read
- Python while loop exercises #1 - #9
- Optional Homework: Finish if-else exercises

### Day 4

- Incorporate PCDR module
  - [Single frequency transmitter](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/005_pcdr_single_freq_transmit.md): work through together
  - [Single frequency receiver](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/050_pcdr_simple_receiver.md):
    - Demo first exercise. GQRX open to confirm functionality.
    - Have students work independently up to exercise #9.
- Incorporate playsound
  - Some students may hit the installation requirement challenge
- Incorporate file writing/naming:
  - .csv file
  - writing to a file
  - When/why we need to flush to a file
- Incorporate time functions (nowtime/datetime)
- _Lunch_
- FM Transmitter using Python/PCDR
- FM Receiver using Python/PCDR
- Homework:
  - Successfully write an activity detector that...
    - Takes continuous measurements of the strength of a specified frequency
    - Records data to a csv file with ability to view immediately (i.e., flush to file)
    - Plays three different sounds depending on RSSI (low|med|high strength measured)

### Day 5

- Tone-varying DF tool built in Python; go outside
- _Lunch_
- URH:
  - Record and Replay
  - Modulation: OOK, ASK, FSK (as time allows)
--------

### Weather-dependent

DF with Yagi-uda

### Other

- GRC: Noise jammer
  
<!-- Links below -->

