## Need for speed

In `050`, we measured every 2 hours. That works for weather, but now, imagine you're dealing with a thermometer on a processor. Actually, you don't need to use your imagination — on Linux, simply run this in the terminal:

```
watch -n 0.2 -- cat /sys/class/thermal/thermal_zone*/temp
```

This means to check the temperature reading every 0.2 seconds, which is a sample rate of 5 Hz (5 times per second).

The units are thousandths of a degree Celsius, so `27800` means 27.8 °C.

Is 5 times per second a good measurement frequency? Let's make the temperature go up by running a useless (but processor-intensive) Python program:

```python3
for x in range(1000000000000):
    y = x
```

Incredibly, the temperature jumps up by about 13 °C within a fifth of a second. (At least, it did on my computer.) So, if you were setting up an automatic throttle (limit) for the processor, it would probably need to sample even more frequently than 5 samples per second (5 Hz).

## Recording the data

We can take measurements using Python. Name this file `temp_measure.py`:

```python3
import time

outputFileName = "myTempReadings.txt"

# If this doesn't work, try changing it to thermal_zone0, thermal_zone1, thermal_zone3, etc
inputFileName = "/sys/class/thermal/thermal_zone2/temp"

f_out = open(outputFileName, "w")

for i in range(1, 12+1):    # Take a specified number of temperature readings
    f_temp = open(inputFileName, "r")
    contents = f_temp.read().strip()
    T = int(contents)/1000   # Convert T from millidegrees to deg. Celcius.
    print(T)
    f_out.write(str(T) + ", ")
    time.sleep(0.2)

f_out.close()
f_temp.close()

```

<details><summary><i>Note: This will take a measurement <b>approximately</b> five times per second. Click for more info.</i></summary>
   
> For our purposes in this class, "approx 5 times per second" is completely fine.
> 
> However, if you ever need a more precise sample rate for something outside of this class, you would want to use a different approach. See [here](https://stackoverflow.com/a/67930185) and [here](https://mail.python.org/pipermail/python-list/2000-November/060154.html). Fair warning that both links go fairly deeply into the topic.

</details>

When you run that Python file, it will write to a file called `myTempReadings.txt`.

## Visualizing the data

Reopen your file `temperature_graph_1.py` from `050`. Replace the `temps` variable with the measured processor temperatures that are in `myTempReadings.txt`. Run that to graph the data.

Also, reopen your file `temperature_graph_2.grc` from `050`. Make the following changes:

Parameters:  
- Variable (_already in the flowgraph_):
  - Id: `samp_rate`
  - Value: `5`
- Vector Source:
  - Vector: _Your data goes here. You'll need to append some zeros at the end just as we did before._
- Time Sink:
  - General Tab:
    - Number of Points: _Approximately 15. Should be the same as the number of data points that you recorded._
    - Y max: 100000

Run that to visualize your data. Make sure it matches the Python-generated graph.

Notice the x-axis on the GNU Radio-generated graph. How much time is there between data points? Is it what you expected?

