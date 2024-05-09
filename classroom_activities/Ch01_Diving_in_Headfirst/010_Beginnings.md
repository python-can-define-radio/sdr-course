<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Feb 22: 025-Beginnings.md
2023 May 22: 010_Beginnings.md
</pre>
</details>

# Beginnings

ℹ️ This material coincides with material from SDR slideshow B (slides 49-53).

- [Daily Schedule of Events](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/toc/7day.md)

### Before starting: 

- If you have changed classrooms it may be necessary to repeat some steps of the python [preliminaries](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_0a_preliminaries.md) lesson.

- Create a folder for your SDR files with your name (and no spaces) on the Desktop.
  
- We recommend that you create a directory for each exercise number to keep things organized. This is especially helpful when you reach the exercises that use Embedded Python Blocks, as they generate helper files.

### Tutorial:

- Go to [this tutorial page at GNUradio.org](https://wiki.gnuradio.org/index.php?title=Tutorials) (https://wiki.gnuradio.org/index.php?title=Tutorials).

  - Work through the "3. Your First Flowgraph" tutorial (in upper-left) together as a class. 

- Once you have finished "Your First Flowgraph", follow these tutorials from the same page (mid-left side):

  - Python Variables in GRC
  - Variables in Flowgraphs
  - Runtime Updating Variables
  - Signal Data Types
  - Converting Data Types
 
- Some useful keyboard shortcuts in GNU Radio Companion (GRC):

  - Ctrl + F : Find blocks
  - D : Disable a block
  - E : Enable a block

### Common pitfalls of GNU Radio Companion (GRC):

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

### Useful information

[HackRF One FAQ](https://hackrf.readthedocs.io/en/latest/faq.html)  
[HackRF One Block Diagram](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Chx_Misc/Images/hackrfone_diagram.png)  
[Resources](https://github.com/python-can-define-radio/sdr-course/tree/main/resources)  
[GNU Radio tutorials](https://wiki.gnuradio.org/index.php?title=Tutorials)
[GNU Radio error messages](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/Common-GNURadio-error-messages.md)

Videos from Veritasium explaining analog and digital:

- https://www.youtube.com/watch?v=IgF3OX8nT0w
- https://www.youtube.com/watch?v=GVsUOuSjvcg
