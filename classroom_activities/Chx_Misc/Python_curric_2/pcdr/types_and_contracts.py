from __future__ import annotations
from typing import Union, TypeVar
import deal



## As per https://stackoverflow.com/questions/43957034/specifying-a-type-to-be-a-list-of-numbers-ints-and-or-floats
TRealNum = TypeVar('TRealNum', int, float)

TRealOrComplexNum = TypeVar('TRealOrComplexNum', int, float, complex)


