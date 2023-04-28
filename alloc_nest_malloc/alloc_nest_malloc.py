# alloc_nest_malloc.py
from __future__ import annotations
from exo import *
from exo.libs.memories import MDRAM

@proc
def alloc_nest_malloc(n: size, m: size, x: R[n, m] @ MDRAM, y: R[n, m] @ MDRAM, res: R[n, m] @ MDRAM):
    for i in seq(0, n):
        rloc: R[m] @ MDRAM
        xloc: R[m] @ MDRAM
        yloc: R[m] @ MDRAM
        for j in seq(0, m):
            xloc[j] = x[i, j]
        for j in seq(0, m):
            yloc[j] = y[i, j]
        for j in seq(0, m):
            rloc[j] = xloc[j] + yloc[j]
        for j in seq(0, m):
            res[i, j] = rloc[j]