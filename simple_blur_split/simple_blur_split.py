# simple_blur_split.py
from __future__ import annotations
from exo import *

@proc
def simple_blur_split(n: size, m: size, k_size: size, image: R[n, m], kernel: R[k_size, k_size], res: R[n, m]):
        for i in seq(0, n):
            for j1 in seq(0, m / 2):
                for j2 in seq(0, 2):
                    res[i, j1 * 2 + j2] = 0.0
        for i in seq(0, n):
            for j1 in seq(0, m / 2):
                for j2 in seq(0, 2):
                    for k in seq(0, k_size):
                        for l in seq(0, k_size):
                            if (i + k >= 1 and i + k - n < 1 and j1 * 2 + j2 + l >= 1 and j1 * 2 + j2 + l - m < 1):
                                res[i, j1 * 2 + j2] += (kernel[k, l] * image[i + k - 1, j1 * 2 + j2 + l - 1])