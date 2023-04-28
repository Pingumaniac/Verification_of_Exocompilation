# blur.py
from __future__ import annotations
from exo import *

@proc
def blur(n: size, m: size, k_size: size, image: R[n, m], kernel: R[k_size, k_size], res: R[n, m]):
    for i in seq(0, n):
        for j in seq(0, m):
            res[i, j] = 0.0
    for i in seq(0, n):
        for j in seq(0, m):
            for k in seq(0, k_size):
                for l in seq(0, k_size):
                    if (i + k >= 1 and i + k - n < 1 and j + l >= 1 and j + l - m < 1):
                        res[i, j] += kernel[k, l] * image[i + k - 1, j + l - 1]
