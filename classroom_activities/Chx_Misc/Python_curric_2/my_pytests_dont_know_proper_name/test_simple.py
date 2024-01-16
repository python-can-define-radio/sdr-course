from pcdr.simple import OsmosdrReceiver
from unittest.mock import patch
from gnuradio import analog
import time


class fake_osmosdr_source(analog.sig_source_c):
    def __init__(self, fake_samp_rate: float, fake_activity_freq: float, fake_center_freq: float):
        """Note that the actual osmocom does not have samp_rate in its constructor."""
        self.fake_samp_rate = fake_samp_rate
        self.fake_center_freq = fake_center_freq
        analog.sig_source_c.__init__(
            self, fake_samp_rate, analog.GR_COS_WAVE, 
            fake_activity_freq - fake_center_freq,
            1)
    
    def set_sample_rate(self, samp_rate: float):
        assert self.fake_samp_rate == samp_rate

    def set_center_freq(self, center_freq: float):
        assert self.fake_center_freq == center_freq

    def set_if_gain(self, if_gain: int):
        pass

    def set_bb_gain(self, bb_gain: int):
        pass


def test_OsmosdrReceiver_tuned_on_activity():
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return fake_osmosdr_source(2e6, 200_000, 180_000)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        receiver = OsmosdrReceiver(200_000)
        time.sleep(0.5)
        assert receiver.get_cf_strength() > 650
        receiver.tb.stop()
        receiver.tb.wait()


def test_OsmosdrReceiver_tuned_off_activity():
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return fake_osmosdr_source(2e6, 600_000, 180_000)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        receiver = OsmosdrReceiver(200_000)
        time.sleep(0.5)
        assert receiver.get_cf_strength() < 10
        receiver.tb.stop()
        receiver.tb.wait()


def test_OsmosdrReceiver_scan():
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return fake_osmosdr_source(2e6, 600_000, 180_000)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        receiver = OsmosdrReceiver(200_000)
        time.sleep(0.5)
        assert receiver.get_cf_strength() < 10
        receiver.tb.stop()
        receiver.tb.wait()
