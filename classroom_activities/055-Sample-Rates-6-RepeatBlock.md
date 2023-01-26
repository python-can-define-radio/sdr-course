# Sample rates: the Repeat Block

In `054`, we created a square wave using a Vector Source block.

Let's imagine we want to make a square wave with a frequency of 2 Hz, and a sample rate of 1 Msps (Million samples per second).

One second of data would look the same as before...

```
               ___________           ___________

    ___________           ___________           
```

... but it would be represented using MANY more samples.

As we discussed in `054`, the period of a 2 Hz signal is half a second, and consequently, it spends a quarter second "high", and a quarter second "low".

<details><summary>Question: With a sample rate of 1 Msps, how many samples are in half a second? How many are in a quarter second? (Click for answer)</summary>

Answer: Half a second is 500,000 samples, and a quarter second is 250,000 samples.
</details>

We could type 250,000 zeros and 250,000 ones in the vector source, but that's definitely not the ideal solution!

The solution? The Repeat block.

To start our experimentation with the Repeat block, let's use a smaller sample rate: 10 samples per second.

Create this flowgraph. Name it `repeat_demo_1.grc`.

```
Vector Source  -->  Repeat  -->  Time Sink
```

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `10`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1]`
  - Repeat: `Yes`
- Repeat:
  - Type: `float`
  - Interpolation: `5`
- Time Sink:
  - General tab:
    - Type: `float`
    - Number of Points: `40`
    - Y min: `-2`
    - Y max: `2`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`

Questions:

1. What is the ratio of the Number of Points to the Sample Rate?
2. How many seconds are shown in the Time Sink? How does that compare to the ratio asked in the previous question?
3. What does the Repeat block appear to do?
4. What is the frequency of the square wave currently?
5. Try different values for Interpolation. How does that affect the frequency of the square wave? What number should you pick if you want the square wave to have a frequency of 0.5 Hz (in other words, one full cycle every two seconds)?

Now, set the sample rate to 20. (This should only require changing the `samp_rate` variable; all others should change automatically.)

6. How many seconds are shown in the Time Sink?
7. What Repeat Interpolation should you pick to make a square wave with a frequency of...
   1. 1 Hz?
   2. 0.5 Hz?
   3. 2 Hz?
8. What Number of Points should you pick to view 1 second of data?
9. How much time would you be able to see if you set the Number of Points to `60`?

Now, let's significantly raise the sample rate. There are two changes that help lower the chance of freezing the flowgraph:
- Add a throttle
- Increase the time between updates (the Update Period) on the Time Sink

Copy and paste your previous flowgraph. Name it `repeat_demo_2.grc`. Add a throttle as shown.

```
Vector Source  -->  Repeat  -->  Throttle  -->  Time Sink
```

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `1e6`
- Vector Source:
  - Output Type: _same as above_
  - Vector: _same as above_
  - Repeat: _same as above_
- Repeat:
  - Type: _same as above_
  - Interpolation: `10`
- Time Sink:
  - General tab:
    - Type: _same as above_
    - Number of Points: `40`
    - Y min: _same as above_
    - Y max: _same as above_
    - Update Period: `15`
  - Config tab:
    - Line 1 Style: _same as above_
    - Line 1 Marker: _same as above_

10. In this new flowgraph, how much time is shown in the Time sink?
11. What is the period of the square wave? 
12. If we want the period to be 100 microseconds, what should the Interpolation be? 
13. Set the Interpolation to 200. What is the period? What Number of Points should you pick so you can se the entire cycle of the square wave?
14. If we want the frequency to be 2 Hz, what should the period be? What should the Interpolation be? What should the Number of Points be?  

With a significantly larger Number of Points, the window may become unresponsive. You may need to lower the Number of Points to avoid freezing. Unfortunately, as a result, you may not be able to see the entirety of the square wave.

15. Why would we want to set the sample rate so high? (Hint: what is the minimum sample rate of the Hack RF?)
