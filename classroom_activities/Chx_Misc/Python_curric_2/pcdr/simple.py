from gnuradio import gr, blocks
from osmosdr import source as osmo_source
from pcdr.our_GR_blocks import Blk_strength_at_freq
import time
from typing import Union
from typeguard import typechecked



class OsmosdrReceiver:
    """A simplified interface to the Osmosdr Source
    which measures the strength of only the specified frequency.
    Example usage:
    
    ```python3
    import pcdr.simple
    receiver = pcdr.simple.OsmosdrReceiver("hackrf", "0", 103.9e6)
    strength = receiver.get_cf_strength()
    print(strength)
    ```
    """
    def __init__(self, device_name: str, device_id: Union[int, str], center_freq: float):
        """
        `device_name`: One of the supported osmocom devices, such as hackrf, bladerf, etc (see the osmocom docs)
        `device_id`: A zero-based index ("0", "1", etc), or the partial serial number of the device, which can be gotten from GQRX

        >>> 
        """
        self.tb = gr.top_block()
        self.freq_offset = 20e3
        self.samp_rate = 2e6
        self.fft_size = 1024
        device_args = f"{device_name}={device_id}"
        self.osmo_source = osmo_source(args=device_args)
        self.osmo_source.set_sample_rate(self.samp_rate)
        self.osmo_source.set_center_freq(center_freq - self.freq_offset)
        self.osmo_source.set_if_gain(32)
        self.osmo_source.set_bb_gain(40)
        self.stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, self.fft_size)
        self.streng = Blk_strength_at_freq(self.samp_rate, self.freq_offset, self.fft_size, 10)
        self.tb.connect(self.osmo_source, self.stream_to_vec, self.streng)
        self.tb.start()


    @typechecked
    def get_cf_strength(self) -> float:
        """Get the center frequency signal strength.
        The center frequency is specified when the `OsmosdrReceiver` is created,
        and can be changed using `set_center_freq`."""
        ## TODO: Fix this sleep with the queue implementation.
        time.sleep(0.01)
        return self.streng.latest_reading
        # while True:
        #     try:
        #         return self.streng._deq.pop()
        #     except IndexError:
        #         time.sleep(100e-6)
    

    def set_sample_rate(self, samp_rate: float):
        # TODO: Validate samp rate within range
        return self.osmo_source.set_sample_rate(samp_rate)

    def set_center_freq(self, center_freq: float):
        # TODO: Validate freq within range
        # Also, TODO:
        #   Tell the queue work function to consume the entire input_items so that
        #   any data after that is fresh, THEN clear the current get_cf_strength() reading (which
        #   will presumably be using a deque object).
        return self.osmo_source.set_center_freq(center_freq - self.freq_offset)

    def set_if_gain(self, TODO):
        TODO

    def set_bb_gain(self, TODO):
        TODO
        

class HackRFReceiver(OsmosdrReceiver):
    def __init__(self, device_id: Union[int, str]):
        OsmosdrReceiver.__init__(self, "hackrf", device_id, center_freq)
