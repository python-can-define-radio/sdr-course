- First:
  - Vector source to all the sinks.
  - Give the students the vector: [0, 0.7071, 1, 0.7071, 0, -0.7071, -1, -0.7071]
    - Note: might be wrong vector; need to figure that out.
  - Ask them to interpolate in whatever way they want.
  - What is the frequency of the wave?
  - Trick question: does interpolating change the frequency?

- Second:
  - for OOK:  whatever --> Complex to Float --(real part) -->  Abs  -->  whatever



--------------------

--------------------

An idea from approx Sept 1 2022. May or may not keep. Not finished typing. Sheet is in my room.

Tx:

Vector source
0, 0.2, 0.4, 0.6, 0.8, 1.0     -->    Repeat: int(samp_rate)     --->   mult  --> Time sink
                                                       sig 50 kHz -->         --> osmocom
                                                       
Time sink set to show points


Rx:

osmocom
 gains 0, 24, 24
 centered at same as TX    -->
****