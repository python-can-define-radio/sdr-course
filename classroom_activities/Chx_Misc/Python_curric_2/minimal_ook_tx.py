import something_probably_pcdr as stg

## 1
## Try this. Have a neighbor receive the signal in 
##  a spectrum analyzer program such as GQRX,
##  and then in URH.
## How many seconds long is each bit?
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=1e6)
sender.send([1, 0, 1, 0, 1, 0, 0, 1])

## (This part is not for the students)
## Behind the scenes, .send() will...
##   if any are not in [0, 1]: raise ValueError 
##   convert bit_length to an int
##   repeated_bits = pydash flatmap: repeat each item bit_length times 
##   padded_rb = pad repeated_bits with zeros to nearest multiple of 1024
##   chunked = pydash.chunk padded_rb, size=1024
##   np_arrys = list(map(np.array, chunked))
##   q = simplequeue()
##   for item in chunked:
##       q.put(item)
##   tb = instantiate a top block that can .get() from my externally-provided queue
##   tb.start()
##
##   ## Check the queue till it's empty.
     ## This is NOT ideal -- would be better to detect done-ness from
     ##  inside the flowgraph if possible, so that I can use .wait() for its
     ## intended purpose.
##   while not q.isempty:
##       time.sleep(0.1)
## 
##   ## TODO: confirm this is correct order of functions (stop then wait)
##   tb.stop()
##   tb.wait()  
##   


## 2
## Copy and modify the previous example to send a different pattern of bits.


## 3
## Try this.
## How many seconds long is each bit?
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=2e6)
sender.send([1, 0, 1, 0, 1, 0, 0, 1])


## 4
## Try this.
## How many seconds long is each bit?
## How many milliseconds is that?
## How many bits per second are you sending?
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=200e3)
sender.send([1, 0, 1, 0, 1, 0, 0, 1])


## 5
## The ASCII (or Unicode) value for the letter C is 67.
## In binary, that's 1000011.
## Since a byte is 8 bits, let's write that with a leading zero: 01000011.
## Let's try to send it, and receive it using URH.
## You may run into an issue, which we'll discuss in the exercise below.
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=1e6)
sender.send([0, 1, 0, 0, 0, 0, 1, 1])


## 6
## If you tried sending the letter C, you may have noticed that since we're
## using On-Off Keying (OOK), it's not obvious where the transmission starts.
## Because of that, URH may have trouble converting this to ASCII.
## So, let's begin our transmission with a preamble.
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=1e6)
sender.send([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1])


## 7a
## Writing the binary explicitly is getting somewhat tedious.
## Here's a function that converts a string to binary.
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
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=1e6)
sender.send(list_of_bits)


## 10
## You may have noticed an issue: we've lost our preamble.
## We're going to use the same symbol we used before, "«", whose binary
## representation (10101011) has two characteristics that we want:
##  - it starts with a 1
##  - it alternates between 1 and 0 often, which makes it recognizable
## Let's send a message with that preamble, and interpret it with URH.
list_of_bits = str_to_bin_list("«Hi")
sender = stg.osmocom_ook_sender(samp_rate=2e6, bit_length=1e6)
sender.send(list_of_bits)


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



