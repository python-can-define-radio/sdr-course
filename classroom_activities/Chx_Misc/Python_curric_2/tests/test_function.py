import time
from gnuradio import gr
from pcdr.function import _QueuedBothEnds
import numpy as np
from tests.test_other__blocks_for_testing import Blk_mult_three



# def test_QueuedBothEnds_1():
#     assert "TODO" == " TODO"
#     qbe = _QueuedBothEnds(Blk_mult_three,
#                 in_dtype=np.uint8,
#                 out_dtype=np.float32, 
#                 in_chunk_size=4,
#                 out_chunk_size=8,
#                 timeout=1)
#     qbe.tb.start()
#     qbe.put(np.array([258,3,10,20]))
#     qbe.put(np.array([50,30,100, 150]))
#     qbe.put(np.array([51,9999,10,20]))
#     qbe.put(np.array([50,30,100, 150]))
#     qbe.put(np.array([5,3,10,20]))
#     qbe.put(np.array([50,30,100, 150]))
#     assert str(qbe.get()) == "[  6.   9.  30.  60. 150.  90. 300. 450.]"
#     assert str(qbe.get()) == "[153.  45.  30.  60. 150.  90. 300. 450.]"
#     assert str(qbe.get()) == "[ 15.   9.  30.  60. 150.  90. 300. 450.]"
#     qbe.tb.wait()


# def test_QueuedBothEnds_proc_func():
#     assert "TODO" == " TODO"
#     qbe = _QueuedBothEnds(Blk_mult_three,
#                 in_dtype=np.uint8,
#                 out_dtype=np.float32, 
#                 in_chunk_size=8,
#                 out_chunk_size=8,
#                 timeout=1)
#     qbe.tb.start()
#     multiplied = qbe.proc(np.array([1, 3, 2, 10, 3, 22, 4, 5]))
#     assert (multiplied == np.array([3, 9, 6, 30, 9, 66, 12, 15], dtype=np.float32)).all()
#     qbe.tb.wait()
