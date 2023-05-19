## Skipping the beginning

Another block that comes in handy is "skip head". This is useful when you have a packet of data that starts with a preamble that you wish to disregard. (You may wish to refer to the earlier exercise that defines a preamble).

To explore the Skip Head block, use a flowgraph similar to the one in the `Keep-1-in-N` exercise:

`skip_head_explore.grc`

```
Vector source  -->  Print block
               -->  Time sink
```

Insert a "Skip Head" block and experiment to see what it does. You'll most likely want to set the Vector's repeat to "no". Also, remember that the time sink won't display unless you have enough data to exceed the Number of Points, so you'll want to set the Number of Points to a low value.