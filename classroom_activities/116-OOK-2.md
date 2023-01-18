# Simulating transmitting and receiving

We're going to combine `056` and `058` to make a simulation of transmit and receive.

## OOK Transmit Hier Block

In `056`, we used the Repeat and Mix Sine Wave blocks to make the data ready to send. Let's put those into a single block.

Name this `ook_mod.grc`, and save it in the `.grc_gnuradio` directory.

```
Parameter

Parameter

Parameter

Pad Source  -->  Repeat  -->  Mix Sine Wave Hier Block  -->  Pad Sink
```

Parameters:

- Variable (_already in the flowgraph_) with id `samp_rate`:
  - Delete this block. It is automatically created, but in this case, we do not want it.
- First Parameter:
  - Id: `samp_rate`
  - Label: `Sample Rate`
  - Value: `0`
  - Type: `Float`
- Second Parameter:
  - Id: `frequency`
  - Label: `Frequency`
  - Value: `40e3`
  - Type: `Float`
- Third Parameter:
  - Id: `symbol_length`
  - Label: `Symbol Length`
  - Value: `100`
  - Type: `Int`
- Pad Source:
  - Output type: `Float`
- Repeat:
  - Type: `Float`
  - Interpolation: `symbol_length`
- Mix Sine Wave Hier Block:
  - Frequency: `frequency`
  - Sample Rate: `samp_rate`
- Options block (_already in the flowgraph_):
  - Id: `ook_mod`
  - Title: `OOK Mod`
  - Generate Options: `Hier Block`

## Full OOK Simulation

Putting it all together:

Title: `Full_OOK_simulation.grc`

```
Vector  --->  OOK Mod    --->  OOK Demod  --- 
Source   |                |                 |
         |                |                 |
         ---> Time        --->  Time        --->  UChar to  -->  Time
              Sink              Sink              Float          Sink
              (First)           (Second)                         (Third)
```

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Time Sink (First):
  - Name: `"Original Data"`
  - Sample Rate: `1`
  - Number of Points: `20`
- OOK Mod:
  - Frequency: `70e3`
  - Sample Rate: `samp_rate`
  - Symbol Length: `int(1e6)`
- Time Sink (Second):
  - Name: `"Wavey Data"`
- OOK Demod:
  - Symbol Length: `int(1e6)`
  - Threshold: `0.2`
- Time Sink (Third):
  - Name: `"Demodulated Data"`
  - Sample Rate: `1`
  - Number of Points: `20`
