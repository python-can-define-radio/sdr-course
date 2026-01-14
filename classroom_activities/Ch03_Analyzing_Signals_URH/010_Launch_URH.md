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

<!-- pandoc-only - LSA 1: Launch Software -->
<!-- pandoc-only - LSA 2: Demonstrate Modulation -->
<!-- pandoc-only - LSA 3: Generate a signal -->
<!-- pandoc-only - LSA 4: Interpret a signal -->
<!-- pandoc-only - LSA 5: Interpret a noisy signal -->
<!-- pandoc-only - LSA 6: Cropping a noisy signal -->
<!-- pandoc-only - LSA 7: Interpret multiple noisy signals -->
<!-- pandoc-only - LSA 8: Record/Replay a signal -->
<!-- pandoc-only - LSA 9: RC Car -->

# <!-- pandoc-only LSA 1: --> Launch Software 📻

### Initial setup   

- You need Universal Radio Hacker installed.
- On DragonOS:
  - Select the bluebird in the bottom left of your screen.
  - Type `urh`; select the software and hit enter or click it.
- If you need to pip-install URH, the following appears to work:
    ```
    pip install 'numpy==1.24.4'
    pip install 'cython==3.2.4'
    pip install 'pyqt5==5.14.2'
    pip install 'urh==2.9.8'
    ```

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
