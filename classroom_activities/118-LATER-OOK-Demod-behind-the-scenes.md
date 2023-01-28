_Note: This exercise isn't finished. Feel free to skip for now._

First, we're going to simulate receiving a perfect signal.

`OOK_receive_simulation_1.grc`

```
GUI Range


       |-->  Waterfall
       |     Sink     
       |
       |-->  Time     |--> Time    |--> Time
       |     Sink     |    Sink    |    Sink
       |              |            |
Signal --->  Complex  -->  Add     -->  Binary  --> Throttle  --> UChar to  --> Time 
Source       to Mag        const        Slicer                    Float         Sink
```

Parameters:

- GUI Range: 
  - Id: `amplitu`
  - Default Value: `1`
  - Start: `0`
  - Stop: `1`
- Signal Source:
  - Amplitude: `amplitu`
- Add Const: 
  - constant: `-0.3`

Slide the GUI Range, and observe all the sinks. 

## Getting rid of the extra data

Make a copy of the same flowgraph, and name it `OOK_receive_simulation_2.grc`.

We're keeping all of the blocks, and adding two: a `Variable` and `Keep 1 in N`.

```
Variable

EVERYTHING ELSE -->  Keep   -->  UChar to  -->  Time     
                     1 in N      Float          Sink
```

Parameters:
- Variable:
  - Id: `N_for_keeper_block`
  - Value: `100`
- Keep 1 in N:
  - N: `N_for_keeper_block`
- Time Sink:
  - Number of Points: `2000`
  - Sample Rate: `samp_rate / N_for_keeper_block`
