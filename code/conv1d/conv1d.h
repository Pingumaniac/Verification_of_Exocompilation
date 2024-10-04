
#pragma once
#ifndef CONV1D_H
#define CONV1D_H

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

typedef struct conv1d_Context { 

} conv1d_Context;


// conv1d(
//     n : size,
//     m : size,
//     r : size,
//     x : f32[n]  @DRAM,
//     w : f32[m]  @DRAM,
//     res : f32[r]  @DRAM
// )
void conv1d( conv1d_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t r, float* x, float* w, float* res );



#ifdef __cplusplus
}
#endif
#endif  // CONV1D_H
