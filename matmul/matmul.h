
#pragma once
#ifndef EXAMPLE_H
#define EXAMPLE_H

#ifdef __cplusplus
extern "C" {
#endif


#include <stdint.h>
#include <stdbool.h>

// Compiler feature macros adapted from Hedley (public domain)
// https://github.com/nemequ/hedley

#if defined(__has_builtin)
#  define EXO_HAS_BUILTIN(builtin) __has_builtin(builtin)
#else
#  define EXO_HAS_BUILTIN(builtin) (0)
#endif

#if EXO_HAS_BUILTIN(__builtin_assume)
#  define EXO_ASSUME(expr) __builtin_assume(expr)
#elif EXO_HAS_BUILTIN(__builtin_unreachable)
#  define EXO_ASSUME(expr) \
      ((void)((expr) ? 1 : (__builtin_unreachable(), 1)))
#else
#  define EXO_ASSUME(expr) ((void)(expr))
#endif

typedef struct example_Context { 

} example_Context;


// example_sgemm(
//     M : size,
//     N : size,
//     K : size,
//     C : f32[M,N]  @DRAM,
//     A : f32[M,K]  @DRAM,
//     B : f32[K,N]  @DRAM
// )
void example_sgemm( example_Context *ctxt, int_fast32_t M, int_fast32_t N, int_fast32_t K, float* C, float* A, float* B );



#ifdef __cplusplus
}
#endif
#endif  // EXAMPLE_H
