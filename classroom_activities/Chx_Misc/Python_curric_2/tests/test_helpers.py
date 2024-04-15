from hypothesis import given
from hypothesis.strategies import text

from pcdr._helpers import str_to_bin_list, bytes_to_bin_list


@given(text(alphabet=[chr(c) for c in range(128)]))
def test_bin_funcs_match_for_first_128_chars(s: str):
    assert str_to_bin_list(s) == bytes_to_bin_list(s.encode("ASCII"))
