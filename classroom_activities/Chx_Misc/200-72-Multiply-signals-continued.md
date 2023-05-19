We want to be able to transmit the generated on-off signal to the Hack RF.

To do so, we need to make a few changes.

## Fixing the types

We can't transmit to the osmocom sink unless the data type is blue (complex).

We're also going to include a slider (a.k.a. GUI Range).

Create a file called `square_multiplied_complex.grc`:

```
GUI Range


Signal  --> Float to  ---┐
Source      Complex      |
                         └->  
                              Multiply  -->   Time Sink 
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
- GUI Range:
  - Id: `frequency`
  - Default Value: `20`
  - Start: `2`
  - Stop: `20`
  - Step: `1`
- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `complex`
  - Waveform: `Sine`
  - Frequency: `frequency`
- Multiply:
  - IO Type: `complex`


<details>
<summary>
  <i>Why change the Frequency?</i>
</summary>
  In the previous exercise, we used `4 Hz` as the frequency because it was easier to draw on paper.
  
  Here, we make the frequency slidable to practice seeing different frequencies.
  
  When we transmit this to the Hack RF, we'll use a much higher frequency. We'll discuss the details of why in a later section.
</details>

## Hiding the details

Now that we have the cycling on and off working, we want to hide some of those details. In most of programming, this is done by defining a function. Here, it's done using a Hier Block.

_If you'd like a visual description of how to work with Hier Blocks, see [here](https://wiki.gnuradio.org/index.php/Hier_Blocks_and_Parameters)._


### Creating the Hier block

Create a new file in GNU Radio Companion. Name the file `mix_sine_wave_hier_block.grc`.

Flowgraph:
```
Parameter

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
- First Parameter:
  - Id: `samp_rate`
  - Label: `Sample Rate`
  - Value: `0`
  - Type: `Float`
- Second Parameter:
  - Id: `frequency`
  - Label: `Frequency`
  - Value: `20`
  - Type: `Float`
- Pad Source:
  - Output type: `Float`
- Signal Source:
  - Output Type: `complex`
  - Sample Rate: `samp_rate`
  - Waveform: `Sine`
  - Frequency: `frequency`
- Options block (_already in the flowgraph_):
  - Id: `mix_sine_wave_hier_block`
  - Title: `Mix Sine Wave Hier Block`
  - Generate Options: `Hier Block`

_Note_: We set the sample rate to 0 because GNU Radio requires us to pick a default value for all parameters. The sample rate won't actually be zero; we'll set it when we use our custom block.

Now, save that file, and press the "Generate" button (right next to run).

Generate won't show any messages or evidence of success. To see it work, move on to the next section.

### Using your custom-built hier block

Congratulations, you've built your first block! Now we're going to use it.

Make a new file called `square_cycle.grc`.

Use Ctrl+F to search for "Mix Sine". You will NOT see the block you created. You need to press the "Reload Blocks" button on the toolbar. (It looks like a "Refresh" button). Then, search again.

Create this flowgraph:

```
GUI Range


Signal Source  -->  Mix Sine Wave Hier Block  -->  Time Sink 
```

- GUI Range:
  - Id: `frequency`
  - Default Value: `20`
  - Start: `2`
  - Stop: `20`
  - Step: `1`
- Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `100`
- Mix Sine Wave Hier Block:
  - Sample Rate: `samp_rate`
  - Frequency: `frequency`


Run that. It should display a wave that pulses on and off, just like the file `square_multiplied_complex.grc` that we created above. The advantage is that we have now hidden the details of the on-off pulsing so that we can focus on the big picture.

Optional Exercises:

- Make the frequency of the Square Signal Source slidable.
- Experiment with the Offset of the Signal Source.

### The background info

_Optional to read_

You'll notice that we set the Generate Options to `Hier Block`. GNU Radio Companion generates the hier blocks in `~/.grc_gnuradio`. You can see them if you run this in a terminal:

```
cd ~
cd .grc_gnuradio
ls
```