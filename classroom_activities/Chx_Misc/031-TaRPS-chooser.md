So far, we've seen GUI Ranges (a.k.a. sliders). This exercise demonstrates how to use a chooser (a.k.a. drop-down menu) to control a parameter. You'll see the chooser again in the FM Receiver flowgraph (exercise 210).

Copy and paste your Transmitting flowgraph from `030-Transmit-and-Receive-Pure-Sine.md`.

Make the following changes:

- Delete the `amplitu` GUI Range.
- Create a QT GUI Chooser. Set the parameters:
  - Id: `amplitu`
  - Type: _Hint: what type allows for non-whole numbers?_
  - Option 0: `0`
  - Label 0: `Off`
  - Option 1: `0.5`
  - Label 1: `Mid`
  - Option 2: `1`
  - Label 2: `High`
