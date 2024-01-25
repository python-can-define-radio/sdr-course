from typing import List, Iterable, TypeVar, Tuple
import numpy as np


T = TypeVar('T')



def __repeat_each_item(original: List[T], numtimes: int) -> List[T]:
    """
    Example:
    >>> __repeat_each_item([2, 5], 3)
    [2, 2, 2, 5, 5, 5]
    """
    assert 0 <= numtimes

    result = []
    for item in original:
        result += [item] * numtimes

    assert len(result) == len(original) * numtimes
    return result



class NonBitError(ValueError):
    pass



def __must_be_binary(bits: List[int]) -> None:
    """
    This returns None:
    >>> __must_be_binary([1, 0, 1])

    This raises:
    >>> __must_be_binary("101")
    Traceback (most recent call last):
        ...
    pcdr.modulators.NonBitError: ...
    """
    if not all(map(lambda x: x in [1, 0], bits)):
        raise NonBitError('`bits` must be of type List[int], and all of those integers'
                         ' must be either 0 or 1. It cannot be a string, such as "1010".')


def ook_modulate(bits: List[int], bit_length: int, dtype=np.uint8) -> np.ndarray:
    """
    OOK Modulate. This is equivalent to simply repeating the bits, that is,
    >>> ook_modulate([1, 0], 3)
    array([1, 1, 1, 0, 0, 0], dtype=uint8)

    It also converts the data to a numpy array.

    Modulating it onto a carrier wave is unnecessary, as transmitting this
    to a GNU Radio osmocom sink will upconvert to the SDR peripheral's carrier frequency.

    If you want your OOK modulation to have a frequency at baseband before 
    hardware upconversion, use the function `ook_modulate_at_frequency`.
    """ 
    __must_be_binary(bits)
    result = np.array(__repeat_each_item(bits, bit_length), dtype=dtype)
    assert result.dtype == dtype
    return result


def ook_modulate_at_frequency(bits: List[int], bit_length: int, samp_rate: float, freq: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    OOK Modulate at a given frequency. Returns the timestamps and the modulated data.

    Examples:
    >>> from pcdr.basictermplot import plot
    >>> timestamps, data = ook_modulate_at_frequency([1, 0, 1, 1], bit_length=20, samp_rate=40, freq=2)
    >>> plot(timestamps, data.real, 80, 10)
    xmin: 0.00
    xmax: 1.98
    ymin: -1.00
    ymax: 1.00
    ~o███████████████████████████████████████o███████████████████o███████████████████
    ~█oo███████████████oo█████████████████████oo███████████████oo█oo███████████████oo
    ~███o█████████████o█████████████████████████o█████████████o█████o█████████████o██
    ~████████████████████████████████████████████████████████████████████████████████
    ~████o███████████o███████████████████████████o███████████o███████o███████████o███
    ~█████o█████████o████oooooooooooooooooooo█████o█████████o█████████o█████████o████
    ~██████o███████o███████████████████████████████o███████o███████████o███████o█████
    ~████████████████████████████████████████████████████████████████████████████████
    ~███████o█████o█████████████████████████████████o█████o█████████████o█████o██████
    ~████████ooooo███████████████████████████████████ooooo███████████████ooooo███████
    """
    __must_be_binary(bits)
    ## TODO: place this import better.
    ## For now, this import must be here due to circular imports
    from pcdr.wavegen import multiply_by_complex_wave

    baseband_sig = ook_modulate(bits, bit_length)
    result = multiply_by_complex_wave(baseband_sig, samp_rate, freq)
    assert result[0].dtype == np.float64
    assert result[1].dtype == np.complex64
    assert len(result[0]) == len(result[1]) == (len(bits) * bit_length)
    return result


