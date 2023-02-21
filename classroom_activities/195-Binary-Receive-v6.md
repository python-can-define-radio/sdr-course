Transmit:

```
File Source
  --> Unpack K bits, K = 8
      --> Repeat Interpolation: symbol_length
          --> Uchar to Float
              --> Mix sine wave hier block (created in a different tutorial)
                  --> osmocom sink
```


Receive:

```
osmocom Source
   --> Band Pass Filter 
       --> Complex to Mag
           --> Moving average (length = symbol_length)
               --> Add & Bin Slice (or the fancier threshold block)
                   --> Keep a chunk after sig equals 1
                       --> Keep M in N:
                           M = 1;
                           N = symbol length 
                           offset = symbol_length//2
                              (greatest chance of hitting the middle of a pulse)
                             
                           --> Keep M in N to strip preamble
                               --> Pack K bits: K = 8
                                   --> File Sink
                                   
```
