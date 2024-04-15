from typing import Optional, Union, Literal
from pathlib import Path
from gnuradio import gr, blocks, analog, audio, filter
import osmosdr
import numpy as np
from pcdr._internal.our_GR_blocks import (
    Blk_strength_at_freq, Blk_VecSingleItemStack
)
import time
from typeguard import typechecked
from pcdr._internal.misc import (
    get_OsmocomArgs_RX, get_OsmocomArgs_TX, 
    configureOsmocom, create_top_block_and_configure_exit,
    connect_probe_common,
    Startable, StopAndWaitable, Waitable, IFGainSettable,
    BBGainSettable, CenterFrequencySettable, ProbeReadable
)
from pcdr._internal.types_and_contracts import HasWorkFunc



class OsmosdrSingleFreqReceiver(Startable, StopAndWaitable, IFGainSettable, BBGainSettable):
    """A simplified interface to the Osmosdr Source
    which measures the strength of only the specified frequency.
    Example usage:
    
    ```python3
    import pcdr.simple
    receiver = pcdr.simple.OsmosdrReceiver("hackrf=0", 103.9e6)
    recevier.start()
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
        self._osmo = configureOsmocom(osmosdr.source, self._osmoargs)
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


class OsmosdrSingleFreqTransmitter(Startable, StopAndWaitable,
                         IFGainSettable, BBGainSettable,
                         CenterFrequencySettable):
    """A simplified interface to the Osmosdr Sink
    which transmits a pure sine wave on the specified frequency.
    
    Example usage:
    
    ```python3
    import pcdr.simple
    import time
    transmitter = pcdr.simple.OsmosdrTransmitter("hackrf=0", 2.45e9)
    transmitter.start()
    transmitter.set_if_gain(37)
    time.sleep(1)
    transmitter.set_center_freq(2.4501e9)
    time.sleep(1)
    transmitter.set_center_freq(2.4502e9)
    time.sleep(1)
    transmitter.set_if_gain(0)
    time.sleep(1)
    transmitter.set_if_gain(37)
    time.sleep(1)
    transmitter.stop_and_wait()
    ```
    """
    @typechecked
    def __init__(self, device_args: str, freq: float):
        """
        `device_args`: For example, "hackrf=0", etc. See the osmocom docs for a full list.
        `freq`: The frequency which the device will tune to.
        >>> 
        """
        self._tb = create_top_block_and_configure_exit()
        self._osmoargs = get_OsmocomArgs_TX(freq, device_args)
        self.__constant_source = analog.sig_source_c(self._osmoargs.samp_rate, analog.GR_CONST_WAVE, 0, 0, 3)
        self._osmo = configureOsmocom(osmosdr.sink, self._osmoargs)
        self._tb.connect(self.__constant_source, self._osmo)

    @typechecked
    def set_freq(self, freq: float) -> float:
        """Equivalent to `self.set_center_freq(freq)`, for backwards compatibility."""
        return self.set_center_freq(freq)


@typechecked
def _pick_audio_source(audio_device: Optional[str],
                      wavfile: Optional[Union[str, Path]],
                      audio_sample_rate: float,
                      repeat: bool) -> Union[audio.source, blocks.wavfile_source]:
    """
    >>> _pick_audio_source("", None, 48000, False)
    <gnuradio.audio...>
    """
    if audio_device != None and wavfile != None:
        raise ValueError("You must specify either `wavfile` or `device`, not both")
    elif audio_device != None:
        return audio.source(audio_sample_rate, audio_device, ok_to_block=True)
    elif wavfile != None:
        return blocks.wavfile_source(wavfile, repeat)
    else:
        raise ValueError("You must specify either `wavfile` or `device`")


class AudioPlayer(Startable, StopAndWaitable, Waitable, ProbeReadable):
    @typechecked
    def __init__(self, *,
                 wavfile: Optional[Union[str, Path]] = None,
                 audio_sample_rate: float = 48e3,
                 repeat: bool = False):
        """
        Plays the audio locally (not using the SDR hardware). Useful for testing that your wav file is working.

        `wavfile`: The path to a wav file that will be played.
        """
        self._tb = create_top_block_and_configure_exit()
        self.__source = blocks.wavfile_source(wavfile, repeat)
        self.__sink = audio.sink(audio_sample_rate, device_name="", ok_to_block=True)
        self._tb.connect(self.__source, self.__sink)
        self._probe: Optional[Blk_VecSingleItemStack] = None
    
    @typechecked
    def connect_probe(self, *,
                      location: Literal["wavfile_source", "audio_sink"],
                      vecsize: int):
        if location == "wavfile_source":
            src_blk = self.__source
            type_ = np.float32
        elif location == "audio_sink":
            # this is the feeder block for the audio sink
            src_blk = self.__source  
            type_ = np.float32
        self._probe = connect_probe_common(self._tb, src_blk, type_, vecsize)


class OsmosdrWBFMTransmitter(Startable, StopAndWaitable, CenterFrequencySettable,
                             IFGainSettable, BBGainSettable, Waitable):
    """
    ```python3
    import pcdr.simple
    import time
    transmitter = pcdr.simple.OsmosdrWBFMTransmitter("hackrf=0", 2.45e9, "pulse_monitor")
    transmitter.start()
    transmitter.set_if_gain(37)
    time.sleep(10)
    transmitter.stop_and_wait()
    ```
    """
    @typechecked
    def __init__(self, device_args: str, freq: float, *,
                 audio_device: Optional[str] = None,
                 wavfile: Optional[Union[str, Path]] = None,
                 audio_sample_rate: float = 48e3,
                 repeat: bool = False):
        """        
        Parameters
        ----------
        device_args :
            For example, "hackrf=0", etc. See the osmocom docs for a full list.
        freq :
            The frequency which the device will tune to in Hz.
        audio_device : 
            - if you want to use the microphone, set to `""`
            - "pulse_monitor" to use whatever is currently playing on the computer. The "pulse_monitor" option currently only works on GNU Linux, and only after pre-configuring the ALSA Pseudodevice according to the GNU Radio docs: https://wiki.gnuradio.org/index.php?title=ALSAPulseAudio#Monitoring_the_audio_input_of_your_system_with_PulseAudio
            
            Note: If you specify `audio_device`, then `repeat` is ignored.
        wavfile :
            The path to a wav file that will be played.
        """
        self._tb = create_top_block_and_configure_exit()
        self.__source = _pick_audio_source(audio_device, wavfile, audio_sample_rate, repeat)
        self._osmoargs = get_OsmocomArgs_TX(freq, device_args)
        self.__rational_resampler = filter.rational_resampler_fff(int(self._osmoargs.samp_rate), int(audio_sample_rate))
        self.__wfm_tx = analog.wfm_tx(self._osmoargs.samp_rate, self._osmoargs.samp_rate)
        self._osmo = configureOsmocom(osmosdr.sink, self._osmoargs)
        self._tb.connect(self.__source, self.__rational_resampler, self.__wfm_tx, self._osmo)
