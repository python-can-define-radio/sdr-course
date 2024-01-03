from gnuradio import gr
from pcdr.function import _QueuedBothEnds, _functionalize_proc_blk
import numpy as np
from .test_other__blocks_for_testing import Blk_mult_three



def test_QueuedBothEnds():
    qbe = _QueuedBothEnds(Blk_mult_three,
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


def test_functionalize_proc_blk():
    multThree = _functionalize_proc_blk(Blk_mult_three, in_dtype=np.uint8, out_dtype=np.float32, in_chunk_size=4, out_chunk_size=4)

    assert multThree(np.array([1, 3, 2, 10])) == np.array([3, 9, 6, 30], dtype=np.float32)
