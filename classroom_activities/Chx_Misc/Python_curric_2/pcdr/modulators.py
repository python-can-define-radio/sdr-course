from __future__ import annotations
import deal
from typing import List, Iterable, TypeVar
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


@deal.pre(lambda _: all(map(__is_binary, _.data)),
          message='ook_modulate expects `data` to be of type List[int], and all of those integers must be either 0 or 1. It cannot be a string, such as "1010".')
@deal.pre(lambda _: len(_.data) * _.bit_length < maxSizeAfterRepetition, message=maxSizeErrMessage)
@deal.pre(lambda _: 0 <= _.bit_length)
@deal.ensure(lambda _: _.result.dtype == _.dtype)
@deal.has()
def ook_modulate(data: List[int], bit_length: int, dtype=np.uint8) -> np.ndarray:
    return np.array(__repeat_each_item(data, bit_length), dtype=dtype)
