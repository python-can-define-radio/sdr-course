_Prerequisite: `038-Multiplying-signals.md`_

We want to be able to transmit the generated on-off signal to the Hack RF.

To do so, we need to make a few changes.

## Fixing the types

We can't transmit to the osmocom sink unless the data type is blue (complex).

So, copy the previous flowgraph into a new file called `square_multiplied_complex.grc`

```
Signal  --> Float to  ---┐
Source      Complex      |
                         └->  
                              Multiply  -->  Throttle  -->  Time Sink 
                         ┌->
                         |
        Signal Source  --┘                    
```

_Notes:_ 

- The Square Signal source should be attached to the `re` port on the Float to Complex block.
- The `im` port on Float to Complex should not be connected.

Parameters:

- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `100`
- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `complex`  (**different from before**)
  - Waveform: `Sine`
  - Frequency: `4`
- Multiply:
  - IO Type: `complex`
- Throttle:
  - IO Type: `complex`

## Hiding the details

Now that we have the cycling on and off working, we want to hide some of those details. In most of programming, this is done by defining a function. Here, it's done using a Hier Block.

_If you'd like a visual description of how to work with Hier Blocks, see [here](https://wiki.gnuradio.org/index.php/Hier_Blocks_and_Parameters)._

### The setup

We need a folder in our home directory called `.grc_gnuradio`. Open a terminal, and type this:

```
cd ~
mkdir .grc_gnuradio
```

### Creating the Hier block

Now that we've created that directory, go back to GNU Radio, and open a new file.

Open the "Save As" window. In that window, you may not be able to see the .grc_gnuradio directory that you created. If you can't see it, then press Ctrl+H to show hidden files.

Name the file `mix_sine_wave_hier_block.grc`, and save it in the .grc_gnuradio directory.

Flowgraph:
```
Parameter

Pad     --> Float to  ---┐
Source      Complex      |
                         └->
                              Multiply  -->  Pad Sink 
                         ┌->
                         |
               Signal  --┘
               Source
```

_Notes:_

- The Pad Source should be attached to the `re` port on the Float to Complex block.
- The `im` port on Float to Complex should not be connected.

Parameters:

- Variable (_already in the flowgraph_) with id `samp_rate`:
  - Delete this block. It is automatically created, but in this case, we do not want it.
- Parameter:
  - Id: `samp_rate`
  - Label: `Sample Rate`
  - Type: `Float`
- Pad Source:
  - Output type: `Float`
- Signal Source:
  - Output Type: `complex`
  - Sample Rate: `samp_rate`
  - Waveform: `Sine`
  - Frequency: `20`
- Options block (_already in the flowgraph_):
  - Title: `Mix Sine Wave Hier Block`
  - Generate Options: `Hier Block`

Now, save that file, and press the "Generate" button (right next to run).

Generate won't show any messages or evidence of success. To see it work, move on to the next section.

### Using your custom-built hier block

Congratulations, you've built your first block! Now we're going to use it.

Make a new file called `square_cycle.grc`.

Use Ctrl+F to search for "Mix Sine". You will NOT see the block you created. You need to press the "Reload Blocks" button on the toolbar. (It looks like a "Refresh" button). Then, search again.

Create this flowgraph:

```
Signal Source  -->  Mix Sine Wave Hier Block  -->  Throttle  -->  Time Sink 
```

- Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Mix Sine Wave Hier Block:
  - Sample Rate: `samp_rate`
- Time Sink:
  - Number of Points: `int(samp_rate * 4)`
  - Update Period: `15`

Run that. It should display a wave that pulses on and off, just like the file `square_multiplied_complex.grc` that we created above. The advantage is that we have now hidden the details of the on-off pulsing so that we can focus on the big picture.

In the next activity, we'll connect this to the Hack RF.

Optional Exercises:

- Make the frequency of the Signal Source slidable. 
- Make the frequency of the On Off Cycle Hier Block slidable.
