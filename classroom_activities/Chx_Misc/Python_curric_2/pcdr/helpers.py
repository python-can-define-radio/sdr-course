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
