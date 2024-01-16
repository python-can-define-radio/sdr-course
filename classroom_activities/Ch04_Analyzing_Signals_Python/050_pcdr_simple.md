

```python3
## 1
## Run this twice -- once with center_freq set to a strong radio station
## in your area, and once with it set to a weak station.
## How does the result vary?
import pcdr.simple
center_freq = 103.7e6
receiver = pcdr.simple.OsmosdrReceiver(center_freq)
strength = receiver.get_cf_strength()
print(f"Strength of {center_freq} Hz: {strength}")


## 2
## Change the previous example to ask the user 
## for a frequency in MHz. Then,
## - Automatically convert the specified frequency to Hz
## - Create an OsmosdrReceiver using the given frequency
## - Display the center frequency strength


## 3
## Try this.
import pcdr.simple
import time
center_freq_first = 102.1e6
center_freq_second = 102.3e6
receiver = pcdr.simple.OsmosdrReceiver(center_freq_first)
strength = receiver.get_cf_strength()
print(f"Strength at {center_freq_first} Hz: {strength}")
print("Will check another frequency in 1 second.")
time.sleep(1)
receiver.set_center_freq(center_freq_second)
strength = receiver.get_cf_strength()
print(f"Strength at {center_freq_second} Hz: {strength}")


## 4
## Copy and modify the previous example so that it
## asks the user to specify center_freq_first and center_freq_second.


## 5
## Try this.
import pcdr.simple
import time
center_freq = 102.1e6
receiver = pcdr.simple.OsmosdrReceiver(center_freq)
for count in range(5):
    strength = receiver.get_cf_strength()
    print(f"Strength at {center_freq} Hz: {strength}")
    time.sleep(0.5)


## 6
## Copy and modify the previous exercise so that
## the user can pick how many measurements are displayed.


## 7
## Try this.
import pcdr.simple
import time
center_freq = 102.1e6
receiver = pcdr.simple.OsmosdrReceiver(center_freq)
while 2 + 2 == 4:
    strength = receiver.get_cf_strength()
    print(f"Strength at {center_freq} Hz: {strength}")
    time.sleep(0.5)


## 8
## Copy and modify the previous example.
## If the strength passes a given threshold, print "SOMETHING HAPPENED!"
## (In other words, make an activity detector.)
## For extra fun, make it play a sound using the playsound module.


## 9
## Copy and modify the previous example.
## Referring back to the Python exercises about while loops if needed,
## make the loop exit if activity is detected.


## 10
## Try this.
import pcdr.simple
import time
from rich.console import Console
from rich.table import Table

center_freq0 = 93.9e6
receiver = pcdr.simple.OsmosdrReceiver(center_freq0)
console = Console()

while True:
    table = Table(title="Frequencies")
    table.add_column("Frequency", justify="center", style="magenta")
    table.add_column("Strength", justify="center", style="green")
    table.add_row(str(center_freq0), str(receiver.get_cf_strength()))
    console.clear()
    console.print(table) 
    time.sleep(3)


## 11
## Copy and modify the previous example.
## Expand the table to include at least four different frequency rows and
## add a time column using the datetime module. You will need to add the following import.

from datetime import datetime
```
