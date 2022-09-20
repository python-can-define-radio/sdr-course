_Prerequisite: `038-Multiplying-signals.md`_

We want to be able to transmit the generated on-off signal to the Hack RF.

To do so, we need to make a few changes.

## Meeting the Hack RF's Sample Rate Requirements

In `038-Multiplying-signals`, we used a sample rate of 100 samples per second for demonstration purposes. Now, we must raise it to  [the Hack RF's required minimum](https://hackrf.readthedocs.io/en/latest/hackrf_one.html): 2 million samples per second.

This necessitates a few other changes:

1. We'll raise the number of points displayed in the Time Sink so that we can still see what is happening. <details><summary>Details if you're curious:</summary>
Before, we used the default value of `1024` points. That worked when the sample rate was `100` samples per second, because it allowed us to see about 10 seconds worth of data. (Reason: `1000` data points would be 10 seconds (because it's ten groups of 100 samples), so `1024` data points is a little more than 10 seconds.)  
&nbsp;  <!-- This nbsp allows for a line break within a list item -->
Now that the sample rate is 2000000, a view of 1024 points would only show us less than a thousandth of a second. A full second of data would be 2000000 points; 2 seconds of data would be 4000000 points; 3 seconds would be 6000000, and so forth. We chose to view 4 seconds, which is 8000000 data points. Instead of typing 8000000, we type `int(samp_rate * 4)` because if we ever change the sample rate, the view of the data will update accordingly.
</details>

2. We'll adjust the Update Period so that the Time Sink only updates every 15 seconds. <details><summary>The only reason is...</summary> The only reason is a very practical concern: the default update frequency is every tenth of a second (Update Period = `0.10`). Since we're displaying 8 million data points, this often maxes out the CPU, and causes the computer to stop responding. The choice of 15 seconds is arbitrary; anything larger than 9 seconds would probably work fine on our classroom computers.</details>

3. We'll add a throttle. <details><summary>Details:</summary>This is another safeguard to avoid maxing out the CPU. More info [here](https://wiki.gnuradio.org/index.php/Throttle).</details>

4. We'll adjust the sine wave's frequency. This is just to show what other frequencies look like. Feel free to pick a different number.

### The Flowgraph

Make a new file: `square_multiplied_2.grc`

```
Signal Source --┐ 
                └->   
                     Multiply  -->  Throttle  -->  Time Sink
                ┌->
Signal Source --┘  
```

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `20`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Number of Points: `int(samp_rate * 4)`
  - Update Period: `15`

_Notes:_

- _For each block, change the input and output port colors to orange._
- _After pressing play, there will be about 5 seconds before any data is displayed._

<details><summary>Challenge Question (optional):</summary>
<p>

- How many seconds of data will be displayed in the Time Sink? 
  - _Hint: Every second, 2 million data points flow into the Time Sink._  
    _How many seconds does it take for 8 million data points to arrive?_

</p>
</details>

Run this to ensure that it works.

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

_Note:_ The Square Signal source should be attached to the `re` port on the Float to Complex block.

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `complex`  (**different from before**)
  - Waveform: `Sine`
  - Frequency: `20`
- Multiply:
  - IO Type: `complex`
- Throttle:
  - IO Type: `complex`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Type: `complex`
  - Number of Points: `int(samp_rate * 4)`
  - Update Period: `15`

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

Now that we've created that directory, go back to GNU Radio.

Click File, New, Hier Block.

Open the "Save As" window. In that window, you may not be able to see the .grc_gnuradio directory that you created. If you can't see it, then press Ctrl+H to show hidden files.

Name the file `on_off_cycle_hier_block.grc`, and save it in the .grc_gnuradio directory.

Flowgraph:
```
Parameter

Parameter


Signal  --> Float to  ---┐
Source      Complex      |
                         └->
                              Multiply  -->  Pad Sink 
                         ┌->
                         |
           Pad Source  --┘
```

_Note:_ The Square Signal source should be attached to the `re` port on the Float to Complex block.

- Signal Source:
  - Output Type: `float`
  - Sample Rate: `samp_rate`
  - Waveform: `Square`
  - Frequency: `frequency`
- Variable (_already in the flowgraph_) with id `samp_rate`:
  - Delete this block. It is automatically created, but in this case, we do not want it.
- First Parameter:
  - Id: `samp_rate`
  - Label: `Sample Rate`
  - Type: `Float`
- Second Parameter:
  - Id: `frequency`
  - Label: `Frequency`
  - Type: `Float`
- Options block (Not shown above):
  - Title: `On Off Cycle Hier Block`


Now, save that file, and press the "Generate" button (right next to run).

Generate won't show any messages or evidence of success. To see it work, move on to the next section.

### Using your custom-built hier block

Congratulations, you've built your first block! Now we're going to use it.

Make a new file called `square_multiplied_complex_2.grc`.

Use Ctrl+F to search for "On Off". You should see the block you created. If you don't, then press the "Reload Blocks" button on the toolbar. (It looks like a "Refresh" button). Then, search again.

Create this flowgraph:

```
Signal Source  -->  On Off Cycle Hier Block  -->  Throttle  -->  Time Sink 
```

- Signal Source:
  - Output Type: `complex`
  - Waveform: `Sine`
  - Frequency: `20`
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `2e6`
- On Off Cycle Hier Block:
  - Frequency: `1`
  - Sample Rate: `samp_rate`
- Time Sink:
  - Number of Points: `int(samp_rate * 4)`
  - Update Period: `15`


Run that. It should display a wave that pulses on and off, just like the file `square_multiplied_complex.grc` that we created above. The advantage is that we have now hidden the details of the on-off pulsing so that we can focus on the big picture.

In the next activity, we'll connect this to the Hack RF.

Optional Exercises:

- Make the frequency of the Signal Source slidable. 
- Make the frequency of the On Off Cycle Hier Block slidable.
