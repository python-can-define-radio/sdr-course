```python3
timestamps, y_vals = parse_csv(filename_csv, samp_rate)
plt.plot(timestamps, y_vals, "*", markersize=10)
plt.show()
```


```python3
import numpy as np
import matplotlib.pyplot as plt

import pcdr.wavegen as wavegen

## 1
# pcdr.wave_gen_prompts()
```

```python3
# pcdr.plot_from_csv("generated_data.csv", 100)


## 2
wavegen.wave_gen(100, 3, 2, "r", "generated_data")
wavegen.plot_from_csv("generated_data.csv", 100)


## 3
# pcdr.wave_gen(100, 3, 2, "r", "generated_data")
# timestamps, y_vals = pcdr.parse_csv("generated_data.csv", 100)
# plt.plot(timestamps, y_vals, "*", markersize=10)
# plt.show()


## 4  (challenge)
# pcdr.wave_gen(100, 3, 2, "r", "generated_data_part_a")
# pcdr.wave_gen(100, 1, 4, "r", "generated_data_part_b")
# times_a, part_a = pcdr.parse_csv("generated_data_part_a.csv", 100)
# times_b, part_b = pcdr.parse_csv("generated_data_part_b.csv", 100)
# data_together = np.concatenate([part_a, part_b])
# plt.plot(data_together, "*", markersize=10)
# plt.show()
```
