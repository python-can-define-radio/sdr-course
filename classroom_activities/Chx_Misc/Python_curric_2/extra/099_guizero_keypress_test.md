```python3
from guizero import App, TextBox
from pcdr import ook_modulate, gnuradio_send


def highlight(evdata):
    app.bg = "lightblue"
    if evdata.tk_event.keysym == "Up":
        print("Pressed up!")
        gnuradio_send(ookmodded_1, center_freq=499e6, samp_rate=2e6, if_gain=2)

def lowlight(evdata):
    app.bg = "white"
    if evdata.tk_event.keysym == "Up":
        print("Released up!")

ookmodded_1 = ook_modulate([1,0,1,0], bit_length=int(500e3))

app = App()
# When the mouse enters the TextBox
app.when_key_pressed = highlight
# When the mouse leaves the TextBox
app.when_key_released = lowlight

app.display()
```
