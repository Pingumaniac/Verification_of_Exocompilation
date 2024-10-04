#include "simple_blur_split.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// simple_blur_split(
//     n : size,
//     m : size,
//     k_size : size,
//     image : f32[n,m]  @DRAM,
//     kernel : f32[k_size,k_size]  @DRAM,
//     res : f32[n,m]  @DRAM
// )
void simple_blur_split( simple_blur_split_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t k_size, float* image, float* kernel, float* res ) {
for (int i = 0; i < n; i++) {
  for (int j1 = 0; j1 < ((m) / (2)); j1++) {
    for (int j2 = 0; j2 < 2; j2++) {
      res[(i) * (m) + (j1 * 2 + j2) * (1)] = 0.0;
    }
  }
}
for (int i = 0; i < n; i++) {
  for (int j1 = 0; j1 < ((m) / (2)); j1++) {
    for (int j2 = 0; j2 < 2; j2++) {
      for (int k = 0; k < k_size; k++) {
        for (int l = 0; l < k_size; l++) {
          if (i + k >= 1 && i + k - n < 1 && j1 * 2 + j2 + l >= 1 && j1 * 2 + j2 + l - m < 1) {
            res[(i) * (m) + (j1 * 2 + j2) * (1)] += kernel[(k) * (k_size) + (l) * (1)] * image[(i + k - 1) * (m) + (j1 * 2 + j2 + l - 1) * (1)];
          }
        }
      }
    }
  }
}
}
