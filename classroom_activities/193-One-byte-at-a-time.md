_UNFINISHED_

We could do this:

- Use Keep M in N to keep every 8 out of 16 bits, with an offset of 8 (because it keeps the FIRST 8 and we want it to skip the first 8.)
- This will throw away each preamble as it arrives, and solve the issue of clock sync because the clock gets re synced every 16 bits.

Another (possibly better) option is that we can use our knowledge of the preamble to see if the packet "looks right":

- If the first 8 bits are as expected (10101010), then there's a higher chance that the rest is real data as opposed to random noise.

