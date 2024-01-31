from pcdr.simple import OsmosdrReceiver
from unittest.mock import patch
import time
from typeguard import typechecked
from tests.test_other__blocks_for_testing import Blk_fake_osmosdr_source



def fake_val_hack_rf_rec(*args, **kwargs):
    """A function that does nothing; current usage is to replace the device parameter validation function."""
    pass
   

def test_OsmosdrReceiver_tuned_on_activity():
    freq_offset = 20e3
    freq_activity = 200e3
    apparent_tune_freq = freq_activity
    behind_the_scenes_tune_freq = apparent_tune_freq - freq_offset
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return Blk_fake_osmosdr_source(2e6, behind_the_scenes_tune_freq)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        with patch("pcdr.simple.validate_hack_rf_receive", fake_val_hack_rf_rec):
            receiver = OsmosdrReceiver("hackrf", freq=apparent_tune_freq)
            assert receiver.get_strength() > 650
            receiver.tb.stop()
            receiver.tb.wait()


def test_OsmosdrReceiver_tuned_off_activity():
    freq_offset = 20e3
    apparent_tune_freq = 400e3  # arbitrary number far from the activity, which is 200e3
    behind_the_scenes_tune_freq = apparent_tune_freq - freq_offset
    def fake_osmo(args: str):
        assert args == "hackrf=0"
        return Blk_fake_osmosdr_source(2e6, behind_the_scenes_tune_freq)
    with patch("pcdr.simple.osmo_source", fake_osmo):
        with patch("pcdr.simple.validate_hack_rf_receive", fake_val_hack_rf_rec):
            receiver = OsmosdrReceiver("hackrf", freq=apparent_tune_freq)
            assert receiver.get_strength() < 10
            receiver.tb.stop()
            receiver.tb.wait()
