import numpy as np
from gnuradio import blocks
from ex_2023_dec_30_flowgraph_test_basic import QueuedSink, getSize


class file_sink(QueuedSink):
    def __init__(self, chunk_size: int, dtype: type, filename: str, append: bool = False, unbuffered: bool = False):
        super().__init__(blocks.file_sink, dtype, chunk_size, [getSize(dtype), filename, append])
        self._sink.set_unbuffered(unbuffered)
