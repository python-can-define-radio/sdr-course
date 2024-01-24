from gnuradio import gr, blocks
from osmosdr import source as osmo_source
from pcdr.our_GR_blocks import Blk_strength_at_freq
import time
from typing import Union
from typeguard import typechecked
from pcdr.helpers import validate_hack_rf_receive



class OsmosdrReceiver:
    """A simplified interface to the Osmosdr Source
    which measures the strength of only the specified frequency.
    Example usage:
    
    ```python3
    import pcdr.simple
    receiver = pcdr.simple.OsmosdrReceiver("hackrf", 0, 103.9e6)
    strength = receiver.get_cf_strength()
    print(strength)
    ```
    """
    @typechecked
    def __init__(self, device_name: str, freq: float, *, device_id: Union[int, str] = 0):
        """
        `device_name`: One of the supported osmocom devices, such as "hackrf", "bladerf", etc. See the osmocom docs for a full list.
        `freq`: The frequency which the device will tune to. See note on `set_freq` for more info.
        `device_id`: A zero-based index ("0", "1", etc), or the partial serial number of the device, which can be gotten from GQRX
        >>> 
        """
        self.tb = gr.top_block()
        self.freq_offset = 20e3
        self.samp_rate = 2e6
        self.fft_size = 1024
        if_gain = 32
        bb_gain = 40
        ### TODO: DEBUG
        device_name = "hackrf"
        device_id = 0
        device_args = f"{device_name}={device_id}"
        validate_hack_rf_receive(device_name, self.samp_rate, freq, if_gain, bb_gain)
        self.osmo_source = osmo_source(args=device_args)
        self.osmo_source.set_sample_rate(self.samp_rate)
        self.osmo_source.set_center_freq(freq - self.freq_offset)
        self.osmo_source.set_gain(0)
        self.osmo_source.set_if_gain(if_gain)
        self.osmo_source.set_bb_gain(bb_gain)
        self.stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, self.fft_size)
        self.streng = Blk_strength_at_freq(self.samp_rate, self.freq_offset, self.fft_size, 10)
        self.tb.connect(self.osmo_source, self.stream_to_vec, self.streng)
        self.tb.start()


    @typechecked
    def get_strength(self) -> float:
        """Get the signal strength at the current frequency.
        The frequency is specified when the `OsmosdrReceiver` is created,
        and can be changed using `set_freq`."""
        ## TODO: Fix this sleep with the queue implementation.
        time.sleep(0.01)
        return self.streng.latest_reading
        # while True:
        #     try:
        #         return self.streng._deq.pop()
        #     except IndexError:
        #         time.sleep(100e-6)
    
    @typechecked
    def set_freq(self, freq: float):
        """
        Set the frequency of the receiver.
        
        Implementation detail: Those who are familiar with SDRs may wonder how
        this avoids the "DC spike". `set_freq` actually tunes below the specified
        frequency (20 kHz below at time of writing). Then, when `get_strength` is run,
        the receiver checks for activity at the expected location (the `freq` specified in this function).
        As a result, the strength level returned by `get_strength` is that of the desired frequency.
        """
        validate_hack_rf_receive("hackrf", center_freq=freq)
        # Also, TODO:
        #   Tell the queue work function to consume the entire input_items so that
        #   any data after that is fresh, THEN clear the current get_cf_strength() reading (which
        #   will presumably be using a deque object).
        return self.osmo_source.set_center_freq(freq - self.freq_offset)

    @typechecked
    def set_if_gain(self, if_gain: float):
        validate_hack_rf_receive("hackrf", if_gain=if_gain)
        self.osmo_source.set_if_gain(if_gain)

    @typechecked
    def set_bb_gain(self, bb_gain: float):
        validate_hack_rf_receive("hackrf", bb_gain=bb_gain)
        self.osmo_source.set_bb_gain(bb_gain)
