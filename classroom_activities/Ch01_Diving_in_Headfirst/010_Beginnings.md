<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 May 22: 010_Beginnings.md
2023 Feb 22: 025-Beginnings.md
</pre>
</details>

ℹ️ This material coincides with material from SDR slideshow B (slides 49-53).

# Beginnings

Before starting:
- Create a folder for yourself with your name (and no spaces) on the Desktop (not necessary if you already created one in the python course).
  - We recommend that you create a directory for each exercise number to keep things organized. This is especially helpful when you reach the exercises that use Embedded Python Blocks, as they generate helper files.
- Follow these directions to run the student setup script (unecessary if you are on the same computer):
  - Right-click on this [student_config_script.sh](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/student_config_script.sh)  and select `Save Link As`.  
  - For the save location, click on `Desktop` on the left, and then click `Save`.
  - Minimize the browser window so that you can see the Desktop.
  - Right-click on your Desktop and select `Open in Terminal`.
  - Type `bash student_config_script.sh` and hit Enter.
  - Let the instructor know if you see any error messages.

Go to [this tutorial page at GNUradio.org](https://wiki.gnuradio.org/index.php?title=Tutorials) (https://wiki.gnuradio.org/index.php?title=Tutorials).

Work through the "3. Your First Flowgraph" tutorial (in upper-left) together as a class. 

There are a few common pitfalls that the instructor will demonstrate:

- When using the "save" dialog in the Ubuntu GNOME desktop environment, it's easy to accidentally search instead of typing the file name.
  - Solution: Click in the file name field before typing a file name.
- When you are searching for blocks, there are odd behaviors if you have a block selected.
  - Solution: Be extra careful to deselect blocks before searching.
  - Solution (alternate): always press Ctrl+F before typing.
- When editing the "Properties" of a block (Access these by double-clicking or right-clicking the block):
  - When you scroll, you may accidentally scroll above the arrow of a drop-down menu, which changes the contents.
    - Solution: Scroll with your cursor on the left side of the window.
  - The `Apply` button is buggy: it will sometimes NOT apply the changes, such as if you use it twice in a row.
    - Solution: Don't use the "Apply" button. Press "Ok" instead.

------

Once you have finished "Your First Flowgraph", follow these tutorials from the same page (mid-left side):

- Python Variables in GRC
- Variables in Flowgraphs
- Runtime Updating Variables
- Signal Data Types
- Converting Data Types

-------

Some useful keyboard shortcuts in GNU Radio Companion:
  - Ctrl + F : Find blocks
  - D : Disable a block
  - E : Enable a block

--------
### Useful information

[HackRF One FAQ](https://hackrf.readthedocs.io/en/latest/faq.html)  
[HackRF One Block Diagram](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/hackrfone_diagram.png)  
[Resources](https://github.com/python-can-define-radio/sdr-course/tree/main/resources)  
[GNU Radio tutorials](https://wiki.gnuradio.org/index.php?title=Tutorials)

