import matplotlib.pyplot as plt

from wave_gen import createTimestamps


with open("generated_data.csv") as f:
    contents = f.read().splitlines()

samp_rate = float(input("What is the sample rate? "))
num_samples = len(contents)
max_time = num_samples / samp_rate
timestamps = createTimestamps(max_time, num_samples)
contents_as_numbers = list(map(float, contents))
plt.plot(timestamps, contents_as_numbers, "*", markersize=10)
plt.show()

