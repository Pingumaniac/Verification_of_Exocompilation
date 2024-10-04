from pysmt.shortcuts import *

def encodeAllocNestPython(solver, n, m, x, y, outputPython):
    for i in range(n):
        rloc = [Real(i + j) for j in range(m)]
        xloc = [Real(i + j) for j in range(m)]
        yloc = [Real(i + j) for j in range(m)]
        for j in range(m):
            solver.add_assertion(Equals(xloc[j], x[i][j]))
        for j in range(m):
            solver.add_assertion(Equals(yloc[j], y[i][j]))
        for j in range(m):
            solver.add_assertion(Equals(rloc[j], Plus(xloc[j], yloc[j])))
        for j in range(m):
            solver.add_assertion(Equals(outputPython[i][j], rloc[j]))

def encodeAllocNestC(solver, n, m, x, y, outputC):
    for i in range(n):
        rloc = [Real(i + j) for j in range(m)]
        xloc = [Real(i + j) for j in range(m)]
        yloc = [Real(i + j) for j in range(m)]
        for j in range(m):
            solver.add_assertion(Equals(xloc[j], x[i][j]))
        for j in range(m):
            solver.add_assertion(Equals(yloc[j], y[i][j]))
        for j in range(m):
            solver.add_assertion(Equals(rloc[j], Plus(xloc[j], yloc[j])))
        for j in range(m):
            solver.add_assertion(Equals(outputC[i][j], rloc[j]))

def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == "__main__":
    n, m = 3, 3

    x = assignMatrix(n, m)
    y =  assignMatrix(n, m)
    outputPython = assignMatrix(n, m)
    outputC = assignMatrix(n, m)

    solver = Solver(name='z3')

    encodeAllocNestPython(solver, n, m, x, y, outputPython)
    encodeAllocNestC(solver, n, m, x, y, outputC)

    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(n) for j in range(m)]
    result = solver.solve(assumptions)

    if result:
        print("alloc_nest.py and alloc_nest.c are not equivalent.")
    else:
        print("alloc_nest.py and alloc_nest.c are equivalent.")
