import sys
import os


cwd = os.getcwd()
print(f"appending {cwd} to sys path")
sys.path.append(cwd)


raise ValueError("Need to make this integrate with pytest")

import doctest

import pcdr.helpers
doctest.testmod(pcdr.helpers)
