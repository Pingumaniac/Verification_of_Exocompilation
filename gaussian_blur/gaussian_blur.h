
#pragma once
#ifndef GAUSSIAN_BLUR_H
#define GAUSSIAN_BLUR_H

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

typedef struct gaussian_blur_Context { 

} gaussian_blur_Context;


// gaussian_blur(
//     n : size,
//     m : size,
//     k_size : size,
//     image : f32[n,m]  @DRAM,
//     kernel : f32[k_size,k_size]  @DRAM,
//     res : f32[n,m]  @DRAM
// )
void gaussian_blur( gaussian_blur_Context *ctxt, int_fast32_t n, int_fast32_t m, int_fast32_t k_size, float* image, float* kernel, float* res );



#ifdef __cplusplus
}
#endif
#endif  // GAUSSIAN_BLUR_H
