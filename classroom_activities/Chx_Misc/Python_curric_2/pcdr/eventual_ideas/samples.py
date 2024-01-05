from dataclasses import dataclass
from typing import TypeVar


if __name__ == "__main__":
    print("""
          I want to learn more how Pint handles these. 
          It's POSSIBLE that we can simply use pint, but only
          if it has a way to pair a numpy array with a scalar.""")
    T = TypeVar("T")

    @dataclass
    class Samples:
        data: T
        samp_rate: float