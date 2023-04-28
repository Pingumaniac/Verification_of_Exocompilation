#include "add_vec.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// add_vec(
//     n : size,
//     x : f32[n]  @DRAM,
//     y : f32[n]  @DRAM,
//     res : f32[n]  @DRAM
// )
void add_vec( add_vec_Context *ctxt, int_fast32_t n, float* x, float* y, float* res ) {
for (int i = 0; i < n; i++) {
  res[(i) * (1)] = x[(i) * (1)] + y[(i) * (1)];
}
}
