from queue import SimpleQueue

import hypothesis.extra.numpy as hyponp
import hypothesis.strategies as st
import numpy as np

from pcdr._beta.gnuradio_sendlike import _pad_chunk_queue
from pcdr._internal.misc import queue_to_list



def test_queue_to_list_empty_queue():
    assert queue_to_list(SimpleQueue()) == []


from pcdr._wavegen import (
    makeRealWave_basic,
    makeComplexWave_basic,
    _isAliasingWhenDisallowed,
    _aliasingError,
    makeComplexWave_numsamps,
    makeRealWave_numsamps,
    makeComplexWave_time,
    makeRealWave_time,
    multiply_by_complex_wave,
    multiply_by_real_wave,
    noisify
)

seconds_strat = st.floats(0, 100)
num_samples_strat = st.integers(0, 100)
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



# test_makeRealWave = deal.cases(
#     func=makeRealWave,
#     kwargs=dict(
#         timestamps=timestamps_strat,
#         freq=freq_strat
#     )
# )

# test_makeComplexWave = deal.cases(
#     func=makeComplexWave,
#     kwargs=dict(
#         timestamps=timestamps_strat,
#         freq=freq_strat
#     )
# )

# test__isAliasingWhenDisallowed = deal.cases(_isAliasingWhenDisallowed)

# test__aliasingError = deal.cases(_aliasingError)

# test_makeComplexWave_numsamps = deal.cases(
#     func=makeComplexWave_numsamps,
#     kwargs=dict(
#         num_samples=num_samples_strat,
#         samp_rate=samp_rate_strat,
#         freq=freq_strat,
#     )
# )

# test_makeRealWave_numsamps = deal.cases(
#     func=makeRealWave_numsamps,
#     kwargs=dict(
#         num_samples=num_samples_strat,
#         samp_rate=samp_rate_strat,
#         freq=freq_strat
#     )
# )

# test_makeComplexWave_time = deal.cases(
#     func=makeComplexWave_time,
#     kwargs=dict(
#         seconds=seconds_strat,
#         samp_rate=samp_rate_strat,
#         freq=freq_strat
#     )
# )

# test_makeRealWave_time = deal.cases(
#     func=makeRealWave_time,
#     kwargs=dict(
#         seconds=seconds_strat,
#         samp_rate=samp_rate_strat,
#         freq=freq_strat
#     )
# )

# test_multiply_by_complex_wave = deal.cases(
#     func=multiply_by_complex_wave,
#     kwargs=dict(
#         baseband_sig=hyponp.arrays(
#             dtype=np.uint8,
#             shape=1
#         ),
#         samp_rate=samp_rate_strat,
#         freq=freq_strat
#     )
# )

# test_multiply_by_real_wave = deal.cases(
#     func=multiply_by_real_wave,
#     kwargs=dict(
#         baseband_sig=hyponp.arrays(
#             dtype=np.uint8,
#             shape=1
#         ),
#         samp_rate=st.floats(0.01, 1e3),
#         freq=st.floats(-1e12, 1e12)
#     )
# )

# test_noisify = deal.cases(
#     func=noisify,
#     kwargs=dict(
#         data=hyponp.arrays(dtype=np.complex64, shape=1),
#     )
# )