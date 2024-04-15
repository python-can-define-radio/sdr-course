These are terms that relate to GNU Radio and/or to SDRs in general. 

**Decimate, Decimation**: Reduce the sample rate of a signal.  
ℹ️ This definition coincides with material from SDR slideshow A (slides 22, 25, 28-32, 40-42).  
Decimation is a mathematical operation that reduces the original sample rate of a sequence to a lower rate. It is the opposite of interpolation. In mathematics, decimation refers to the creation of a new sequence comprising only every n-th element of a source sequence.1.

Common reasons to do this include...

- Hardware compatibility: A common SDR use-case is demodulating and playing sound. Sound cards usually only allow sample rates up to 48 thousand samples per second, while SDR hardware often samples at much high rates, such as 2 million samples per second.
- Reduced computational effort and storage space: Generally speaking, decreasing the number of samples helps with both of these.

**Interpolate, Interpolation**: Increase the sample rate of a signal.  
The word "Extrapolate" is fairly common in non-technical English. The word "Interpolate" has a related meaning.
As used in mathematics the definition of interpolation is: The insertion of an intermediate value or term into a series by estimating or calculating it from surrounding known values.

**Sample Rate**: (todo)

**Sink**: in GNU Radio, a block that has "in" ports (data can flow into it), but no "out" ports.  
Common sinks that we use:

- GUI Sinks (Display data in a Graphical User Interface)
- File Sinks (Write data to a file)
- osmocom Sink (transmits data using an osmocom-compatible device)

