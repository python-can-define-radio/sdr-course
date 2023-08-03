import pydash
import numpy as np
from queue import SimpleQueue
from pcdr.osmocom_queued_tx_flowgraph import queue_to__osmocom_sink
from pcdr.osmocom_queued_tx_flowgraph import queue_to__print_blk
from pcdr.osmocom_queued_tx_flowgraph import queue_to__string_file_sink
from pcdr.osmocom_queued_tx_flowgraph import top_block_manager


class osmocom_ook_sender():
    
    def __init__(self, center_freq, samp_rate, bit_length):
        self.center_freq = center_freq
        self.samp_rate = samp_rate
        self.bit_length = int(bit_length)

    def send(self, data, output_to=None, print_delay=0.5):
        """`output_to` can be one of these:
          - None (default): send to osmocom sink.
          - "PRINT": print to stdout (usually the terminal).
          - any other string: interpret `output_to` as a filename. Write output data to that file.

          `print_delay` is only used if printing to stdout.
          """
        acceptable = [1, 0]
        pad_val = 0
        chunk_size = 1024

        ## Validate data
        for num in data:   
            if type(num) != int:
                raise TypeError("Only integers are allowed")
            if num not in acceptable:
                raise ValueError("All data must be binary 1 or 0")

        ## Repeat, so [1, 0] becomes [1, 1, 1, 0, 0, 0] (if bit_length=3)
        repeated_data = [item for item in data for i in range(self.bit_length)]

        ## Pad to next full chunk size, then chunk
        while len(repeated_data)%chunk_size != 0:
            repeated_data.append(pad_val)
        chunked = pydash.chunk(repeated_data, size=chunk_size)

        ## List-of-lists to queue of numpy arrays
        q = SimpleQueue()
        for item in map(np.array, chunked):
            q.put(item)

        
        ## Set up and run flowgraph with the data queue we've prepared above
        if output_to == None:
            tb = queue_to__osmocom_sink(self.center_freq, self.samp_rate, q)
        elif output_to == "PRINT":
            tb = queue_to__print_blk(print_delay=print_delay, external_queue=q)
        else:
            tb = queue_to__string_file_sink(filename=output_to, external_queue=q)
        
        tbm = top_block_manager(tb)

        ## TODO: This is NOT ideal -- would be better to detect done-ness from
        ##  inside the flowgraph if possible, so that I can use .wait() for its
        ## intended purpose.
        waittime = 1.1 * len(repeated_data)/self.samp_rate
        tbm.start_and_keep_open(seconds=waittime)
        
        ##   ## TODO: Do we need this? Or is it taking care of itself?
        ##   tb.stop()
        ##   tb.wait() 

