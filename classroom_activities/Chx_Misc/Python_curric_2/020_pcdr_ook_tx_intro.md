## Introduction to OOK Transmitting using Python

One of the biggest advantages of defining radios using software is being able to transmit using arbitrary modulation schemes. In this lesson, we practice using Python (which is using GNU Radio behind the scenes) to transmit data using On-Off Keying (OOK).

```python3
from pcdr.gnuradio_sender import gnuradio_send
from pcdr.modulators import ook_modulate


## 1
## Try this. Have a neighbor receive the signal in 
##  a spectrum analyzer program such as GQRX,
##  and then in URH.
## How many seconds long is each bit?
modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## NOTE: If you don't have a SDR peripheral, use this modified version:
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6, output_to="print")



## 2
## Copy and modify the previous example to send a different pattern of bits.


## 3
## Try this.
## How many seconds long is each bit?
modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(2e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 4
## Try this.
## How many seconds long is each bit?
## How many milliseconds is that?
## How many bits per second are you sending?
modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(200e3))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 5
## The ASCII (or Unicode) value for the letter C is 67.
## In binary, that's 1000011, which is 7 bits long.
## Since computers expect bytes to be 8 bits long,
## we need to "pad" with a leading zero so that we
## have a full byte of information: 01000011.
## Let's try to send it, and receive it using URH.
## You may run into an issue, which we'll discuss in the exercise below.
modulated = ook_modulate([0, 1, 0, 0, 0, 0, 1, 1], bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 6
## If you tried sending the letter C, you may have noticed that since we're
## using On-Off Keying (OOK), it's not obvious where the transmission starts.
## Because of that, URH may have trouble converting this to ASCII.
## So, let's begin our transmission with a preamble.
modulated = ook_modulate([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1], bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 7a
## Writing the binary explicitly is getting somewhat tedious.
## Here's a function that converts a string to binary.
## Like any function, it is only useful if you "call" it
## (in other words, run the function), which you'll see below.
##
## Interested readers may wish to look up "list comprehensions 
##   in Python", but we can use this function without fully 
##   understanding the implementation details.
def str_to_bin_list(mystr):
     bitstrs = [f"{x:08b}" for x in mystr.encode("utf")]
     joined = "".join(bitstrs)
     return list(map(int, joined))


## 7b
## Let's try it. This should print the same list we saw earlier,
## specifically, [0, 1, 0, 0, 0, 0, 1, 1].
list_of_bits = str_to_bin_list("C")
print(list_of_bits)


## 8
## Try this. Verify that it prints the expected sequence of 16 bits.
list_of_bits = str_to_bin_list("Hi")
print(list_of_bits)


## 9
## Now that we can use str_to_bin_list, it's much easier to send messages.
## Try this:
list_of_bits = str_to_bin_list("Hi")
modulated = ook_modulate(list_of_bits, bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 10
## You may have noticed an issue: we've lost our preamble.
## We're going to use the same symbol we used before, "«", whose binary
## representation (10101011) has two characteristics that we want:
##  - it starts with a 1
##  - it alternates between 1 and 0 often, which makes it recognizable
## Let's send a message with that preamble, and interpret it with URH.
list_of_bits = str_to_bin_list("«Hi")
modulated = ook_modulate(list_of_bits, bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)


## 11
## Copy and modify the previous example to use input() to 
## ask the user for a string to send.
## Once the user has provided a string, prepend our preamble 
## before sending the message.


## 12
## Copy and modify the previous example to ask the user for
##  - a string to send
##  - the bit length
## As before, include a preamble.
```
