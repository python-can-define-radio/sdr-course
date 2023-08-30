import math
import deal
from typing import List, Iterable, TypeVar, Tuple
import pydash
import numpy as np


T = TypeVar('T')


maxSizeAfterRepetition = 100e6
maxSizeErrMessage = f"Either your data or the number of repetitions is too large. Please ensure that the length of the result is no more than {maxSizeAfterRepetition}."

@deal.example(lambda: __repeat_each_item([1, 3], 2) == [1, 1, 3, 3])
@deal.pre(lambda _: 0 <= _.numtimes)
@deal.pre(lambda _: len(_.original) * _.numtimes < maxSizeAfterRepetition, message=maxSizeErrMessage)
@deal.ensure(lambda _: len(_.result) == len(_.original) * _.numtimes)
@deal.has()
def __repeat_each_item(original: List[T], numtimes: int) -> List[T]:
    """Example:
    ```
    original = [1, 0]  
    numtimes = 3  
    result = [1, 1, 1, 0, 0, 0]
    ```
    """
    return pydash.flat_map(original, lambda item: [item] * numtimes)


@deal.pure
def __is_binary(x: int) -> bool:
    return x in [1, 0]




@deal.pre(lambda _: all(map(__is_binary, _.bits)),
          message='`bits` must be of type List[int], and all of those integers must be either 0 or 1. It cannot be a string, such as "1010".')
@deal.pre(lambda _: len(_.bits) * _.bit_length < maxSizeAfterRepetition, message=maxSizeErrMessage)
@deal.pre(lambda _: 0 <= _.bit_length)
@deal.ensure(lambda _: _.result.dtype == _.dtype)
@deal.has()
def ook_modulate(bits: List[int], bit_length: int, dtype=np.uint8) -> np.ndarray:
    return np.array(__repeat_each_item(bits, bit_length), dtype=dtype)


## This import must be here due to circular imports
from pcdr.wavegen import multiply_by_complex_wave


@deal.post(lambda result: result[0].dtype == np.float64)
@deal.post(lambda result: result[1].dtype == np.complex64)
@deal.ensure(lambda _: len(_.result[0]) == len(_.result[1]) == len(_.bits) * _.bit_length)
@deal.pre(lambda _: all(map(__is_binary, _.bits)),
          message='`bits` must be of type List[int], and all of those integers must be either 0 or 1. It cannot be a string, such as "1010".')
@deal.pre(lambda _: 1e-10 < _.samp_rate)  # arbitrarily low number
@deal.pre(lambda _: -1e100 < _.freq < 1e100)  # arbitrarily high number that is less than the max float
@deal.pre(lambda _: 0 <= _.bit_length)
@deal.has()
def ook_modulate_at_frequency(bits: List[int], bit_length: int, samp_rate: float, freq: float) -> Tuple[np.ndarray, np.ndarray]:
    baseband_sig = ook_modulate(bits, bit_length)
    return multiply_by_complex_wave(baseband_sig, samp_rate, freq)
