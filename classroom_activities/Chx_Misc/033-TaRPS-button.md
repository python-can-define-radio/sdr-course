This exercise demonstrates how to use a button to control a parameter. You could, for example, use this for transmitting Morse Code.

Copy and paste your Transmitting flowgraph from `030-Transmit-and-Receive-Pure-Sine.md`.

Make the following changes:

- Delete the `amplitu` GUI Range.
- Create a QT GUI Push Button. Set the parameters:
  - Id: `amplitu`
  - Type: _Hint: what type allows for non-whole numbers?_
  - Default Value: `0`
  - Pressed: `0.9`
  - Released `0`
