import numpy as np
import random
from typing import Optional, List, Tuple, Literal
from pcdr.fileio import writeRealCSV, writeComplexCSV
from pcdr.modulators import ook_modulate
from pcdr.helpers import str_to_bin_list
from typeguard import typechecked



def createTimestamps(seconds: float, num_samples: int, dtype=np.float64) -> np.ndarray:
    """Creates timestamps from zero up to the given maximum number of seconds.
    Implemented using np.linspace().
    
    Note: We use np.float64 as the default dtype because np.float32 was causing float rounding issues
    that became worse with larger time values (as float rounding issues usually do).
    
    Example:
    >>> createTimestamps(2, 10)
    array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8])
    """
    assert 0 <= seconds
    assert 0 <= num_samples
    result = np.linspace(
        start=0,
        stop=seconds,
        num=num_samples,
        endpoint=False,
        dtype=dtype
    )
    assert result.dtype == dtype
    assert len(result) == num_samples
    assert (0 <= result).all()
    return result


def createTimestamps_samprate(samp_rate: float, num_samples: int, dtype=np.float64) -> np.ndarray:
    """Creates `num_samples` timestamps spaced by `1/samp_rate`.
    Implemented using np.linspace().
    
    Examples:
    >>> createTimestamps_samprate(5, 10)
    array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8])

    >>> createTimestamps_samprate(10, 4)
    array([0. , 0.1, 0.2, 0.3])

    Note: We use np.float64 as the default dtype because np.float32 was causing float rounding issues
    that became worse with larger time values (as float rounding issues usually do)."""
    assert 0 < samp_rate
    assert 0 <= num_samples
    
    result = np.linspace(
            start=0,
            stop=num_samples/samp_rate,
            num=num_samples,
            endpoint=False,
            dtype=dtype
        )
    
    assert result.dtype == dtype
    assert len(result) == num_samples
    assert (0 <= result).all()

    return result


#### This is something we may do eventually.
# @overload
# def makeRealWave(samp_rate: float,
#                  freq: float,
#                  num_samples: int,
#                  allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]: ...
# @overload
# def makeRealWave(samp_rate: float,
#                  freq: float,
#                  seconds: float,
#                  allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]: ...
# def makeRealWave(samp_rate: float,
#                  freq: float,
#                  **kwargs):
#     return something


def makeRealWave_basic(timestamps: np.ndarray, freq: float) -> np.ndarray:
    """Return a sine wave.
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps = createTimestamps(1, 50)
    >>> wave = makeRealWave_basic(timestamps, 2)
    >>> plot(timestamps, wave)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    result = np.float32(np.sin(freq * 2 * np.pi * timestamps))
    assert timestamps.shape == result.shape
    return result


def makeComplexWave_basic(timestamps: np.ndarray, freq: float) -> np.ndarray:
    """Return a complex wave.
    
    The real part is cosine (starts at 1); the imaginary part is sine (starts at 0).
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps = createTimestamps(1, 50)
    >>> wave = makeComplexWave_basic(timestamps, 2)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~o████████████████████████o████████████████████████
    ~█ooo██████████████████ooo█ooo██████████████████ooo
    ~████o████████████████o██████o█████████████████o███
    ~█████o██████████████o█████████o██████████████o████
    ~██████o████████████o███████████o████████████o█████
    ~███████o██████████o█████████████o██████████o██████
    ~████████oo██████oo███████████████oo██████oo███████
    ~██████████oooooo███████████████████oooooo█████████
    >>> plot(timestamps, wave.imag)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    ## Note: I don't know enough about math with complex numbers
    ## to know if freq should be restricted to real, but I figured
    ## it was better to type-annotate it as `float` rather than leaving
    ## it as `Any`.
    result = np.complex64(np.exp(1j * freq * 2 * np.pi * timestamps))
    assert timestamps.shape == result.shape
    return result



class AliasError(ValueError):
    pass



