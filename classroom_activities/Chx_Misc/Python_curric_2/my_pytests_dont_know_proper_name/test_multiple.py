from queue import SimpleQueue
import numpy as np
import deal
import hypothesis.extra.numpy as hyponp
import hypothesis.strategies as st


from pcdr.gnuradio_sender import pad_chunk_queue
from pcdr.helpers import queue_to_list


def test_pad_chunk_queue_small_chunk():
    testdata = np.array([1, 2, 3], dtype=np.uint8)
    pcq = pad_chunk_queue(testdata, 2)
    nparry = np.array(queue_to_list(pcq))
    should_be = np.array([[1, 2], [3, 0]], dtype=np.complex64)
    assert (nparry == should_be).all()


def test_pad_chunk_queue_padding():
    testdata = np.array([1, 2, 3], dtype=np.uint8)
    pcq = pad_chunk_queue(testdata, 5)
    nparry = np.array(queue_to_list(pcq))
    should_be = np.array([[1, 2, 3, 0, 0]], dtype=np.complex64)
    assert (nparry == should_be).all()


def test_1_queue_to_list():
    assert queue_to_list(SimpleQueue()) == []


from pcdr.wavegen import createTimestamps, makeRealWave, makeComplexWave, isAliasingWhenDisallowed, aliasingValueError, makeComplexWave_numsamps, makeRealWave_numsamps, makeComplexWave_time, makeRealWave_time, multiply_by_complex_wave, multiply_by_real_wave

seconds_strat = st.floats(max_value=100)
num_samples_strat = st.integers(max_value=100)
freq_strat = st.floats(-1e12, 1e12)
timestamps_strat = hyponp.arrays(
            dtype=np.float64,
            shape=1,
            elements=st.floats(-10e9, 10e9)
        )
samp_rate_strat = st.floats(
    1e-9,  # To help with deal tests, the samp_rate must be reasonable (not tiny)
    100
)


test_createTimestamps = deal.cases(
    func=createTimestamps,
    kwargs=dict(
        seconds=seconds_strat,
        num_samples=num_samples_strat
    )
)

test_makeRealWave = deal.cases(
    func=makeRealWave,
    kwargs=dict(
        timestamps=timestamps_strat,
        freq=freq_strat
    )
)

test_makeComplexWave = deal.cases(
    func=makeComplexWave,
    kwargs=dict(
        timestamps=timestamps_strat,
        freq=freq_strat
    )
)

test_isAliasingWhenDisallowed = deal.cases(isAliasingWhenDisallowed)

test_aliasingValueError = deal.cases(aliasingValueError)

test_makeComplexWave_numsamps = deal.cases(
    func=makeComplexWave_numsamps,
    kwargs=dict(
        num_samples=num_samples_strat,
        samp_rate=samp_rate_strat,
        freq=freq_strat,
    )
)

test_makeRealWave_numsamps = deal.cases(
    func=makeRealWave_numsamps,
    kwargs=dict(
        num_samples=num_samples_strat,
        samp_rate=samp_rate_strat,
        freq=freq_strat
    )
)

test_makeComplexWave_time = deal.cases(
    func=makeComplexWave_time,
    kwargs=dict(
        seconds=seconds_strat,
        samp_rate=samp_rate_strat,
        freq=freq_strat
    )
)

test_makeRealWave_time = deal.cases(
    func=makeRealWave_time,
    kwargs=dict(
        seconds=seconds_strat,
        samp_rate=samp_rate_strat,
        freq=freq_strat
    )
)

test_multiply_by_complex_wave = deal.cases(
    func=multiply_by_complex_wave,
    kwargs=dict(
        baseband_sig=hyponp.arrays(
            dtype=np.uint8,
            shape=1
        ),
        samp_rate=samp_rate_strat,
        freq=freq_strat
    )
)

test_multiply_by_real_wave = deal.cases(
    func=multiply_by_real_wave,
    kwargs=dict(
        baseband_sig=hyponp.arrays(
            dtype=np.uint8,
            shape=1
        ),
        samp_rate=st.floats(0.01, 1e3),
        freq=st.floats(-1e12, 1e12)
    )
)