<!-- pandoc-only % SDR: Modulation -->

<!--
Note regarding what goes in the quad chart:

Action: Discuss Modulation in the context of Software Defined Radios.
Standard: Students will be able to explain modulation.


Evaluation: Check on Learning
-->

<!-- pandoc-only ### Purpose -->

<!-- pandoc-only The purpose of this lesson is to practice modulating and demodulating signals using a Software Defined Radio (SDR). -->

<!-- pandoc-only ### Outcome -->

<!-- pandoc-only Students will be able to explain modulation. -->

<!-- pandoc-only ### Learning Step Activities -->

<!-- pandoc-only - LSA 1: Install Universal Radio Hacker (URH) -->
<!-- pandoc-only - LSA 2: Demonstrate Modulation using URH -->
<!-- pandoc-only - LSA 3: Generate a signal using URH -->
<!-- pandoc-only - LSA 4: Interpret a signal using URH -->
<!-- pandoc-only - LSA 5: Interpret a noisy signal using URH -->
<!-- pandoc-only - LSA 6: Cropping a noisy signal using URH -->
<!-- pandoc-only - LSA 7: Interpret multiple noisy signals using URH -->
<!-- pandoc-only - LSA 8: Record a signal using URH -->

# <!-- pandoc-only LSA 1: --> Install Universal Radio Hacker (URH) 📻

### Initial setup   

- Click on the 9 dots in the taskbar of your linux machine and type `terminal` in the search window.

- In terminal type `pip install cython`. 
  
- In terminal type `pip install "urh==2.9.4"`.
<!-- ensure pyqt5 version 5.14.1 is installed. The newest version is failing on the build wheel -->

- In terminal type `pip install --upgrade numpy`.

- In terminal type `urh` to launch the program.

- If you get an error when launching urh:
    - Type `source ~/.profile` and hit Enter.
    - Relaunch by typing `urh` again.

### Launch screen

<div class="columns">
<div class="column">

- At the top left of urh 
    - Select `File > Open folder` or use the shortcut `Ctrl + Shift + O`.
    - Navigate to the Desktop.
    - Select/Create a folder to store your files.
    - Select Open at the top right of the Open folder popup.
    - When it asks if you want to make it a project folder select No.

</div>
<div class="column">

![urh launched](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/Images/urh_screenshot.png?raw=true)  

</div>
</div>

### Some useful resources for urh <!-- pandoc-exclude-line --> 

- https://github.com/jopohl/urh  <!-- pandoc-exclude-line --> 

## <p align="center">[Next Lesson &rarr;](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch03_Analyzing_Signals_URH/020_Modulation.md)</p> <!-- pandoc-exclude-line --> 
