## Basic OOK Transmitting using Python

ℹ️ This material coincides with material from python slideshows B (slides 1-11, 16, 24, 39, 54-63, 69) C (slides 30-38) and D (slides 4-15, 31-37), and SDR slideshow A (slides 22, 25, 28-32, 40-42).

ℹ️ Prerequisite: `pip install pcdr`

### Introduction

One of the biggest advantages of SDRs is that they allow us to transmit arbitrary modulation schemes. In this lesson, we practice using Python (which is using GNU Radio behind the scenes) to transmit data using On-Off Keying (OOK).

Note: if you don't have a SDR peripheral, or if you don't want to actually transmit, you have a few options, listed below the first example. You can use these alternatives for any of the exercises on this page.

### Sending bits

```python3
from pcdr import gnuradio_send, ook_modulate
import numpy as np


## 1
## Try this. Have a neighbor receive the signal in 
##  a spectrum analyzer program such as GQRX,
##  and then in URH.
## How many seconds long is each bit?
## If you aren't sure, try setting the bit length to something longer,
## like int(8e6). Then, use a stopwatch.
## How does the time for a single bit relate to the bit_length and the samp_rate?
modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6)
```

### Non-transmission alternatives

These alternative options are useful if you don't have a SDR peripheral, or if you don't want to actually transmit.

<details><summary>Click here if you'd like to see them.</summary>

**Option A**: Print the data. In this case, you may wish to use a shorter bit length, for example, `bit_length=4`, as the print output would be impractical due to its length if you kept the original `bit_length`.
   ```python3
   ## Option A example
   modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=4)
   print(modulated)
   ```

**Option B**: Write the data to a file. You can then examine the file using URH or a program of your choice. URH handles fairly large files without too much trouble, so the `bit_length` does not need to change. However, note that you'll need to convert the data to `np.complex64` before writing it.
   ```python3
   ## Option B example
   modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
   complexdata = np.complex64(modulated)
   f = open("generatedfile.complex", "wb")
   f.write(complexdata)
   f.close()
   ```

**Option C**: Plot the data using matplotlib. A `bit_length` value of no more than `50e3` is recommended when using this option due to performance issues.
   ```python3
   ## Option C example
   from pcdr import ook_modulate
   import matplotlib.pyplot as plt
   modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(50e3))
   plt.plot(modulated, "*-")
   plt.show()
   ```

<!-- TODO someday: figure out if this works
**Option D**. Display the data in a QT GUI Sink. You may wish to use the `prepend_zeros` argument, which adds a delay before the actual data. This can help by giving you time to switch to the GUI window before the actual data is displayed.  
   ```python3
   ## Option D example
   from pcdr import gnuradio_guisink, ook_modulate
   modulated = ook_modulate([1, 0, 1, 0, 1, 0, 0, 1], bit_length=int(1e6))
   gnuradio_guisink(modulated, center_freq=2.413e9, samp_rate=2e6, prepend_zeros=int(4e6))
   ```
-->
</details>

### Further practice

```python3
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
```

<!--

TODO: consider

### Sending hexadecimal strings as bits

from pcdr import hex_to_bin_list
list_of_bits = hex_to_bin_list(0x43)
print(list_of_bits)

-->

### Sending text as bits

Writing the binary explicitly is getting somewhat tedious. The pcdr module includes a `str_to_bin_list` function that converts a string to binary. Let's try it:

```python3
## 7
## Try this. It should print the same list we saw earlier,
## specifically, [0, 1, 0, 0, 0, 0, 1, 1].
from pcdr import str_to_bin_list
list_of_bits = str_to_bin_list("C")
print(list_of_bits)


## 8
## Try this. Verify that it prints the expected sequence of 16 bits.
## (You can use an online ASCII-to-binary converter to verify.)
list_of_bits = str_to_bin_list("Hi")
print(list_of_bits)


## 9
## Now that we can use str_to_bin_list, it's much easier to create messages.
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


## 13
## Open a text file using f = open(...).
## Modulate and send the contents using the above examples.


## 14
## Use a `for` loop to send the same message 5 times.
## Note: if you're using f.write() with the data that you're
## generating, you may wish to append to the file rather than
## overwriting it.


## 15
## Use a `while` loop to repeatedly send a message forever.
## Use time.sleep to put a 1 second delay between messages.
## Note: if you're using f.write(), you'll probably want to skip
## this to avoid filling your hard drive.
```

The `gnuradio_send` function has a built in option for repeating, shown in the example below. This has the advantage of having no delay between repeats (if that's your goal).

```python3
## 16
## Try this.
modulated = ook_modulate([1, 0], bit_length=int(100e3))
gnuradio_send(modulated, center_freq=2.413e9, samp_rate=2e6, repeat=True)
```

### Further exercises:

```python3
## 17
## Using a loop, repeatedly ask for frequencies.
## Transmit on the chosen frequency for 2 seconds.
## Then ask for the next transmit frequency.

## 18
## Jam two radio stations by randomly picking between the two.
## The logic will look like this:
while 2 + 2 == 4:
    freq = random.choice([104.5e6, 105.3e6])
    ## you'll add something here.
```
