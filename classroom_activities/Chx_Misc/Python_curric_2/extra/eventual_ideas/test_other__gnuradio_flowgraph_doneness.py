from pcdr._internal.our_GR_blocks import Blk_queue_source, Blk_sink_print
from gnuradio import gr, blocks
import time
import numpy as np
from unittest.mock import patch
from io import StringIO
from .test_function import Blk_mult_three


# class Test_Queue_Source:
#     def test_queue_source_stops_based_on_timeout(self):
#         assert "TODO" == " TODO"
#         queue_timeout = 1.5
#         sleep_time = 0.5
#         tb = gr.top_block()
#         queue_source = Blk_queue_source(np.uint8, 1024, timeout=queue_timeout)
#         vec_to_stream = blocks.vector_to_stream(gr.sizeof_char, 1024)
#         mult3 = Blk_mult_three()
#         printsink = Blk_sink_print()
#         tb.connect(queue_source, vec_to_stream, mult3, printsink)
#         tb.start()
#         startTime = time.perf_counter()
#         time.sleep(sleep_time)
#         tb.stop()
#         trying_to_stop = time.perf_counter() - startTime
#         tb.wait()
#         done_waiting = time.perf_counter() - startTime
#         assert abs(trying_to_stop - sleep_time) < 0.1
#         assert abs(done_waiting - queue_timeout) < 0.1


#     @patch('sys.stdout', new_callable=StringIO)
#     def test_wait(self, output: StringIO):
#         assert "TODO" == " TODO"
#         tb = gr.top_block()
#         queue_source = Blk_queue_source(np.uint8, 4, timeout=1)
#         vec_to_stream = blocks.vector_to_stream(gr.sizeof_char, 4)
#         mult3 = Blk_mult_three()
#         printsink = Blk_sink_print()
#         tb.connect(queue_source, vec_to_stream, mult3, printsink)
#         tb.start()
#         queue_source.queue.put(np.array([3, 6, 2, 5], dtype=np.uint8))
#         tb.wait()
#         outlines = output.getvalue().splitlines()
#         assert outlines[0] == "9.0"
#         assert outlines[1] == "18.0"
#         assert outlines[2] == "6.0"
#         assert outlines[3] == "15.0"
#         assert outlines[4] == "Queue is empty, block will now report 'done' to GNU Radio flowgraph"
        

#     @patch('sys.stdout', new_callable=StringIO)
#     def test_flowgraph_completes_processing_after_source_block_marks_done(self, output: StringIO):
#         assert "TODO" == " TODO"
#         tb = gr.top_block()
#         queue_source = Blk_queue_source(np.uint8, 4, timeout=1)
#         vec_to_stream = blocks.vector_to_stream(gr.sizeof_char, 4)
#         mult3 = Blk_mult_three()
#         printsink = Blk_sink_print(sleep_seconds=0.2)
#         tb.connect(queue_source, vec_to_stream, mult3, printsink)
#         tb.start()
#         queue_source.queue.put(np.array([3, 6, 2, 5], dtype=np.uint8))
#         queue_source.queue.put(np.array([30, 60, 20, 50], dtype=np.uint8))
#         tb.wait()
#         outlines = output.getvalue().splitlines()
#         queue_empty_msg = "Queue is empty, block will now report 'done' to GNU Radio flowgraph"
#         ## Queue empty message is in the output, but isn't first or last
#         assert queue_empty_msg in outlines
#         assert outlines[0] != queue_empty_msg
#         assert outlines[-1] != queue_empty_msg
#         outcopy = outlines.copy()
#         outcopy.remove(queue_empty_msg)
#         assert outcopy == ["9.0", "18.0", "6.0", "15.0", "90.0", "180.0", "60.0", "150.0"]
