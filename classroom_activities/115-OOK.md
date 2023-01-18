# On Off Keying

In 056, we transmitted binary data (0 and 1) using On and Off pulses. This is called On Off Keying.

We can visually decode this on a Time Sink or a Waterfall Sink, but wouldn't it be great to have the computer do the work for us?

## Demodulating OOK

We're going to start by creating a Hier Block. There's a lot inside of this Hier block that we'll talk about later. For now, we're just going to build the block, and experiment to see how it works.

Name this `ook_demod.grc`, and since it's a Hier block, **make sure to save it in ~/.grc_gnuradio**.

```
Variable

Parameter

Parameter


Pad    -->  Complex  -->  Moving  --> Add   -->  Binary  --> Keep 1  --> Pad
Source      to Mag        Average     Const      Slicer      in N        Sink
```

Parameters:

- Variable (_already in the flowgraph_) with id `samp_rate`:
  - Delete this block. It is automatically created, but in this case, we do not want it.
- Variable (_the new one_):
  - Id: `moving_average_length`
  - Value: `1000`
- First Parameter:
  - Id: `threshold`
  - Label: `Threshold`
  - Value: `0.2`
  - Type: `Float`
- Second Parameter:
  - Id: `symbol_length`
  - Label: `Symbol Length`
  - Value: `100`
  - Type: `Int`
- Pad Source:
  - Output type: `Complex`
- Moving Average:
  - Type: `Float`
  - Length: `moving_average_length`
  - Scale: `1 / moving_average_length`
- Add Const:
  - Type: `Float`
  - Constant: `-1 * threshold`
- Keep 1 in N:
  - Type: `Byte`
  - N: `symbol_length`
- Pad Sink:
  - Input type: `Byte`
- Options block (_already in the flowgraph_):
  - Id: `ook_demod`
  - Title: `OOK Demod`
  - Generate Options: `Hier Block`

As before, make sure to 

1. Press the "Generate" button
2. Reload the list of blocks

### Testing the OOK Hier block

Create this flowgraph. Name it `OOK_experiment_Demod_1.grc`.

```
GUI Range


Signal   ---┐          ┌-->  Time Sink 
Source      |          |     (first)
            └->        |
                 Add  -┘-->  OOK Demod  -->  UChar to Float  -->  Time Sink
            ┌->                                                   (second)
            |
  Noise   --┘
  Source
```

Parameters:
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- GUI Range:
  - Id: `amplit`
  - Default Value: `0.5`
  - Start: `0`
  - Stop: `1`
  - Step: `0.01`
- Signal Source:
  - Waveform: `Sine`
  - Frequency: `40e3`
  - Amplitude: `amplit`
- Noise Source:
  - Amplitude: `0.1`
- OOK Demod:
  - Symbol Length: `100`
  - Threshold: `0.2`
- Time Sink (first):
  - "General" Tab: 
    * Type: `Complex`
  - "Trigger" Tab:
    * Trigger Mode: `Free`  (i.e., keep the default)
- Time Sink (second):
  - "General" Tab: 
    - Type: `Float`
    - Sample Rate: `samp_rate / 100`
  - "Trigger" Tab:
    * Trigger Mode: `Free`  (i.e., keep the default)

When you run the program, what happens as you adjust the "amplit" slider?
