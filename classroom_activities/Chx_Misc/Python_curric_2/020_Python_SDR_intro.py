import numpy as np
import matplotlib.pyplot as plt

import pcdr

## 1
# pcdr.wave_gen_prompts()
# pcdr.plot_from_csv("generated_data.csv", 100)


## 2
pcdr.wave_gen(100, 3, 2, "r", "generated_data")
pcdr.plot_from_csv("generated_data.csv", 100)


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
