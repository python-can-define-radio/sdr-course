import matplotlib.pyplot as plt
import turtle
import numpy as np
from itertools import cycle

## Change this part to positive 
## or negative 1 to see how it varies
freq = -1

colorcyc = cycle(["red", "green", "blue"])
turtle.penup()
t = np.linspace(0, 1, 100)
x = np.cos(2 * np.pi * freq * t)
y = np.sin(2 * np.pi * freq * t)
plt.plot(t, x, "b")
plt.plot(t, y, "r")
plt.show(block=False)
while True:
    turtle.fillcolor(next(colorcyc))
    for idx in range(len(x)):
        xp = x[idx] * 100  # rescale
        yp = y[idx] * 100
        turtle.goto(xp, yp)
        turtle.stamp()
