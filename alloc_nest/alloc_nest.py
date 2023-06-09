# alloc_nest.py
from __future__ import annotations
from exo import *

@proc
def alloc_nest(n: size, m: size, x: R[n, m], y: R[n, m] @ DRAM, res: R[n, m] @ DRAM):
    for i in seq(0, n):
        rloc: R[m] @ DRAM
        xloc: R[m] @ DRAM
        yloc: R[m] @ DRAM
        for j in seq(0, m):
            xloc[j] = x[i, j]
        for j in seq(0, m):
            yloc[j] = y[i, j]
        for j in seq(0, m):
            rloc[j] = xloc[j] + yloc[j]
        for j in seq(0, m):
            res[i, j] = rloc[j]