"""
A collection of misc functions
and such for this class.

Try this to start: wave_gen_prompts()
"""


import numpy as np
import matplotlib.pyplot as plt
import deal
from typeguard import typechecked

from pcdr.fileio import writeRealCSV, writeRaw, writeComplexCSV


@typechecked
def createTimestamps(seconds: float, num_samples: int) -> np.ndarray:
    return np.linspace(
            start=0,
            stop=seconds,
            num=num_samples,
            endpoint=False
        )


@typechecked
def makeRealWave(timestamps: np.ndarray, freq):
    return np.float32(np.sin(freq * 2 * np.pi * timestamps))


@typechecked
def makeComplexWave(timestamps, freq):
    return np.complex64(np.exp(1j * freq * 2 * np.pi * timestamps))


@typechecked
@deal.pre(lambda _: _.complex_or_real in ["r", "c"], message="Must choose 'c' or 'r' to specify if real or complex is wanted.")
def waveAndWrite(basename: str, timestamps: np.ndarray, freq, complex_or_real):
    if complex_or_real == "r":
        data = makeRealWave(timestamps, freq)
        writeRealCSV(basename + ".csv", data)
        writeRaw(basename + ".float32", data)
    elif complex_or_real == "c":
        data = makeComplexWave(timestamps, freq)
        writeComplexCSV(basename + ".csv", data)
        writeRaw(basename + ".complex64", data)


def wave_file_gen_prompts():
    print()
    print("This will create a simulated wave, and write it to two files:")
    print(" - A CSV file (for easy viewing in text editors and spreadsheet programs)")
    print(" - Either a raw float32 or complex64 file (for use in GNU Radio, URH, etc)")
    print()

    samp_rate = float(input("Pick a sample rate (samples per second): "))
    max_time = float(input("How many seconds of data would you like to generate? "))
    num_samples_original = samp_rate * max_time
    num_samples = int(num_samples_original)

    if num_samples != num_samples_original:
        raise ValueError(f"The number of samples would be {num_samples_original}, but a partial sample is meaningless.\nPlease pick a sample rate and an amount of time whose product is an integer.")

    freq = float(input("What frequency wave would you like to generate (Hz)? "))
    complex_or_real = input("Complex or Real wave? Enter c or r. ")
    filename = input("Filename? (Press enter to choose the default name, 'generated_data'.) ")
    if filename.strip() == "":
        filename = "generated_data"

    timestamps = createTimestamps(max_time, num_samples)
    print("------------------")
    print(f"Going to generate {int(num_samples)} samples.")
    print("Simulated samples were taken at these times (units are seconds):")
    print(timestamps)

    waveAndWrite(filename, timestamps, freq, complex_or_real)
    print("Done writing files.")


@typechecked
@deal.pre(lambda _: _.complex_or_real in ["r", "c"], message="Must choose 'c' or 'r' to specify if real or complex is wanted.")
def wave_file_gen(samp_rate: float, max_time: float, freq: float, complex_or_real: str, filename: str = 'generated_data'):
    """Units:
    samp_rate: samples per sec
    max_time: seconds
    freq: Hz
    complex_or_real: 'c' or 'r'
    """
    
    num_samples = samp_rate * max_time

    if int(num_samples) != num_samples:
        raise ValueError(f"The number of samples would be {num_samples}, but a partial sample is meaningless.\nPlease pick a sample rate and an amount of time whose product is an integer.")

    timestamps = createTimestamps(max_time, num_samples)

    waveAndWrite(filename, timestamps, freq, complex_or_real)
