"""
A collection of misc functions
and such for this class.

Try this to start: wave_gen_prompts()
"""


import numpy as np
import matplotlib.pyplot as plt



def createTimestamps(amount_of_time, num_samples):
    return np.linspace(
            start=0,
            stop=amount_of_time,
            num=int(num_samples),
            endpoint=False
        )


def writeRealCSV(filename, data_to_write):
    with open(filename, "w") as outfile:
        for item in data_to_write:
            outfile.write(f"{item}\n")


def writeComplexCSV(filename, data_to_write):
    with open(filename, "w") as outfile:
        for item in data_to_write:
            inphase = item.real
            quad = item.imag
            outfile.write(f"{inphase},{quad}\n")


def writeRaw(filename, data_to_write):
    with open(filename, "wb") as outfile:
        outfile.write(data_to_write)
        outfile.close()


def makeRealWave(timePoints, freq):
    return np.float32(np.cos(freq * 2 * np.pi * timePoints))


def makeComplexWave(timePoints, freq):
    return np.complex64(np.exp(1j * freq * 2 * np.pi * timePoints))


def waveAndWrite(basename, timestamps, freq, complex_or_real):
    if complex_or_real == "r":
        data = makeRealWave(timestamps, freq)
        writeRealCSV(basename + ".csv", data)
        writeRaw(basename + ".float32", data)
    elif complex_or_real == "c":
        data = makeComplexWave(timestamps, freq)
        writeComplexCSV(basename + ".csv", data)
        writeRaw(basename + ".complex64", data)
    else:
        raise ValueError("Must enter c or r to specify if real or complex is wanted.")


def wave_gen_prompts():
    print()
    print("This will create a simulated wave, and write it to two files:")
    print(" - A CSV file (for easy viewing in text editors and spreadsheet programs)")
    print(" - Either a raw float32 or complex64 file (for use in GNU Radio, URH, etc)")
    print()

    samp_rate = float(input("Pick a sample rate (samples per second): "))
    max_time = float(input("How many seconds of data would you like to generate? "))
    num_samples = samp_rate * max_time

    if int(num_samples) != num_samples:
        raise ValueError(f"The number of samples would be {num_samples}, but a partial sample is meaningless.\nPlease pick a sample rate and an amount of time whose product is an integer.")

    freq = float(input("What frequency wave would you like to generate (Hz)? "))
    complex_or_real = input("Complex or Real wave? Enter c or r: ")

    timestamps = createTimestamps(max_time, num_samples)
    print("------------------")
    print(f"Going to generate {int(num_samples)} samples.")
    print("Simulated samples were taken at these times (units are seconds):")
    print(timestamps)

    waveAndWrite("generated_data", timestamps, freq, complex_or_real)
    print("Done writing files.")


def plot_from_file():
    with open("generated_data.csv") as f:
        contents = f.read().splitlines()

    samp_rate = float(input("What is the sample rate? "))
    num_samples = len(contents)
    max_time = num_samples / samp_rate
    timestamps = createTimestamps(max_time, num_samples)
    contents_as_numbers = list(map(float, contents))
    plt.plot(timestamps, contents_as_numbers, "*", markersize=10)
    plt.show()
