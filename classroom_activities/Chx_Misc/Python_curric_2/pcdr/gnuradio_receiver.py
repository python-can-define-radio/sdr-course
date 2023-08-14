def gnuradio_receive(
        center_freq: float,
        samp_rate: float,
        if_gain: int = 16,
        input_from: str = "hackrf",
        device_args: str = "hackrf=0"
                     ):
    