## Is the "Pack Bits" block enough?

The "Pack Bits" block works great when you have a sequence of bits. However, in many cases, you have something like this:

```
     •••••     ••••••••••

•••••     •••••          •••••
```

Notice that each "on" or "off" pulse appears to be 5 samples. How do we discard the extras?

## Changing the sample rate

In an earlier exercise, we created these sequences of zeros and ones using a Repeat block. In this exercise, we'll learn about the opposite block: "Keep 1 in N".

Here's the first flowgraph to start exploring:

`keep_1_in_n_explore.grc`

```
Vector source  -->  Python Block: Print
               -->  Time sink
```

Vector source:
- Type: `float`
- Vector: _make up a random sequence of numbers_
- Repeat: `yes`

Print block and Time sink: Try various parameters.

Once you get that flowgraph running, try inserting the Keep 1 in N block, and see if you can get an intuition for what it's doing.

## 1's and zeros

In your `keep_1_in_n_explore.grc` flowgraph that you just created, change the Vector to `[1, 1, 1, 0, 0, 0]`.

How would you do a keep 1 in N to get rid of the sequential duplicates, so that the print block and the time sink just show the pattern 1, 0, 1, 0,... ?
