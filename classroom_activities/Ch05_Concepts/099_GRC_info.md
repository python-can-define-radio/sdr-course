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

### Some useful keyboard shortcuts in GNU Radio Companion (GRC):

  - Ctrl + F : Find blocks
  - D : Disable a block
  - B : Bypass a block
  - E : Enable a block

### Tutorial:

- Go to [this tutorial page at GNUradio.org](https://wiki.gnuradio.org/index.php?title=Tutorials) (https://wiki.gnuradio.org/index.php?title=Tutorials).

  - Under `Beginner Tutorials > Introducing GNU Radio` we will work through the "Your First Flowgraph" tutorial together as a class. 

- Once you have finished "Your First Flowgraph", complete these tutorials from the `Flowgraph Fundamentals` category:

  - Python Variables in GRC
  - Variables in Flowgraphs
  - Runtime Updating Variables
  - Signal Data Types
  - Converting Data Types

- Once those are completed you should return to `Ch01_Diving_in_Headfirst` and try constructing the FM receiver in `030_GRC_FM_Receiver.md`.

[GNU Radio tutorials](https://wiki.gnuradio.org/index.php?title=Tutorials)  
[GNU Radio error messages](https://github.com/python-can-define-radio/sdr-course/blob/main/resources/Common-GNURadio-error-messages.md)  