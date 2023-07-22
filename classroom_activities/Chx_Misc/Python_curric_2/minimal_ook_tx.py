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
sender.send([1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])

