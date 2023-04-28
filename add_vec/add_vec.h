
#pragma once
#ifndef ADD_VEC_H
#define ADD_VEC_H

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

typedef struct add_vec_Context { 

} add_vec_Context;


// add_vec(
//     n : size,
//     x : f32[n]  @DRAM,
//     y : f32[n]  @DRAM,
//     res : f32[n]  @DRAM
// )
void add_vec( add_vec_Context *ctxt, int_fast32_t n, float* x, float* y, float* res );



#ifdef __cplusplus
}
#endif
#endif  // ADD_VEC_H
