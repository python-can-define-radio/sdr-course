<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 030_Generate_a_signal.md
</pre>
</details>

# Generate a signal using URH 

- Click on the Generator tab at the top of the urh window.

- On the right side under "Generated Data" in the white space right-click and select `add empty message`.

- Type in 32 and hit `ok`.

- At the bottom right of the window select `ASCII` from the `viewtype` dropdown menu.

- This is what your generated data window should now look like.

![generated_data.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/generated_data.png?raw=true) 


- Notice that the 32 bit message we selected is now showing up as 4 bytes in the generated data window.

- Now add the « character which will serve as a preamble of 10101011 in the first slot so we will know when our useful data begins.
    - The Ubuntu keyboard shortcut for this symbol would be Ctl + Shift + u then release and type 00ab then press enter.
    - The Windows keyboard shortcut if your interested would be Alt + 0171 then release.
 
- The next step would be to add a simple 3 letter word in the remaining slots.

- It should now look like this

![catscreenshot.png](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/catscreenshot.png?raw=true) 

### ℹ️ Some useful resources for urh:

- https://github.com/jopohl/urh
