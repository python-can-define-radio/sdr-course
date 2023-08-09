from typing import Iterable, Callable
from typeguard import typechecked



@typechecked
def writeRealCSV(filename: str, data_to_write: Iterable):
    with open(filename, "w") as outfile:
        for item in data_to_write:
            outfile.write(f"{item}\n")


@typechecked
def writeComplexCSV(filename: str, data_to_write: Iterable):
    with open(filename, "w") as outfile:
        for item in data_to_write:
            inphase = item.real
            quad = item.imag
            outfile.write(f"{inphase},{quad}\n")


def writeRaw(filename, data_to_write):
    with open(filename, "wb") as outfile:
        outfile.write(data_to_write)
        outfile.close()


@typechecked
def __readCSV(filename_csv: str, samp_rate: float, type_: Callable) -> tuple:
    
    ## This import must be here to avoid circular imports.
    from pcdr.wavegen import createTimestamps

    with open(filename_csv) as f:
        contents = f.read().splitlines()
    
    num_samples = len(contents)
    max_time = num_samples / samp_rate
    timestamps = createTimestamps(max_time, num_samples)
    contents_as_numbers = list(map(type_, contents))
    return timestamps, contents_as_numbers


@typechecked        
def readRealCSV(filename_csv: str, samp_rate: float) -> tuple:
    __readCSV(filename_csv, samp_rate, float)


@typechecked        
def readComplexCSV(filename_csv: str, samp_rate: float) -> tuple:
    __readCSV(filename_csv, samp_rate, complex)
