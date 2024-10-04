# conv2d.py
from __future__ import annotations
from exo import *

@proc
def conv2d(n: size, m: size, p: size, q: size, r: size, s: size, x: R[n, m], w: R[p, q], res: R[r, s]):
    for i in seq(0, r):
        for j in seq(0, s):
            res[i, j] = 0.0
            for k in seq(0, p):
                for l in seq(0, q):
                    if (i + k < n) and (j + l < m):
                        res[i, j] += x[i + k, j + l] * w[k, l]
