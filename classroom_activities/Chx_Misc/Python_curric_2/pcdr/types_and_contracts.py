from typing import Union, TypeVar, Protocol
import deal
from pcdr.our_GNU_blocks import queue_sink



## As per https://stackoverflow.com/questions/43957034/specifying-a-type-to-be-a-list-of-numbers-ints-and-or-floats
TRealNum = TypeVar('TRealNum', int, float)

TRealOrComplexNum = TypeVar('TRealOrComplexNum', int, float, complex)

class SupportsQueueSink(Protocol):
    queue_sink: queue_sink