def isAliasingWhenDisallowed(allowAliasing: bool, freq: float, samp_rate: float) -> bool:
    """
    Examples:

    >>> allowAliasing = False
    >>> samp_rate = 5
    >>> too_high_freq = 4
    >>> acceptable_freq = 2
    >>> isAliasingWhenDisallowed(allowAliasing, too_high_freq, samp_rate)
    True
    >>> isAliasingWhenDisallowed(allowAliasing, acceptable_freq, samp_rate)
    False
    >>> allowAliasing = True
    >>> isAliasingWhenDisallowed(allowAliasing, too_high_freq, samp_rate)
    False
    >>> isAliasingWhenDisallowed(allowAliasing, acceptable_freq, samp_rate)
    False
    """
    return (not allowAliasing) and (abs(freq) > samp_rate/2)


def aliasingError(allowAliasing: bool, freq: float, samp_rate: float) -> None:
    """Gives a detailed Aliasing error message if it's aliasing when it shouldn't.
    :raises AliasError:"""
    if isAliasingWhenDisallowed(allowAliasing, freq, samp_rate):
        raise AliasError(f"For a sample rate of {samp_rate}, the highest frequency that can be faithfully represented is {samp_rate/2}. The specified freq, {freq}, is greater than the limit specified by Shannon/Nyquist/Kotelnikov/Whittaker (commonly called the Nyquist frequency).")


