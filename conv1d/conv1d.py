# example.py
from __future__ import annotations
from exo import *

@proc
def conv1d(n: size, m: size, r: size, x: R[n], w: R[m], res: R[r]):
    for i in seq(0, r):
        res[i] = 0.0
    for i in seq(0, r):
        for j in seq(0, n):
            if j < i + 1 and j >= i - (m - 1):
                res[i] += x[j] * w[i - j]