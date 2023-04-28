
#pragma once
#ifndef NEGATE_ARRAY_H
#define NEGATE_ARRAY_H

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

typedef struct negate_array_Context { 

} negate_array_Context;


// negate_array(
//     n : size,
//     x : f32[n]  @DRAM,
//     res : f32[n]  @DRAM
// )
void negate_array( negate_array_Context *ctxt, int_fast32_t n, float* x, float* res );



#ifdef __cplusplus
}
#endif
#endif  // NEGATE_ARRAY_H
