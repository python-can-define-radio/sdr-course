```python3
# The list of bits here comes from URH.
# URH will provide it all concatenated (10101001...), so
# this is a great opportunity to show how to use either find-and-replace
# or ctrl D to add comma-and-space after each digit.
# The bit_length will also come from URH.
modulated_forward = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))



## Some part they figure out on their own by copy/pasting the up pattern

def transmit_forward():
    gnuradio_send(modulated_forward, center_freq=2.413e9, samp_rate=2e6)
    
def transmit_back():
    pcdr.gnusend("10111")
    
def transmit_forward_left():
    pcdr.gnusend("10111")

def transmit__forward_right():
    pcdr.gnusend("10111")

def transmit_back_left():
    pcdr.gnusend("10111")

def transmit__back_right():
    pcdr.gnusend("10111")

app = App()
upButton = PushButton(app, "Up", command=transmit_up)
```
