## Meeting the Hack RF's Sample Rate Requirements

In the previous two exercises (038 and 039), we used a sample rate of 100 samples per second for demonstration purposes. Now, we must raise it to  [the Hack RF's required minimum](https://hackrf.readthedocs.io/en/latest/hackrf_one.html): 2 million samples per second.

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
