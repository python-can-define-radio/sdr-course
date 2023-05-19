This is synthesizes a signal that can be used to control a particular RC car. It functions, but is not production-quality code.

```python3
## Somewhat manually written. GNU Radio version: 3.8.1.0

from gnuradio import blocks
from gnuradio import gr
import sys
import signal
import osmosdr


def stuffYouHaveToDo():
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)


def setDirection(direction, old_vec_source):
    tb.lock()
    tb.disconnect(old_vec_source)
    vec_source = blocks.vector_source_c(direction, repeat=True)
    tb.connect(vec_source, repeat_block)
    tb.unlock()
    return vec_source


samp_rate = 2e6
tb = gr.top_block()

REPEAT = 1030

HEADER = [1, 1, 1, 0] * 4
FWD = HEADER + ([1, 0] * 34)
REV = HEADER + ([1, 0] * 52)


vec_source = blocks.vector_source_c(REV, repeat=True)

repeat_block = blocks.repeat(gr.sizeof_gr_complex, REPEAT)

osmo_sink = osmosdr.sink()
osmo_sink.set_sample_rate(samp_rate)
osmo_sink.set_center_freq(50e6)
osmo_sink.set_gain(0)
osmo_sink.set_if_gain(30)

tb.connect(vec_source, repeat_block, osmo_sink)


stuffYouHaveToDo()

tb.start()


while True:
    direct = input("f or r?")
    print("Swapping.")

    if direct == "f": 
        vec_source = setDirection(FWD, vec_source)
    elif direct == "r":
        vec_source = setDirection(REV, vec_source)


```


What you could do: incorporate this:

```python3
import tkinter

wn = tkinter.Tk()


def key_press_func(e):
    # print('Key pressed:', e.char, '\nMore details:', e)
    if e.keysym == "Up":
        print("You Pressed up!!")



wn.bind('<KeyPress>', key_press_func)
wn.mainloop()
```
