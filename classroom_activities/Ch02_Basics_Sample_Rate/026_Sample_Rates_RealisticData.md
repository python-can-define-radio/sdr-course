<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Oct 11: 056-Sample-Rates-7.md
2022 Oct 27: 056-Sample-Rates-7-RealisticData.md
2023 May 22: 026_Sample_Rates_RealisticData.md
</pre>
</details>

## Sending more interesting (and realistic) data

We've seen how to create a square wave using the Vector Source. Now, let's simulate a more interesting signal.

Create this flowgraph. Name it `repeat_demo_3.grc`.

```
Vector Source  -->  Repeat  -->  Time Sink
```

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `10`
- Vector Source:
  - Output Type: `float`
  - Vector: `[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]`
  - Repeat: `Yes`
- Repeat:
  - Type: `float`
  - Interpolation: `5`
- Time Sink:
  - General tab:
    - Type: `float`
    - Number of Points: `100`
    - Y min: `-2`
    - Y max: `2`
  - Config tab:
    - Line 1 Style: `0`
    - Line 1 Marker: `Circle`
