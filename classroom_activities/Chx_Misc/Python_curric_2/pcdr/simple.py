from gnuradio import gr, blocks
from osmosdr import source as osmo_source
from pcdr.our_GR_blocks import Blk_strength_at_freq
from pcdr import configure_graceful_exit
import time
from typing import Union
from typeguard import typechecked
from pcdr.helpers import (
    HackRFArgs_RX, OsmocomArgs_RX, get_OsmocomArgs_RX,
    configureOsmocom, create_top_block_and_configure_exit,
    Startable, StopAndWaitable, IFGainSettable,
    BBGainSettable
)



class OsmosdrReceiver(Startable, StopAndWaitable, IFGainSettable, BBGainSettable):
    """A simplified interface to the Osmosdr Source
    which measures the strength of only the specified frequency.
    Example usage:
    
    ```python3
    import pcdr.simple
    receiver = pcdr.simple.OsmosdrReceiver("hackrf", 103.9e6)
    strength = receiver.get_strength()
    print(strength)
    ```
    """
    @typechecked
    def __init__(self, device_args: str, freq: float):
        """
        `device_args`: For example, "hackrf=0", etc. See the osmocom docs for a full list.
        `freq`: The frequency which the device will tune to. See note on `set_freq` for more info.
        >>> 
        """
        self._tb = create_top_block_and_configure_exit()
        self.__freq_offset = 20e3
        true_freq = freq - self.__freq_offset
        self._osmoargs = get_OsmocomArgs_RX(true_freq, device_args)
        self._osmo = configureOsmocom(osmo_source, self._osmoargs)
        fft_size = 1024        
        self.__stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, fft_size)
        self.__streng = Blk_strength_at_freq(self._osmoargs.samp_rate, self.__freq_offset, fft_size)
        self._tb.connect(self._osmo, self.__stream_to_vec, self.__streng)
        
    @typechecked
    def get_strength(self, block: bool = True, timeout: float = 2.0) -> float:
        """Get the signal strength at the current frequency.
        The frequency is specified when the `OsmosdrReceiver` is created,
        and can be changed using `set_freq`.
        """
        return self.__streng._reading.get(block, timeout)
    
    @typechecked
    def set_freq(self, freq: float, seconds: float = 0.5):
        """
        Set the frequency of the receiver, then
        wait `seconds` seconds. This delay allows the buffer to fill with data from the newly chosen frequency.
        
        Note: It's possible that a smaller delay would suffice; we chose a number that would safely guarantee a fresh buffer.
        
        Implementation detail: Those who are familiar with SDRs may wonder how
        this avoids the "DC spike". `set_freq` actually tunes below the specified
        frequency (20 kHz below at time of writing). Then, when `get_strength` is run,
        the receiver checks for activity at the expected location (the `freq` specified in this function).
        As a result, the strength level returned by `get_strength` is that of the desired frequency.
        """
        true_freq = freq - self.__freq_offset
        self._osmoargs.center_freq = true_freq
        retval = self._osmo.set_center_freq(true_freq)
        time.sleep(seconds)
        return retval
