Simulation:

```
                                   --> Time Sink
Signal Source  -->  Complex to Mag --> Add const --> Binary Slicer --> Keep 1 in N --> UChar to Float --> Time Sink
               -->  Time Sink                                      
```


- Make the sig source amplitude slidable from 0 to 1
- add const: 
  - constant: `-0.5`

Once you've tested this, change the signal Source to Osmocom source with adjustable IF and BB gains

Finally, after adjusting the `Keep 1 in N` appropriately, you can add a file sink after the `Keep 1 in N`. Make sure that the file you create is reasonable size -- they often grow very quickly!!

You probably want a `Pack K Bits` too.
