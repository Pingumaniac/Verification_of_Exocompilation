
#pragma once
#ifndef ALLOC_NEST_H
#define ALLOC_NEST_H

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

typedef struct alloc_nest_Context { 

} alloc_nest_Context;


// alloc_nest(
//     n : size,
//     m : size,
//     x : f32[n,m]  @DRAM,
//     y : f32[n,m]  @DRAM,
//     res : f32[n,m]  @DRAM
// )
void alloc_nest( alloc_nest_Context *ctxt, int_fast32_t n, int_fast32_t m, float* x, float* y, float* res );



#ifdef __cplusplus
}
#endif
#endif  // ALLOC_NEST_H
