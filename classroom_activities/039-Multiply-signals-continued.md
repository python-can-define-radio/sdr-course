_Prerequisite: `038-Multiplying-signals.md`_

We want to be able to transmit the generated on-off signal to the Hack RF.

To do so, we need a higher sample rate than in `038-Multiplying-signals`, because the Hack RF requires at least 2 million samples per second.

We also adjust the number of points displayed in the Time Sink so that we can still see what is happening.
<details><summary>Details if you're curious:</summary>
<p>
  
------
  
Before, we used the default value of `1024` points. That worked when the sample rate was 100 Hz, because `1000` points would be 10 seconds, so `1024` points is a little more than 10 seconds. Now that the sample rate is 2000000, we want to see a larger chunk of time, because 1024 is only about a thousandth of 2000000.
  
------
  
</p>
</details>



Lastly, we add a throttle. This keeps the program from maxing out the CPU.

Note: The sine wave's frequency is arbitrary. Feel free to adjust it.

----------------------------------

Make a new file: `square_multiplied_2.grc`
```
Signal Source  -->  Multiply  -->  Throttle  -->  Time Sink
Signal Source  -->  
```

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `float`
  - Waveform: `Sine`
  - Frequency: `20`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Number of Points: `int(samp_rate)*4`

Note: When you run this file, it will take about 4 seconds before displaying any data.

----------------------------------

We can't transmit to the osmocom sink unless the data type is blue (complex).

So, copy the previous flowgraph into a new file called `square_multiplied_complex.grc`

```
Signal Source --> Float to Complex -->  Multiply  -->  Throttle  -->  Time Sink
                    Signal Source  -->
```

_Note:_ The Square Signal source should be attached to the `re` port on the Float to Complex block.

- First Signal Source:
  - Output Type: `float`
  - Waveform: `Square`
  - Frequency: `1`
- Second Signal Source:
  - Output Type: `complex`  (**different**)
  - Waveform: `Sine`
  - Frequency: `20`
- Variable samp_rate (Not shown above):
  - Id: `samp_rate`
  - Value: `2e6`
- Time Sink:
  - Number of Points: `int(samp_rate)*4`


----------------------------------

Now that we have the cycling on and off working, we want to hide some of those details. In most of programming, this is done by defining a function. Here, it's done using a Hier Block.

_If you'd like a visual description of Hier Blocks, see [here](https://wiki.gnuradio.org/index.php/Hier_Blocks_and_Parameters)._

We need a folder in our home directory called `.grc_gnuradio`. Open a terminal, and type this:

```
cd ~
mkdir .grc_gnuradio
```

Now that we've created that directory, go back to GNU Radio.

Click File, New, Hier Block.

Open the "Save As" window. You may not be able to see the .grc_gnuradio directory that you created. If you can't, then press Ctrl+H to show hidden files.

Name the file `hier_on_off_cycle.grc`, saved in the .grc_gnuradio directory.

Flowgraph:
```
Signal Source --> Float to Complex -->  Multiply  -->  Pad Sink
                       Pad Source  -->
```


