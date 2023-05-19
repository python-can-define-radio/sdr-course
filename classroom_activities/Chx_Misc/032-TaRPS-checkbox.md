This exercise demonstrates how to use a checkbox to control a parameter. For example, this checkbox is used in the FM Receiver (exercise 210) to enable/disable a filter.

Copy and paste your Transmitting flowgraph from `030-Transmit-and-Receive-Pure-Sine.md`.

Make the following changes:

- Delete the `amplitu` GUI Range.
- Create a QT GUI Checkbox. Set the parameters:
  - Id: `amplitu`
  - Type: _Hint: what type allows for non-whole numbers?_
  - Default Value: `0`
  - True: `0.9`
  - False `0`
