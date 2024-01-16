from gnuradio import gr, blocks
from osmosdr import source as osmo_source
from pcdr.our_GR_blocks import Blk_strength_at_freq
import time



class OsmosdrReceiver:
    """A simplified interface to the Osmosdr Source
    which measures the strength of only the specified frequency.
    Example usage:
    
    ```python3
    import pcdr.simple
    receiver = pcdr.simple.OsmosdrReceiver(103.9e6)
    strength = receiver.get_cf_strength()
    print(strength)
    ```
    """
    def __init__(self, center_freq: float):
        self.tb = gr.top_block()
        self.freq_offset = 20e3
        samp_rate = 2e6
        fft_size = 1024
        self.osmo_source = osmo_source()
        self.osmo_source.set_sample_rate(samp_rate)
        self.osmo_source.set_center_freq(center_freq - self.freq_offset)
        self.osmo_source.set_if_gain(32)
        self.osmo_source.set_bb_gain(40)
        self.stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
        self.streng = Blk_strength_at_freq(samp_rate, self.freq_offset, fft_size)
        self.tb.connect(self.osmo_source, self.stream_to_vec, self.streng)
        self.tb.start()
        
        ## TODO: this is a temporary fix to ensure the osmocom source has
        ## had time to collect some data.
        ## One possible proper fix is to implement Blk_strength_at_freq.latest_reading
        ## using a LIFO queue that clears every time we fetch from it
        ## (so that it's always the freshest data, but it will block
        ##  if it hasn't received anything since the last fetch).
        time.sleep(0.3)

    def get_cf_strength(self) -> float:
        """Get the center frequency signal strength.
        The center frequency is specified when the `OsmosdrReceiver` is created,
        and can be changed using `set_center_freq`."""
        return self.streng.latest_reading
    
    def set_sample_rate(self, samp_rate: float):
        return self.osmo_source.set_sample_rate(samp_rate)

    def set_center_freq(self, center_freq: float):
        return self.osmo_source.set_center_freq(center_freq - self.freq_offset)
