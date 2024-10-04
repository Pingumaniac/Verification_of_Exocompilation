#include "alloc_nest.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// alloc_nest(
//     n : size,
//     m : size,
//     x : f32[n,m]  @DRAM,
//     y : f32[n,m]  @DRAM,
//     res : f32[n,m]  @DRAM
// )
void alloc_nest( alloc_nest_Context *ctxt, int_fast32_t n, int_fast32_t m, float* x, float* y, float* res ) {
for (int i = 0; i < n; i++) {
  float *rloc = malloc(m * sizeof(*rloc));
  float *xloc = malloc(m * sizeof(*xloc));
  float *yloc = malloc(m * sizeof(*yloc));
  for (int j = 0; j < m; j++) {
    xloc[(j) * (1)] = x[(i) * (m) + (j) * (1)];
  }
  for (int j = 0; j < m; j++) {
    yloc[(j) * (1)] = y[(i) * (m) + (j) * (1)];
  }
  for (int j = 0; j < m; j++) {
    rloc[(j) * (1)] = xloc[(j) * (1)] + yloc[(j) * (1)];
  }
  for (int j = 0; j < m; j++) {
    res[(i) * (m) + (j) * (1)] = rloc[(j) * (1)];
  }
  free(rloc);
  free(xloc);
  free(yloc);
}
}
