#include "example.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// example_sgemm(
//     M : size,
//     N : size,
//     K : size,
//     C : f32[M,N]  @DRAM,
//     A : f32[M,K]  @DRAM,
//     B : f32[K,N]  @DRAM
// )
void example_sgemm( example_Context *ctxt, int_fast32_t M, int_fast32_t N, int_fast32_t K, float* C, float* A, float* B ) {
for (int i = 0; i < M; i++) {
  for (int j = 0; j < N; j++) {
    for (int k = 0; k < K; k++) {
      C[(i) * (N) + (j) * (1)] += A[(i) * (K) + (k) * (1)] * B[(k) * (N) + (j) * (1)];
    }
  }
}
}
