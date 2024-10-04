from pysmt.shortcuts import *

def encodeAllocNestMallocPython(n, m, x, y, res):
    for i in range(n):
        for j in range(m):
            xloc_j = x[i][j]
            yloc_j = y[i][j]
            rloc_j = xloc_j + yloc_j
            res[i][j] = rloc_j

def encodeAllocNestMallocC(n, m, x, y, res):
    for i in range(n):
        for j in range(m):
            xloc_j = x[i][j]
            yloc_j = y[i][j]
            rloc_j = xloc_j + yloc_j
            res[i][j] = rloc_j

def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == "__main__":
    n, m = 3, 3

    x = assignMatrix(n, m)
    y =  assignMatrix(n, m)
    outputPython = assignMatrix(n, m)
    outputC = assignMatrix(n, m)

    encodeAllocNestMallocPython(n, m, x, y, outputPython)
    encodeAllocNestMallocC(n, m, x, y, outputC)

    solver = Solver(name='z3')

    # Add the constraints
    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(n) for j in range(m)]
    result = solver.solve(assumptions)
    
    if result:
        print("alloc_nest_malloc.py and alloc_nest_malloc.c are not equivalent.")
    else:
        print("alloc_nest_malloc.py and alloc_nest_malloc.c are equivalent.")
