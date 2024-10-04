#include "alloc_nest_malloc.h"

static int _floor_div(int num, int quot) {
  int off = (num>=0)? 0 : quot-1;
  return (num-off)/quot;
}

static int8_t _clamp_32to8(int32_t x) {
  return (x < -128)? -128 : ((x > 127)? 127 : x);
}

#include <stdio.h>
#include <stdlib.h>


// clang-format off
// these are filled in by Python's str.format()
#define HEAP_SIZE 100000
// clang-format on

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

uint8_t HEAP[HEAP_SIZE];

// https://stackoverflow.com/questions/5473189/what-is-a-packed-structure-in-c
typedef struct __attribute__((__packed__)) FreeBlock {
  uint32_t size;
  struct FreeBlock *next;
  uint8_t data[0];
} FreeBlock;
FreeBlock *freelist;

void init_mem() {
  FreeBlock *p = (FreeBlock *)HEAP;
  p->next = p + 1;
  p->size = 0;
  freelist = p;

  p++;
  p->next = 0;
  p->size = HEAP_SIZE - sizeof(FreeBlock);
}

void *search(FreeBlock *cur, uint32_t bytes) {
  FreeBlock *prev = freelist;

  for (;;) {
    uint32_t size = sizeof(uint32_t) + sizeof(FreeBlock *);

    if (cur->next == 0 && cur->size < bytes + size) {
      printf("Out of memory!\n");
      return 0;
    } else if (cur->next == 0 && cur->size >= (bytes + size)) {
      // cut cur into bytes blocks and create new
      uint32_t sz = cur->size;
      FreeBlock *new = (void *)cur + bytes + size;
      new->next = 0;
      new->size = sz - bytes - size;
      cur->size = bytes + size;
      prev->next = new;
      break;
    } else if (cur->size >= (bytes + size)) {
      prev->next = cur->next;
      break;
    } else {
      prev = cur;
      cur = cur->next;
    }
  }

  return cur->data;
}

void *malloc_dram(long unsigned int bytes) {
  bytes = bytes < sizeof(FreeBlock) ? sizeof(FreeBlock) : bytes;
  if (bytes == 0)
    return 0;
  FreeBlock *loc = search(freelist, bytes);
  if (loc == 0)
    return 0;
  else {
    return loc;
  }
}

void free_dram(void *ptr) {
  if (ptr == 0)
    return;
  ptr = ptr - sizeof(uint32_t) - sizeof(FreeBlock *);
  FreeBlock *next = freelist->next;
  freelist->next = ptr;
  ((FreeBlock *)ptr)->next = next;

  return;
}


// alloc_nest_malloc(
//     n : size,
//     m : size,
//     x : f32[n,m]  @MDRAM,
//     y : f32[n,m]  @MDRAM,
//     res : f32[n,m]  @MDRAM
// )
void alloc_nest_malloc( alloc_nest_malloc_Context *ctxt, int_fast32_t n, int_fast32_t m, float* x, float* y, float* res ) {
for (int i = 0; i < n; i++) {
  float *rloc = (float*) malloc_dram (m * sizeof(float));
  float *xloc = (float*) malloc_dram (m * sizeof(float));
  float *yloc = (float*) malloc_dram (m * sizeof(float));
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
  free_dram(rloc);
  free_dram(xloc);
  free_dram(yloc);
}
}
