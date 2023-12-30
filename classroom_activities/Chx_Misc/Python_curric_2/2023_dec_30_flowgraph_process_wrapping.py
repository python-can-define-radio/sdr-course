from gnuradio import gr, blocks, analog
from flowgraph_test_basic import getSize, Blk_queue_sink, Blk_queue_source, QueuedSource, QueuedSink
import numpy as np
from typeguard import typechecked
from typing import Type



class Blk_mult_three(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self, name='Multiply by three', in_sig=[np.uint8], out_sig=[np.float32])

    def work(self, input_items, output_items):
        output_items[0][0] = 3 * input_items[0][0]
        return 1


class QueuedBothEnds:
    """
    Sets up a top block that does
    queue - vecstream - proc - streamvec - queue.

    See notes on QueuedSource and QueuedSink regarding args.
    """
    def __init__(self, 
                 ProcessBlk, 
                 in_dtype: type, 
                 out_dtype: type, 
                 in_chunk_size: int, 
                 out_chunk_size: int,
                 proc_blk_args: list = []):
        self.__tb = gr.top_block()
        self.__source_q = Blk_queue_source(in_dtype, in_chunk_size)
        self.__vector_to_stream = blocks.vector_to_stream(getSize(in_dtype), in_chunk_size)
        self.__proc = ProcessBlk(*proc_blk_args)
        self.__stream_to_vec = blocks.stream_to_vector(getSize(out_dtype), out_chunk_size)
        self.__sink_q = Blk_queue_sink(out_dtype, out_chunk_size)
        self.__tb.connect(self.__source_q, self.__vector_to_stream, 
                          self.__proc,
                          self.__stream_to_vec, self.__sink_q)
        self.__tb.start()
    
    def put(self, val: np.ndarray):
        return self.__source_q.queue.put(val)

    def get(self) -> np.ndarray:
        return self.__sink_q.queue.get()


def test_QueuedBothEnds():
    qbe = QueuedBothEnds(Blk_mult_three,
                in_dtype=np.uint8,
                out_dtype=np.float32, 
                in_chunk_size=4,
                out_chunk_size=8)
    qbe.put(np.array([258,3,10,20]))
    qbe.put(np.array([50,30,100, 150]))
    qbe.put(np.array([51,9999,10,20]))
    qbe.put(np.array([50,30,100, 150]))
    qbe.put(np.array([5,3,10,20]))
    qbe.put(np.array([50,30,100, 150]))
    assert str(qbe.get()) == "[  6.   9.  30.  60. 150.  90. 300. 450.]"
    assert str(qbe.get()) == "[153.  45.  30.  60. 150.  90. 300. 450.]"
    assert str(qbe.get()) == "[ 15.   9.  30.  60. 150.  90. 300. 450.]"


@typechecked
def functionalize_proc_blk(ProcessBlk, 
                 in_dtype: type, 
                 out_dtype: type, 
                 in_chunk_size: int, 
                 out_chunk_size: int,
                 proc_blk_args: list = []):
    qbe = QueuedBothEnds(ProcessBlk, in_dtype, out_dtype, in_chunk_size, out_chunk_size, proc_blk_args)
    
    def run(chunk: np.ndarray) -> np.ndarray:
        qbe.put(chunk)
        return qbe.get()
    
    return run


def test_functionalize_proc_blk():
    multThree = functionalize_proc_blk(Blk_mult_three, in_dtype=np.uint8, out_dtype=np.float32, in_chunk_size=4, out_chunk_size=4)

    assert str(multThree(np.array([1, 3, 2, 10]))) == "[ 3.  9.  6. 30.]"




if __name__ == "__main__":
    # wav file source -> fm modulate -> file sink
    audio_size = 2**8
    modulated_size = 2**10
    wavsource = QueuedSource(blocks.wavfile_source, np.float32, audio_size, ["testf.wav", False])

    mod = functionalize_proc_blk(analog.wfm_tx, np.float32, np.complex64,
                                 in_chunk_size=audio_size, out_chunk_size=modulated_size,
                                 proc_blk_args=[48_000, 400_000])
    file_sink = QueuedSink(blocks.file_sink, np.complex64, modulated_size, [getSize(np.complex64), "somecomplexfile.complex"])

    file_sink.put(mod(wavsource.get()))

# blocks.file_sink(gr.sizeof_gr_complex*1, '', False)
# self.blocks_file_sink_0.set_unbuffered(False)


# blocks.wavfile_sink(
#     '',
#     1,
#     samp_rate,
#     blocks.FORMAT_WAV,
#     blocks.FORMAT_PCM_16,
#     False
#     )

#     analog.wfm_rcv(
# 	quad_rate=,
# 	audio_decimation=,
# )