from pcdr.simple import OsmosdrReceiver
from unittest.mock import patch
from gnuradio import analog


class fake_osmosdr_source(analog.sig_source_c):
    def __init__(self, fake_samp_rate: float, fake_activity_freq: float):
        """Note that the actual osmocom does not have samp_rate in its constructor."""
        analog.sig_source_c.__init__(
            self, fake_samp_rate, analog.GR_COS_WAVE)
            


@patch("pcdr.simple.osmo_source", fake_osmosdr_source)
def test_OsmosdrReceiver():
    samp_rate = 1000
    receiver = OsmosdrReceiver(samp_rate)
    assert something_about_receiver  ## TODO


