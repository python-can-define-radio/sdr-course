Imagine you have this signal:

```

5  |                                 
   |                               
4  |                •         • •     
   |            • •• •      •• • •         
3  |             •                  
   |                               
2  |                               
   |      •   •       • ••••             
1  |     • •••         •                
   |                                 
0  ------------------------------------

```

It looks similar to OOK, but there's some noise. However, the noise isn't terribly large, so there should be enough space in between the high points and low points that we can clearly determine whether something is high or low.

What block does this "slicing" between high and low?

## Binary Slicer

As per the [documentation](https://wiki.gnuradio.org/index.php/Binary_Slicer), the Binary Slicer block "slices a float value producing 1 bit output. Positive input produces a binary 1 and negative input produces a binary zero."

Let's try it:

```
Vector source  -->  Binary Slicer --> UChar to Float --> Print block
```

Try various vectors (without repeat) and see what happens.

## What if my data isn't negative?

You may have noticed that the data in the example above is approx 1 or 2 when it's low, and approx 3 or 4 when it's high. So, we would probably want to slice at 2.5, but the Binary Slicer block only slices around zero.

So, we need to shift the data down to be centered around zero by subtracting 2.5. There's no "Subtract constant" block, but you can use the "Add const" with `-2.5`. You'll get practice in the next exercise.

