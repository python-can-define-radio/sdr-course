We've seen that a wave can express binary data. Specifically, we've discussed using On-Off Keying (OOK). 

We humans can easily see the on-off pattern in the wave; what block should we use to automate this?

## Complex waves

Up to this point, we've been postponing the explanation of why there are two waves to express a single signal. We still won't have a full discussion of that, but here's what you need to know now:

- In a typical (purely real) sine wave, you would most likely need to see a good portion of the wave to know its amplitude. For example, a full cycle would be enough to see the peak and the trough -- based on that, you could be fairly confident of the wave's amplitude.
- On the other hand, in a complex sine wave (meaning one that has both real and imaginary parts), you can know the amplitude based on a _single complex sample_.

If this doesn't make sense, it's ok -- this is a fairly deep concept, but it's not necessary to understand deeply for the sake of the next few topics. (For those who are interested in a deep-dive, look up "IQ data" in your search engine of choice. I have not yet found an explanation that I find satisfying, but let me know if you find one.)

## Complex to mag 

It turns out that there's a block that "converts" a wave into its amplitude, called Complex to Mag. (Again, I'm avoiding going into details of why this works for now.)

You'll experiment with it in the next exercise. 