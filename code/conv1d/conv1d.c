#include "conv1d.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// conv1d(
//     n : size,
//     m : size,
//     r : size,
//     x : f32[n]  @DRAM,
//     w : f32[m]  @DRAM,
//     res : f32[r]  @DRAM
// )
void conv1d( conv1d_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t r, float* x, float* w, float* res ) {
for (int i = 0; i < r; i++) {
  res[(i) * (1)] = 0.0;
}
for (int i = 0; i < r; i++) {
  for (int j = 0; j < n; j++) {
    if (j < i + 1 && j >= i - (m - 1)) {
      res[(i) * (1)] += x[(j) * (1)] * w[(i - j) * (1)];
    }
  }
}
}
