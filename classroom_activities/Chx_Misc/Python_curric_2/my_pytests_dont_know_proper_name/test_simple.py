from pcdr.simple import OsmosdrReceiver
from unittest.mock import patch
from gnuradio import analog
import time
from typeguard import typechecked



def fake_val_hack_rf_rec(*args):
    pass


@typechecked
def fake_osmosdr_source_factory(fake_samp_rate: float, fake_center_freq: float):
    """Return a block that resembles the osmosdr_source, but always has activity at only 200kHz."""
    fake_activity_freq = 200e3
    analog_sig_source = analog.sig_source_c(
        fake_samp_rate, analog.GR_COS_WAVE, 
        fake_activity_freq - fake_center_freq, 1)

    def set_sample_rate(samp_rate: float):
        assert fake_samp_rate == samp_rate
    analog_sig_source.set_sample_rate = set_sample_rate

    def set_center_freq(center_freq: float):
        assert fake_center_freq == center_freq
    analog_sig_source.set_center_freq = set_center_freq

    analog_sig_source.set_gain = lambda gain: None
    analog_sig_source.set_if_gain = lambda if_gain: None
    analog_sig_source.set_bb_gain = lambda bb_gain: None

    return analog_sig_source
    

def test_OsmosdrReceiver_tuned_on_activity():
    freq_offset = 20e3
    freq_activity = 200e3
    apparent_tune_freq = freq_activity
    behind_the_scenes_tune_freq = apparent_tune_freq - freq_offset
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return fake_osmosdr_source_factory(2e6, behind_the_scenes_tune_freq)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        with patch("pcdr.simple.validate_hack_rf_receive", fake_val_hack_rf_rec):
            receiver = OsmosdrReceiver("hackrf", freq=apparent_tune_freq)
            time.sleep(0.5)
            assert receiver.get_strength() > 650
            receiver.tb.stop()
            receiver.tb.wait()


def test_OsmosdrReceiver_tuned_off_activity():
    freq_offset = 20e3
    apparent_tune_freq = 400e3  # arbitrary number far from the activity, which is 200e3
    behind_the_scenes_tune_freq = apparent_tune_freq - freq_offset
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return fake_osmosdr_source_factory(2e6, behind_the_scenes_tune_freq)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        with patch("pcdr.simple.validate_hack_rf_receive", fake_val_hack_rf_rec):
            receiver = OsmosdrReceiver("hackrf", freq=apparent_tune_freq)
            time.sleep(0.5)
            assert receiver.get_strength() < 10
            receiver.tb.stop()
            receiver.tb.wait()
