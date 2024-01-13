from gnuradio import gr
from osmosdr import source as osmo_source


class OsmosdrReceiver:
    def __init__(self):
        self.osmo_source = osmo_source()
        ## TODO
        # osmosdr.source(
        #     args="numchan=" + str(1) + " " + ""
        # )
        # self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        # self.osmosdr_source_0.set_sample_rate(samp_rate)
        # self.osmosdr_source_0.set_center_freq(100e6, 0)
        # self.osmosdr_source_0.set_freq_corr(0, 0)
        # self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        # self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        # self.osmosdr_source_0.set_gain_mode(False, 0)
        # self.osmosdr_source_0.set_gain(10, 0)
        # self.osmosdr_source_0.set_if_gain(20, 0)
        # self.osmosdr_source_0.set_bb_gain(20, 0)
        # self.osmosdr_source_0.set_antenna('', 0)
        # self.osmosdr_source_0.set_bandwidth(0, 0)
