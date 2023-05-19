For detecting a single peak.

```
sig ->
Stream to vec ->
FFT  ->
complex to mag ->
argmax  -> (max_vec output) ->
add const: -512  ->
Short to float ->
multiply const: samp_rate/fftsize
```
