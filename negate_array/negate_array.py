# negate_array.py
from __future__ import annotations
from exo import *

@proc
def negate_array(n: size, x: R[n], res: R[n] @ DRAM):  
    for i in seq(0, n):
        res[i] = -x[i] + -(x[i]) - -(x[i] + 0.0)