<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Feb 22: 025-Beginnings.md
2023 May 22: 010_Beginnings.md
</pre>
</details>

ℹ️ This material coincides with material from SDR slideshow B (slides 49-53).

# Beginnings

- [Daily Schedule of Events](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/toc/7day.md)

Before starting: 

- If you did not change classrooms from Python skip the next three steps.

- Open VSCode, then close it.

- <details><summary>Link your computer to the student samba. (Expand for details)</summary>
  
  1) Open the file browser.  
  
  2) Click on `+ Other Locations` in the bottom left corner.
  
  3) At the bottom where it says `Enter server address`, type smb://`the url` (provided by the instructor) and hit Enter.
  
  4) Double-click on `studentsamba`.
  
  5) Select the `Registered User` radio button.
  
  6) Enter username and password (provided by the instructor).
  
  7) Select the `Forget password immediately` radio button.
  
  8) Click Connect.
  
  9) Close file browser. you are now linked to the studentsamba.

  10) Repeat as necessary if the `studentsamba` loses connection. 
</details>

- <details><summary>Follow these directions to run the student setup script. (Expand for details)</summary>
  
  1) Right-click on this [student_config_script.sh](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/student_config_script.sh)  and select `Save Link As`.
  
  2) For the save location, click on `Desktop` on the left, and then click `Save`.
  
  3) Minimize the browser window so that you can see the Desktop.
  
  4) Right-click on your Desktop and select `Open in Terminal`.
     
  5) Type `bash student_config_script.sh` and hit Enter.
     
  6) Let the instructor know if you see any error messages.
     
  7) <details><summary>Expand here for Manual instructions if the script does not work.</summary>

      ### How to change terminal timeout (TMOUT variable):
      
      - Activate a Terminal program window in Linux OS.
      - Type and run: `echo -e '\n\nexport TMOUT=30000' >> ~/.bashrc` (this appends `export TMOUT=30000` to the end of the .bashrc file)
      - Verify that it changed the file using this command to view the file: `cat ~/.bashrc`
      - Close all terminals so it'll take effect.
      
      ### Alternate approach to change TMOUT:
      
      Run this Python:
      
      ```python3
      f = open("/home/PUT_YOUR_USERNAME_HERE/.bashrc", "a")
      f.write("\n\n")
      f.write("export TMOUT=300000")
      f.close()
      ```
      
      ### How to change OS screen timeout on Ubuntu:
      
      In Settings, click the magnifying glass in the top left of the window and search `Screen Lock` and select it.
      - Adjust the "Blank Screen" option. Recommended setting: 15 minutes.
      - Adjust the "Automatic Screen Lock Delay". Recommended setting: 30 minutes.
      
      ### For instructions on how to disable middle click go to:
      https://github.com/python-can-define-radio/python-course/blob/main/resources/disable-middle-click-how-to.md
      </details>
</details>  

  - Create a folder for yourself with your name (and no spaces) on the Desktop.
  
  - We recommend that you create a directory for each exercise number to keep things organized. This is especially helpful when you reach the exercises that use Embedded Python Blocks, as they generate helper files.

  - Go to [this tutorial page at GNUradio.org](https://wiki.gnuradio.org/index.php?title=Tutorials) (https://wiki.gnuradio.org/index.php?title=Tutorials).

  - Work through the "3. Your First Flowgraph" tutorial (in upper-left) together as a class. 

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

