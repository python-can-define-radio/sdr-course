from __future__ import annotations
import deal
from queue import SimpleQueue, Empty
from typing import List, TypeVar



T = TypeVar('T')


@deal.pure
def queue_to_list(q: SimpleQueue[T]) -> List[T]:
    retval = []
    while True:
        try:
            retval.append(q.get_nowait())
        except Empty:
            return retval


@deal.example(lambda _: str_to_bin_list("C") == [0, 1, 1, 0, 0, 1, 0, 1])
def str_to_bin_list(message: str):
    bitstrs = [f"{ord(x):08b}" for x in message]
    joined = "".join(bitstrs)
    return list(map(int, joined))
