These are terms that relate to GNU Radio and/or to SDRs in general. 

**Decimate, Decimation**: Reduce the sample rate of a signal. Common reasons to do this include...

- Hardware compatibility: A common SDR use-case is demodulating and playing sound. Sound cards usually only allow sample rates up to 48 thousand samples per second, while SDR hardware often samples at much high rates, such as 2 million samples per second.
- Reduced computational effort and storage space: Generally speaking, decreasing the number of samples helps with both of these.

**Sample Rate**: (todo)

**Sink**: in GNU Radio, a block that has "in" ports (data can flow into it), but no "out" ports.  
Common sinks that we use:

- GUI Sinks (Display data in a Graphical User Interface)
- File Sinks (Write data to a file)
- osmocom Sink (transmits data using an osmocom-compatible device)

