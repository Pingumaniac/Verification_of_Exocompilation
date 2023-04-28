
#pragma once
#ifndef CONV2D_H
#define CONV2D_H

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

typedef struct conv2d_Context { 

} conv2d_Context;


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
void conv2d( conv2d_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t p, int_fast32_t q, int_fast32_t r, int_fast32_t s, float* x, float* w, float* res );



#ifdef __cplusplus
}
#endif
#endif  // CONV2D_H
