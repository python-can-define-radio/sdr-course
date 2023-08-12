from __future__ import annotations

from typing import Iterable, Callable, Any, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import FileDescriptorOrPath

import numpy as np

from pcdr.types_and_contracts import TRealNum



def writeRealCSV(filename, data_to_write):
    # type: (FileDescriptorOrPath, Iterable[TRealNum]) -> None
    with open(filename, "w") as outfile:
        for item in data_to_write:
            outfile.write(f"{item}\n")


def writeComplexCSV(filename, data_to_write):
    # type: (FileDescriptorOrPath, Iterable[complex]) -> None
    with open(filename, "w") as outfile:
        for item in data_to_write:
            inphase = item.real
            quad = item.imag
            outfile.write(f"{inphase},{quad}\n")


def __readCSV(filename_csv: FileDescriptorOrPath, samp_rate: float, type_: Callable) -> Tuple[np.ndarray, np.ndarray]:
    
    ## This import must be here to avoid circular imports.
    from pcdr.wavegen import createTimestamps

    with open(filename_csv) as f:
        contents = f.read().splitlines()
    
    num_samples = len(contents)
    max_time = num_samples / samp_rate
    timestamps = createTimestamps(max_time, num_samples)
    contents_as_numbers = np.array(list(map(type_, contents)))
    return timestamps, contents_as_numbers


def readRealCSV(filename_csv: FileDescriptorOrPath, samp_rate: float) -> Tuple[np.ndarray, np.ndarray]:
    __readCSV(filename_csv, samp_rate, float)


def readComplexCSV(filename_csv: FileDescriptorOrPath, samp_rate: float) -> Tuple[np.ndarray, np.ndarray]:
    __readCSV(filename_csv, samp_rate, complex)
