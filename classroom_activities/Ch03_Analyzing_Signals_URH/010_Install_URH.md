<!-- pandoc-only % SDR: Modulation -->

<!-- pandoc-only ### Purpose -->

<!-- pandoc-only The purpose of this lesson is to practice modulating and demodulating signals using a Software Defined Radio (SDR). -->


# <!-- pandoc-only LSA 1: --> Install Universal Radio Hacker (URH) 📻

### Initial setup   

- Click on the 9 dots in the taskbar of your linux machine and type `terminal` in the search window.

- In terminal type `pip install cython`. 
  
- In terminal type `pip install "urh==2.9.4"`.
<!-- ensure pyqt5 version 5.14.1 is installed. The newest version is failing on the build wheel -->

- In terminal type `pip install --upgrade numpy`.

- In terminal type `urh` to launch the program.

- If you get an error when launching urh type `source ~/.profile` then relaunch by typing `urh` again.

### Launch screen

<div class="columns">
<div class="column">

- At the top left of urh 
    - Select `File > Open folder` or use the keyboard shortcut `Ctrl + Shift + O`.
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
  

