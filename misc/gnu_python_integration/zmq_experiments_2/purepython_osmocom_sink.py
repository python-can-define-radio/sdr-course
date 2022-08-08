"""
This file provides a python interface to the GNU Radio osmocom sink.
It's inspired by [SoapySDR](https://github.com/pothosware/SoapySDR/wiki/PythonSupport),
and is particularly useful when one has access to the former but not the latter.

Implementation approach:
Create a GNU Radio flowgraph with two blocks:
  zmq source -> osmocom sink
"""