def makeComplexWave_numsamps(num_samples: int, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns a tuple (timestamps, wave).
    
    The real part of the wave is cosine (starts at 1); the imaginary part is sine (starts at 0).

    :raises AliasError: if isAliasingWhenDisallowed
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps, wave = makeComplexWave_numsamps(50, 50, 2)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~o████████████████████████o████████████████████████
    ~█ooo██████████████████ooo█ooo██████████████████ooo
    ~████o████████████████o██████o█████████████████o███
    ~█████o██████████████o█████████o██████████████o████
    ~██████o████████████o███████████o████████████o█████
    ~███████o██████████o█████████████o██████████o██████
    ~████████oo██████oo███████████████oo██████oo███████
    ~██████████oooooo███████████████████oooooo█████████
    >>> plot(timestamps, wave.imag)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    assert 0 < samp_rate
    assert 0 <= num_samples
    aliasingError(allowAliasing, freq, samp_rate)
    t = num_samples / samp_rate
    timestamps = createTimestamps(seconds=t, num_samples=num_samples)
    wave = makeComplexWave_basic(timestamps, freq)
    assert len(timestamps) == len(wave) == num_samples
    return timestamps, wave


def makeRealWave_numsamps(num_samples: int, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return a Real wave.

    :raises AliasError: if isAliasingWhenDisallowed
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps, wave = makeRealWave_numsamps(50, 50, 2)
    >>> plot(timestamps, wave)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    assert 0 < samp_rate
    assert 0 <= num_samples
    aliasingError(allowAliasing, freq, samp_rate)
    t = num_samples / samp_rate
    timestamps = createTimestamps(seconds=t, num_samples=num_samples)
    wave = makeRealWave_basic(timestamps, freq)
    assert len(timestamps) == len(wave) == num_samples
    return timestamps, wave


def makeComplexWave_time(seconds: float, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns a tuple (timestamps, wave).
    
    The real part of the wave is cosine (starts at 1); the imaginary part is sine (starts at 0).

    :raises AliasError: if isAliasingWhenDisallowed
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps, wave = makeComplexWave_time(1, 50, 2)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~o████████████████████████o████████████████████████
    ~█ooo██████████████████ooo█ooo██████████████████ooo
    ~████o████████████████o██████o█████████████████o███
    ~█████o██████████████o█████████o██████████████o████
    ~██████o████████████o███████████o████████████o█████
    ~███████o██████████o█████████████o██████████o██████
    ~████████oo██████oo███████████████oo██████oo███████
    ~██████████oooooo███████████████████oooooo█████████
    >>> plot(timestamps, wave.imag)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    assert 0 < samp_rate
    aliasingError(allowAliasing, freq, samp_rate)
    num_samples = int(samp_rate * seconds)
    timestamps = createTimestamps(seconds, num_samples)
    wave = makeComplexWave_basic(timestamps, freq)
    assert len(timestamps) == len(wave) == num_samples
    return timestamps, wave


def makeRealWave_time(seconds: float, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return a Real wave.

    :raises AliasError: if isAliasingWhenDisallowed
    
    Example:
    >>> from pcdr.basictermplot import plot
    >>> timestamps, wave = makeRealWave_time(1, 50, 2)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~██████o████████████████████████o██████████████████
    ~████oo█ooo██████████████████o█o█ooo███████████████
    ~██oo██████o████████████████oo██████o██████████████
    ~█o█████████o██████████████o█████████o█████████████
    ~o███████████oo███████████o███████████oo███████████
    ~██████████████o█████████o██████████████o█████████o
    ~███████████████o██████oo████████████████o██████oo█
    ~████████████████oooooo███████████████████oooooo███
    """
    assert 0 < samp_rate
    aliasingError(allowAliasing, freq, samp_rate)
    num_samples = int(samp_rate * seconds)
    timestamps = createTimestamps(seconds, num_samples)
    wave = makeRealWave_basic(timestamps, freq)
    assert len(timestamps) == len(wave) == num_samples
    return timestamps, wave


@typechecked
def makeWave(samp_rate: float,
             freq: float,
             type_: Literal["real", "complex"],
             *, seconds: Optional[float] = None,
             num: Optional[float] = None,
             allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    TODO:
     - finish writing tests
     - Write implementation that makes these tests pass
     - Change lessons to use makeWave
     - Add @typechecked to all funcs in this file
    
    >>> from pcdr.basictermplot import plot
    >>> timestamps, wave = makeWave(50, 3, "real", seconds=1)
    >>> plot(timestamps, wave)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~████o████████████████o████████████████████████████
    ~███o█oo████████████oo█o█████████████oooo██████████
    ~██o████o██████████o████o███████████o████o█████████
    ~█o██████████████████████o█████████o██████o████████
    ~o███████o████████o███████o███████o████████o███████
    ~█████████o██████o█████████o██████████████████████o
    ~██████████o████o███████████o████o██████████o████o█
    ~███████████oooo█████████████o█oo████████████oooo██

    >>> timestamps, wave = makeWave(50, 3, "complex", seconds=1)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~o█████████████████████████████████████████████████
    ~█oo████████████oooo█████████████oooo████████████oo
    ~██████████████o████o███████████o████o█████████████
    ~███o█████████o██████o█████████o██████o█████████o██
    ~████o████████████████o██████o█████████████████o███
    ~█████o██████o█████████o█████o█████████o██████o████
    ~██████o████o███████████████████████████o████o█████
    ~███████oooo████████████ooooo████████████oooo██████

    >>> plot(timestamps, wave.imag)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~████o████████████████o████████████████████████████
    ~███o█oo████████████oo█o█████████████oooo██████████
    ~██o████o██████████o████o███████████o████o█████████
    ~█o██████████████████████o█████████o██████o████████
    ~o███████o████████o███████o███████o████████o███████
    ~█████████o██████o█████████o██████████████████████o
    ~██████████o████o███████████o████o██████████o████o█
    ~███████████oooo█████████████o█oo████████████oooo██

    >>> timestamps, wave = makeWave(50, 3, "real", num=60)
    >>> plot(timestamps, wave)
    xmin: 0
    xmax: 1.18
    ymin: 0
    ymax: 1.0
    ~████o████████████████o████████████████████████████████o█████
    ~███o█oo████████████oo█o█████████████oooo█████████████o█oo███
    ~██o████o██████████o████o███████████o████o███████████o████o██
    ~█o██████████████████████o█████████o██████o█████████o████████
    ~o███████o████████o███████o███████o████████o███████o██████o██
    ~█████████o██████o█████████o██████████████████████o█████████o
    ~██████████o████o███████████o████o██████████o████o███████████
    ~███████████oooo█████████████o█oo████████████oooo████████████

    >>> timestamps, wave = makeWave(50, 3, "complex", num=60)
    >>> plot(timestamps, wave.real)
    xmin: 0
    xmax: 1.18
    ymin: 0
    ymax: 1.0
    ~o█████████████████████████████████████████████████o█████████
    ~█oo████████████oooo█████████████oooo████████████oo█oo███████
    ~██████████████o████o███████████o████o███████████████████████
    ~███o█████████o██████o█████████o██████o█████████o█████o██████
    ~████o████████████████o██████o█████████████████o███████o█████
    ~█████o██████o█████████o█████o█████████o██████o█████████o████
    ~██████o████o███████████████████████████o████o███████████o███
    ~███████oooo████████████ooooo████████████oooo█████████████o█o
    >>> plot(timestamps, wave.imag)
    xmin: 0
    xmax: 1.18
    ymin: 0
    ymax: 1.0
    ~████o████████████████o████████████████████████████████o█████
    ~███o█oo████████████oo█o█████████████oooo█████████████o█oo███
    ~██o████o██████████o████o███████████o████o███████████o████o██
    ~█o██████████████████████o█████████o██████o█████████o████████
    ~o███████o████████o███████o███████o████████o███████o██████o██
    ~█████████o██████o█████████o██████████████████████o█████████o
    ~██████████o████o███████████o████o██████████o████o███████████
    ~███████████oooo█████████████o█oo████████████oooo████████████
    
    >> makeWave(10, 2, "real")
    Traceback:
      ...
    ValueError: Must specify either `seconds` or `num`
    >> makeWave(10, 2, "complex", seconds=3, num=60)
    Traceback:
      ...
    ValueError: Cannot specify both `seconds` or `num` simultaneously
    >> makeWave(10, 7, "real", seconds=3)
    Traceback:
      ...
    For a sample rate of 10, the highest frequency ...
    >> makeWave(10, 7, "real", seconds=3, allowAliasing=True) == makeRealWave_time(3, 10, 2, allowAliasing=True)
    True
    """
    if seconds != None and num != None:
        raise ValueError("Cannot specify both `seconds` and `num` simultaneously")
    elif seconds == None and num == None:
        raise ValueError("Must specify either `seconds` or `num`")
    elif seconds != None:
        if type_ == "real":
            return makeRealWave_time(seconds, samp_rate, freq, allowAliasing)
        elif type_ == "complex":
            return makeComplexWave_time(seconds, samp_rate, freq, allowAliasing)
        else:
            raise ValueError("This will never happen if the @typechecked works")
    elif num != None:
        if type_ == "real":
            return makeRealWave_numsamps(num, samp_rate, freq, allowAliasing)
        elif type_ == "complex":
            return makeComplexWave_numsamps(num, samp_rate, freq, allowAliasing)
        else:
            raise ValueError("This will never happen if the @typechecked works")
    else:
        raise Exception("Impossible case")
    

def waveAndWrite(basename: str, timestamps: np.ndarray, freq, complex_or_real: Literal["c", "r"]):
    if complex_or_real == "r":
        data = makeRealWave_basic(timestamps, freq)
        writeRealCSV(basename + ".csv", data)
        data.tofile(basename + ".float32")
    elif complex_or_real == "c":
        data = makeComplexWave_basic(timestamps, freq)
        writeComplexCSV(basename + ".csv", data)
        data.tofile(basename + ".complex64")
    else:
        raise ValueError("Must choose 'c' or 'r' to specify if real or complex is wanted.")


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


def multiply_by_complex_wave(baseband_sig: np.ndarray, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns a tuple (timestamps, mult).

    >>> from pcdr.basictermplot import plot
    >>> from pcdr.wavegen import multiply_by_complex_wave, ook_modulate
    >>> baseband_sig = ook_modulate([1, 0], 32)
    >>> timestamps, mult = multiply_by_complex_wave(baseband_sig, 64, 2)
    >>> plot(timestamps, mult.real)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~o███████████████████████████████████████████████████████████████
    ~█ooo█████████████████████████ooo████████████████████████████████
    ~████oo█████████████████████oo███████████████████████████████████
    ~██████oo█████████████████oo█████████████████████████████████████
    ~████████o███████████████o███████oooooooooooooooooooooooooooooooo
    ~█████████oo███████████oo████████████████████████████████████████
    ~███████████oo███████oo██████████████████████████████████████████
    ~█████████████ooooooo████████████████████████████████████████████
    """
    timestamps, wave = makeComplexWave_numsamps(len(baseband_sig), samp_rate, freq, allowAliasing)
    mult = np.complex64(baseband_sig) * wave
    assert len(timestamps) == len(mult) == len(baseband_sig)
    assert timestamps.dtype == np.float64
    assert mult.dtype == np.complex64
    return timestamps, mult


def multiply_by_real_wave(baseband_sig: np.ndarray, samp_rate: float, freq: float, allowAliasing: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns a tuple (timestamps, mult).

    >>> from pcdr.basictermplot import plot
    >>> from pcdr.wavegen import multiply_by_real_wave, ook_modulate
    >>> baseband_sig = ook_modulate([1, 0], 32)
    >>> timestamps, wave = multiply_by_real_wave(baseband_sig, 64, 2)
    >>> plot(timestamps, wave)
    xmin: 0
    xmax: 0.98
    ymin: 0
    ymax: 1.0
    ~████████o███████████████████████████████████████████████████████
    ~█████ooo█ooo████████████████████████████████████████████████████
    ~███oo███████oo██████████████████████████████████████████████████
    ~█oo███████████oo████████████████████████████████████████████████
    ~o███████████████o███████████████oooooooooooooooooooooooooooooooo
    ~█████████████████oo███████████oo████████████████████████████████
    ~███████████████████oo███████oo██████████████████████████████████
    ~█████████████████████ooooooo████████████████████████████████████
    """
    timestamps, wave = makeRealWave_numsamps(len(baseband_sig), samp_rate, freq, allowAliasing)
    mult = np.float32(baseband_sig) * wave
    assert len(timestamps) == len(mult) == len(baseband_sig)
    assert timestamps.dtype == np.float64
    assert mult.dtype == np.float32
    return timestamps, mult


def random_normal(size: int, dtype=np.float32, seed=None) -> np.ndarray:
    """A wrapper of numpy's `standard_normal()` function;
    returns a numpy array of length `size` containing normally distributed.

    `seed` is optional, and mostly just used for testing the function.
    
    TODO >>> random_normal(size=3, seed=0)
    array([ 1.117622 , -1.3871249, -0.4265716], dtype=float32)

    TODO >>> random_normal(size=2, dtype=np.float64, seed=0)
    array([ 0.12573022, -0.13210486])
    """
    rng = np.random.default_rng(seed=seed)
    if dtype == np.complex64:
        re = rng.standard_normal(size=size, dtype=np.float32)
        im = 1j * rng.standard_normal(size=size, dtype=np.float32)
        result = re + im
    assert isinstance(result, np.ndarray)
    assert len(result) == size
    assert result.dtype == dtype
    return result


def noisify(data: np.ndarray, amplitude=1, seed=None) -> np.ndarray:
    """
    Returns a copy of `data` with random normally distributed noise added.
    `seed` is optional, and mostly just used for testing the function.

    TODO >>> dat = np.array([10, 100, 1000], dtype=np.float32)
    TODO >>> noisify(dat, amplitude=0.1, seed=0)
    array([ 11.117622,  98.61288 , 999.5734  ], dtype=float32)

    TODO >>> dat = np.array([10 + 20j, 100 + 200j], dtype=np.complex64)
    TODO >>> noisify(dat, amplitude=0.1, seed=0)
    array([11.117622 +21.117622j, 98.61288 +198.61287j ], dtype=complex64)
    """
    if data.dtype == np.float32:
        randnoise = random_normal(len(data), dtype=np.float32, seed=seed)
    elif data.dtype == np.complex64:
        randnoisereal = np.complex64(random_normal(len(data), dtype=np.float32, seed=seed))
        randnoiseimag = np.complex64(random_normal(len(data), dtype=np.float32, seed=seed))
        randnoise = randnoisereal + (1j * randnoiseimag)
    else:
        raise NotImplementedError("Currently, this only works for these dtypes: float32, complex64.")
    assert randnoise.dtype == data.dtype
    result = data + randnoise
    assert result.dtype == data.dtype
    return result


def generate_ook_modulated_example_data(noise: bool = False, message_delay: bool = False, text_source: Optional[str] = None) -> np.ndarray:
    """
    Generate a file with the given `output_filename`.

    if `noise` is True, random noise will be added to the generated signal.
    if `message_delay` is True, there will be a pause before the meaningful data starts.
    if `text_source` is any string, a random sentence from it will be used as the message.
    
    Example usage:

    text_content = "These are some words, and more words. There are many words in a row in these sentences."
    generate_ook_modulated_example_data(text_source=text_content)
    """
    message = "This is an example message."
    if text_source == None:
        print(f"No text source file specified, so all generated files will contain the message '{message}'")
    else:
        sentences = text_source.split(".")
        message = random.choice(sentences) + "."
        
        
    samp_rate = random.randrange(100, 700, 100)
    bit_length = random.randrange(50, 3000, 10)
    freq = random.randrange(10, samp_rate // 5)
    
    bits = str_to_bin_list(message)
    baseband_sig = ook_modulate(bits, bit_length)
    timestamps, fully_modded = multiply_by_complex_wave(baseband_sig, samp_rate, freq)
    if message_delay:
        fully_modded = np.concatenate([
            np.zeros(random.randint(100, 1500), dtype=np.complex64),
            fully_modded
        ])
    if noise:
        fully_modded = noisify(fully_modded)
    
    assert fully_modded.dtype == np.complex64
    return fully_modded


def generate_ook_modulated_example_file(output_filename: str, noise: bool = False, message_delay: bool = False, text_source: Optional[str] = None):
    """
    Generate a file with the given `output_filename`.

    if `noise` is True, random noise will be added to the generated signal.
    if `message_delay` is True, there will be a pause before the meaningful data starts.
    if `text_source` is any string, a random sentence from it will be used as the message.
    
    Example usage:

    text_content = "These are some words, and more words. There are many words in a row in these sentences."
    generate_ook_modulated_example_file("generated_example_file.complex", text_source=text_content)
    """
    
    data = generate_ook_modulated_example_data(noise, message_delay, text_source)
    data.tofile(output_filename)


def make_fft_positive_freqs_only(sig: np.ndarray, samp_rate: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes an fft, returns only the positive frequencies.
    Return value is a tuple: (sample_freqs, fft_mag).
    `sample_freqs` ranges from 0 to approximately samp_rate/2

    >>> from pcdr.basictermplot import plot
    >>> from pcdr.wavegen import makeWave, make_fft_positive_freqs_only
    >>> samp_rate = 50
    >>> timestamps, wave = makeWave(samp_rate, 5, "complex", seconds=2)
    >>> sample_freqs, fft_mag = make_fft_positive_freqs_only(wave, samp_rate)
    >>> plot(sample_freqs, fft_mag, youtputsize=4)
    xmin: 0
    xmax: 24.5
    ymin: 0
    ymax: 53.54
    ~██████████o███████████████████████████████████████
    ~██████████████████████████████████████████████████
    ~█████████o█o██████████████████████████████████████
    ~ooooooooo███oooooooooooooooooooooooooooooooooooooo
    """
    sample_freqs, fft_mag = make_fft(sig, samp_rate)
    halfway = len(sample_freqs) // 2
    return sample_freqs[halfway:], fft_mag[halfway:]


def make_fft(sig: np.ndarray, samp_rate: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns a tuple of (sample_freqs, fft_mag).
    `sample_freqs` ranges from approximately `-samp_rate/2` to approximately `samp_rate/2`.

    >>> from pcdr.basictermplot import plot
    >>> from pcdr.wavegen import makeComplexWave_time, make_fft
    >>> timestamps, wave = makeComplexWave_time(1, 50, 10)
    >>> sample_freqs, fft_mag = make_fft(wave, 50)
    >>> plot(sample_freqs, fft_mag)
    xmin: 0
    xmax: 24.0
    ymin: 0
    ymax: 26.54
    ~███████████████████████████████████o██████████████
    ~██████████████████████████████████████████████████
    ~██████████████████████████████████████████████████
    ~██████████████████████████████████████████████████
    ~██████████████████████████████████o█o█████████████
    ~██████████████████████████████████████████████████
    ~██████████████████████████████████████████████████
    ~oooooooooooooooooooooooooooooooooo███ooooooooooooo
    """
    windowed = sig * np.hamming(len(sig))
    fft_result = np.fft.fftshift(np.fft.fft(windowed))
    sample_freqs = np.fft.fftshift(np.fft.fftfreq(len(windowed), 1/samp_rate))
    fft_mag = abs(fft_result)
    return sample_freqs, fft_mag
