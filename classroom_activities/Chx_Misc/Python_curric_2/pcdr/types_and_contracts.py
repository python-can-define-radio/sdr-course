from typing import Union, TypeVar, Protocol
from pcdr.our_GR_blocks import queue_sink

from gnuradio import gr
from PyQt5 import Qt



## As per https://stackoverflow.com/questions/43957034/specifying-a-type-to-be-a-list-of-numbers-ints-and-or-floats
TRealNum = TypeVar('TRealNum', int, float)

TRealOrComplexNum = TypeVar('TRealOrComplexNum', int, float, complex)

class SupportsQueueSink(Protocol):
    queue_sink: queue_sink


class top_block_and_widget(gr.top_block, Qt.QWidget):
    pass
