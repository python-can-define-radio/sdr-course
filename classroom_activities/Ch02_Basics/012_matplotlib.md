# Matplotlib module

### Install the necessary modules
`pip install matplotlib`  
`pip install numpy`

### Import the modules

- We will use numpy to create waves, so it will need to be imported as well.

```python3
import matplotlib.pyplot as plt
import numpy as np
```
### Plotting with y as the variable (x is default) or plotting x and y together

```python3
## 1
## Plot this.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
plt.plot(y)
plt.show()
```
- This is the minimum required to plot anything (define the y-axis values, plot them, and show the plot).
- If you don't specify any values for the x-axis, it will default to the index of the y-axis element. In this example, there are 9 y-axis elements, so there will be 9 x-axis values: `0, 1, 2 ... 7, 8`.

```python3
## 2
## Now let's add a background grid and a title.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
plt.plot(y)
plt.grid()
plt.title("First Plot")
plt.show()
```

- Now let's provide x-axis values.

```python3
## 3
## Plot this.
y = [1, 2, 2, 3, 4, 3, 2, 2, 1]
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(x, y)
plt.grid()
plt.title("First Plot")
plt.show()

## 4
## Copy and modify the previous example and remove a single point of either x or y.
## What happened? See answer below.
```
<details><summary>Answer</summary>

- You should have gotten an error similar to this:  
  `ValueError: x and y must have same first dimension, but have shapes (9,) and (8,).`
  
- This means that the length of the lists `x` and `y` must be the same.
</details>

### Specifying markers, colors, linestyle, and legends 

- [Here](https://matplotlib.org/stable/api/markers_api.html) is a list of available matplotlib markers.
- [Here](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html) is a list of available matplotlib linestyles.
- [Here](https://matplotlib.org/stable/gallery/color/named_colors.html) is a list of available matplotlib colors.
- [Look Here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) for information about legends in matplotlib.

```python3
## 5
## Plot this.
## Feel free to experiment.
amplitude = [1, 2, 2, 3, 4, 3, 2, 2, 1]
time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(time, amplitude, marker="*", markersize=10, color="red", linestyle="--", label="test legend")
plt.legend(loc="upper right")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.title("Second Plot")
plt.show()


## 6
## The plot function also accepts a short form which combines the
## marker, color, and linestyle arguments.
## Try replacing your plt.plot command with this one.
plt.plot(time, amplitude, "*r--", markersize=10)
## The order of *, r, and -- do not matter.
```

### Using numpy functions `np.linspace()` and `np.sin()` to generate values

- Now let's trying using numpy functions to generate our values.
- We are going back to a basic plot without any of the `fancy` stuff

```python3
## 7
## Try this, it fails. Can you determine why?
timestamps = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
y = timestamps + 3
plt.plot(timestamps, y, "*g--")
plt.show()
## See below for answer
```
<details><summary>Answer</summary>
  
A normal Python list does not interpret the `+` as addition to each element of `timestamps`. However, a numpy array does, so we'll use those for the rest of this exercise.

</details>

```python3
## 8
## Plot this.
## We'll use a numpy array instead of a list because it allows us to
## use math operations, such as adding a constant.
timestamps = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
y = timestamps + 3
plt.plot(timestamps, y, "*g--")
plt.show()


## 9
## Plot this.
## We can simplify by using np.linspace, which generates an array of LINearly SPACEd numbers.
## This will do the same thing as the np.array above,
## but allows us to generate very long arrays with very little code.
timestamps = np.linspace(0, 1, 10, endpoint=False)
y = timestamps + 3
plt.plot(timestamps, y, "*g--")
plt.show()


## 10
## Plot this.
## We can also use more interesting functions
## like the sine function to create a wave.
timestamps = np.linspace(0, 5, 50, endpoint=False)
y = np.sin(timestamps)
plt.plot(timestamps, y, "*g--")
plt.show()
```

### Multiple signals in a single `plot`, separating signals using `plt.subplot()`, and `plt.tight_layout()`

```python3
## 11
## Plot this.
## It demonstrates multiple signals in a single plot.
## I also separated marker, color, and linestyle in order to use special characters for the marker.
timestamps = np.linspace(0, 6.28, 15, endpoint=False)
y = np.sin(timestamps)
z = np.cos(timestamps)
plt.plot(timestamps, y, marker="$S$", color="blue", linestyle= "-", markersize=10, linewidth=3, label="sine")
plt.plot(timestamps, z, marker="$C$", color="red", linestyle= "-", markersize=10, linewidth=3, label="cosine")
plt.legend(loc="upper right")
plt.show()


## 12
## Plot this.
## It shows the same two waves in seperate subplots.
timestamps = np.linspace(0, 6.28, 15, endpoint=False)
y = np.sin(timestamps)
z = np.cos(timestamps)
plt.subplot(211)
plt.plot(timestamps, y, marker="$S$", color="blue", linestyle= "-", markersize=10, linewidth=3, label="sine")
plt.legend(loc="upper right")
plt.subplot(212)
plt.plot(timestamps, z, marker="$C$", color="red", linestyle= "-", markersize=10, linewidth=3, label="cosine")
plt.legend(loc="upper right")
plt.show()


## 13
## We have added a third subplot.
## Use plt.tight_layout() to prevent overlapping subplots.
timestamps = np.linspace(0, 6.28, 15, endpoint=False)
y = np.sin(timestamps)
z = np.cos(timestamps)
t = timestamps
plt.subplot(311)
plt.plot(timestamps, y, marker="$S$", color="blue", linestyle= "-", markersize=10, linewidth=3, label="sine")
plt.legend(loc="upper right")
plt.subplot(312)
plt.plot(timestamps, z, marker="$C$", color="red", linestyle= "-", markersize=10, linewidth=3, label="cosine")
plt.legend(loc="upper right")
plt.subplot(313)
plt.plot(timestamps, t, marker="$T$", color="green", linestyle= "-", markersize=10, linewidth=3, label="Timestamps")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()


## 14
## Create a plot that has 4 subplots, laid out as a 4-by-1 grid.
## Use the same x-axis values for all four plots.
## Use np.linspace to create those x-axis values.
## For the y-values, use these:
##   np.sin(timestamps)
##   np.sin(2*timestamps)
##   np.sin(3*timestamps)
##   np.sin(4*timestamps)
## If the sine waves appear rough, raise the number of points generated by linspace.


## 15
## Copy and modify the above plot.
## Lay it out as a 1-by-4 grid.


## 16
## Copy and modify the above plot,
## laid out as a 2-by-2 grid.
```
### Adding text onto our plot

```python3

## 17
## Plot this.
amplitude = [1, 2, 2, 3, 4, 3, 2, 2, 1]
time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(time, amplitude, "Pr-", linewidth=.2)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.text(0.2, 2.5, 'box with italic text at data coords: .2(x) and 2.5(y)', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.4, 'pad': 10})
plt.grid()
plt.title("Eleventy seventh Plot")
plt.show()
```

### Links for further exploration

[Link to matplotlib docs](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#)  
[Quick start guide](https://matplotlib.org/stable/tutorials/introductory/quick_start.html)  
[A simple plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)
