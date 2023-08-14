from __future__ import annotations
import deal
from typing import List, Iterable, TypeVar
import pydash
import numpy as np


T = TypeVar('T')


@deal.example(lambda: __repeat_each_item([1, 3], 2) == [1, 1, 3, 3])
@deal.pre(lambda _: _.numtimes >= 0)
@deal.ensure(lambda _: len(_.result) == len(_.original) * len(_.numtimes))
@deal.has()
def __repeat_each_item(original: Iterable[T], numtimes: int) -> List[T]:
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


@deal.pre(lambda _: all(map(__is_binary, _.data)), message="ook_modulate expects `data` to only contain 0 and 1")
@deal.ensure(lambda _: _.result.dtype == _.dtype)
@deal.has()
def ook_modulate(data: Iterable[int], bit_length: int, dtype=np.uint8) -> np.ndarray:
    return np.array(__repeat_each_item(data, bit_length), dtype=dtype)
