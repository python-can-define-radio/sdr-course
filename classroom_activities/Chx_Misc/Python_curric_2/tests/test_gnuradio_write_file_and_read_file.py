# """This demonstrates a few functions. We may turn it into an exercise."""
# from pcdr.gnuradio_sender import _gnuradio_write_file
# from pathlib import Path
# import numpy as np


# def FAILED_test_write_and_read():
#     """This didn't ever work, presumably because of incomplete writes due to how gnuradio works.
#     I'm abandoning this approach."""
#     basepath = Path("temp_dir_for_tests")
#     tot_time = 30
#     timestamps, wave = makeComplexWave_time(tot_time, 100, 20)
#     assert len(wave) == 3000
#     assert timestamps[1] == 0.01
#     _gnuradio_write_file(wave, str(basepath / "samprate_2e6_basic_wave.complex"), chunk_size=2)

#     numpyread = np.fromfile(str(basepath / "samprate_2e6_basic_wave.complex"), dtype=np.complex64)
#     assert len(numpyread) == len(wave)

#     loaded = gnuradio_read_file(str(basepath / "samprate_2e6_basic_wave.complex"), chunk_size=2)
#     assert len(loaded) == len(wave)
    
    