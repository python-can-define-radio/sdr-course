from pcdr._beta.gnuradio_sendlike import _gnuradio_write_file
from pcdr import makeComplexWave_time
import numpy as np
import random
from pathlib import Path


def test_write_and_read():
    basepath = Path("temp_dir_for_tests")
    fn = str(basepath / "samprate_2e6_basic_wave.complex")

    len_dat = random.randint(200, 30000)
    dat_to_write = np.complex64(np.random.random(len_dat))
    # timestamps, wave = makeComplexWave_time(2, 1000, 10)
    assert len(dat_to_write) == len_dat
    assert isinstance(dat_to_write, np.ndarray)
    _gnuradio_write_file(dat_to_write, fn)
    
    nploaded = np.fromfile(fn, np.complex64)
    assert len(nploaded) <= len(dat_to_write)
    subset_of_original_that_actually_got_written = dat_to_write[:len(nploaded)]
    assert (nploaded == subset_of_original_that_actually_got_written).all()
    


