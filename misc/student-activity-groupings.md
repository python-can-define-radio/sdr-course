1. `050, 051, 052` (Sample Rates 1, Sample Rates 2, Sample Rates 3)
2. `053` (Sample Rates 4)
3. `054` (Sample Rates 5)
4. `055, 056` (Sample Rates 6, Sample Rates 7)
5. `060, 061` (Python Block, Custom Python Print Block)
6. `065` (Unicode and File Source)
7. `068, 070` (File Sink, Sig interpret bits manual)
8. `085` (Packing and unpacking)
9. `090` (Sig interpret practice 3)
10. `095, 100` (Keep 1 in N, Skip Head)
11. `110` (Sig interpret practice 4)
12. `120, 130` (Binary Slicer, Sig interpret practice 5)
13. `140, 145a, 145b, 150` (Complex to mag, sig interpret practice, sig interpret practice, sig interpret practice 6) (**NOTE: THIS ONE IS LONG**)
14. `160, 170` (Band pass filter, sig interpret practice 7)


```python3
import random

nums = list(range(1, 11+1))
print(random.sample(nums, k=len(nums)))
```

Reminder of how to run a local server in the Linux Terminal:

```
python3 -m http.server
```
