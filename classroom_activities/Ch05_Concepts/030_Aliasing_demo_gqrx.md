<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Apr 21: 999-aliasing-demo-gqrx.md
2023 May 22: 030_Aliasing_demo_gqrx.md
</pre>
</details>

## Aliasing

Aliasing in signal processing happens when you measure a signal that is outside of what your sample rate allows.

1. Open GQRX on the instructor screen. Tune to the broadcast FM range.
2. Have a student run the noise jammer, tuned to near the top end of the spectrum.
3. Slowly raise the noise jammer past the right edge. It will incorrectly appear on the left edge due to aliasing.
 
### How to fix?

In the FM Radio flowgraph, we use the "filteron" checkbox to do analog filtering inside the Hack RF.

In GQRX, you should be able to use the same filter, but as far as I can tell, there's a bug that prevents that from working, unfortunately. (Either that, or I'm doing it wrong.)
 
 
 
