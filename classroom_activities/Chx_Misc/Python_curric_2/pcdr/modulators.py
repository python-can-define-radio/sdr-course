import deal
from typing import List
from typeguard import typechecked
import pydash



@typechecked
@deal.example(lambda: __repeat_each_item([1, 3], 2) == [1, 1, 3, 3])
def __repeat_each_item(original: List[int], numtimes: int) -> List[int]:
    """Example:
    ```
    original = [1, 0]  
    numtimes = 3  
    result = [1, 1, 1, 0, 0, 0]
    ```
    """
    def repeat(item):
        return [item] * numtimes
    return pydash.flat_map(original, repeat)


def __is_binary(x: int) -> bool:
    return x in [1, 0]


@typechecked
@deal.pre(lambda _: all(map(__is_binary, _.data)), message="ook_modulate expects data to be a list of only 0 and 1")
def ook_modulate(data: List[int], bit_length: int) -> List[int]:
    return __repeat_each_item(data, bit_length)