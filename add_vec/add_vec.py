# add_vec.py
from __future__ import annotations
from exo import *

@proc
def add_vec(n: size, x: R[n], y: R[n], res: R[n]):
    for i in seq(0, n):
        res[i] = x[i] + y[i]