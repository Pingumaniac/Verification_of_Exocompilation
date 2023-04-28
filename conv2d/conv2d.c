#include "conv2d.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// conv2d(
//     n : size,
//     m : size,
//     p : size,
//     q : size,
//     r : size,
//     s : size,
//     x : f32[n,m]  @DRAM,
//     w : f32[p,q]  @DRAM,
//     res : f32[r,s]  @DRAM
// )
void conv2d( conv2d_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t p, int_fast32_t q, int_fast32_t r, int_fast32_t s, float* x, float* w, float* res ) {
for (int i = 0; i < r; i++) {
  for (int j = 0; j < s; j++) {
    res[(i) * (s) + (j) * (1)] = 0.0;
    for (int k = 0; k < p; k++) {
      for (int l = 0; l < q; l++) {
        if (i + k < n && j + l < m) {
          res[(i) * (s) + (j) * (1)] += x[(i + k) * (m) + (j + l) * (1)] * w[(k) * (q) + (l) * (1)];
        }
      }
    }
  }
}
}
