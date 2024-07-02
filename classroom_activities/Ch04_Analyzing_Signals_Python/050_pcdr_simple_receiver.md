## Version 1

```python3
## 1
## Run this twice -- once with tuned_freq set to a strong radio station
## in your area, and once with it set to a weak station.
## How do the two results differ?
from pcdr.unstable.flow import OsmoSingleFreqReceiver
receiver = OsmoSingleFreqReceiver("hackrf=0", 103.9e6)
receiver.start()
strength = receiver.get_strength()
print(strength)
receiver.stop_and_wait()
```

## Version zero below

```python3
## 1
## Run this twice -- once with tuned_freq set to a strong radio station
## in your area, and once with it set to a weak station.
## How do the two results differ?
import pcdr.simple
tuned_freq = 103.7e6
receiver = pcdr.simple.OsmosdrReceiver("hackrf", freq=tuned_freq)
strength = receiver.get_strength()
print(f"Strength of {tuned_freq} Hz: {strength}")
receiver.stop_and_wait()


## 2
## Change the previous example to ask the user 
## for a frequency in MHz. Then,
## - Automatically convert the specified frequency to Hz
## - Create an OsmosdrReceiver using the given frequency
## - Display the tuned frequency strength


## 3
## Try this.
import pcdr.simple
import time
tuned_freq_first = 102.1e6
tuned_freq_second = 102.3e6
receiver = pcdr.simple.OsmosdrReceiver("hackrf", freq=tuned_freq)
strength = receiver.get_strength()
print(f"Strength at {tuned_freq_first} Hz: {strength}")
print("Will check another frequency.")
# Note that set_freq has a time.sleep built inside it.
receiver.set_freq(tuned_freq_second)
strength = receiver.get_strength()
print(f"Strength at {tuned_freq_second} Hz: {strength}")


## 4
## Copy and modify the previous example so that it
## asks the user to specify tuned_freq_first and tuned_freq_second.


## 5
## Try this.
import pcdr.simple
import time
tuned_freq = 102.1e6
receiver = pcdr.simple.OsmosdrReceiver("hackrf", freq=tuned_freq)
for count in range(5):
    strength = receiver.get_strength()
    print(f"Strength at {tuned_freq} Hz: {strength}")
    time.sleep(0.5)


## 6
## Copy and modify the previous exercise so that
## the user can pick how many measurements are displayed.


## 7
## Try this.
import pcdr.simple
import time
tuned_freq = 102.1e6
receiver = pcdr.simple.OsmosdrReceiver("hackrf", freq=tuned_freq)
while 2 + 2 == 4:
    strength = receiver.get_strength()
    print(f"Strength at {tuned_freq} Hz: {strength}")
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
for tuned_freq in range(104_000_000, 104_700_000, 100_000):
    print(tuned_freq)


## 11
## Copy and modify the previous example so that the step size is
## one thousand instead of one hundred thousand.


## 12
## Copy and modify the previous example so that it does the following:
## - Create an OsmosdrReceiver (once, before any looping)
## - Use a for loop to produce output as shown in the example below.
## - From earlier recall this command: receiver.set_freq(##)
##
## Example run:
## Strength of 104000000 Hz: 2.131712706467802
## Strength of 104001000 Hz: 2.439891476468502
## Strength of 104002000 Hz: 2.011395112798358
## ... (many lines omitted)
## Strength of 104600000 Hz: 2.011395112798358


## 13
## Copy and modify the previous example. Instead of displaying the 
## strength as a number, display it using this code:
## dots = int(strength) * "o"
## print(f"Strength of {tuned_freq} Hz: {dots}")


## 14  Tabular display -- Measure strength of a single frequency multiple times
## Try this.
import pcdr.simple
import time
from rich.console import Console
from rich.table import Table

tuned_freq = 93.9e6
receiver = pcdr.simple.OsmosdrReceiver("hackrf", freq=tuned_freq)
console = Console()

while True:
    table = Table(title="Frequencies")
    table.add_column("Frequency", justify="center", style="magenta")
    table.add_column("Strength", justify="center", style="green")
    table.add_row(str(tuned_freq), str(receiver.get_strength()))
    console.clear()
    console.print(table) 
    time.sleep(3)


## 15 Tabular display -- Measure strength of multiple frequencies multiple times
## Copy and modify the previous example.
## Expand the table to include at least four different frequency rows and
## add a time column using the datetime module. You will need to add the following import.
## For an extra challenge, do this using a for loop.
## Be sure to tune/set your "receiver" to the targetted frequency when appropriate.

from datetime import datetime
## To get current time:
datetime.now()
## Save that to a variable or put it directly in an output statement.  Convert to string.


## 16
## Loop through the Commercial FM broadcast frequencies.
## Check the strength of each.
## If any of the strength levels surpass a specified threshold, display that frequency.


## 17
## - Loop through the Commercial FM broadcast frequencies. 
## - Make a list of strength levels that surpass a threshold.
## - Randomly jam each using what you learned in the PCDR OOK Transmission lesson:
##     https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch04_Analyzing_Signals_Python/010_pcdr_ook_tx_intro.md
```

