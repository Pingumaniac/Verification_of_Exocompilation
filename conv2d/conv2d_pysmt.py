from pysmt.shortcuts import *

def encodeConv2dPython(solver, n, m, p, q, r, s, x, w, res):
    for i in range(r):
        for j in range(s):
            for k in range(p):
                for l in range(q):
                    if i + k < n and j + l < m:
                        solver.add_assertion(Equals(res[i][j], Plus(res[i][j], Times(x[i + k][j + l], w[k][l]))))

def encodeConv2dC(solver, n, m, p, q, r, s, x, w, res):
    for i in range(r):
        for j in range(s):
            for k in range(p):
                for l in range(q):
                    if i + k < n and j + l < m:
                        solver.add_assertion(Equals(res[i][j], Plus(res[i][j], Times(x[i + k][j + l], w[k][l]))))

def assignMatrix(X, Y, option=1):
    if option == 0:
        return [[Real(0) for j in range(Y)] for i in range(X)]
    else:
        return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == '__main__':
    # These are the dimensions (rows, columns) of the input matrix 
    n, m = 7, 7
    # These are the dimensions (rows, columns) of the kernel matrix
    p, q = 3, 3
    # These are the dimensions (rows, columns) of the output matrix
    r, s = 7, 7

    # The input matrix in which convolution is to be performed
    x = assignMatrix(n, m, 1)
    
    # The kernel matrix to perform the convolution
    w = assignMatrix(p, q, 1)
    
    # Output matrices
    outputPython = assignMatrix(r, s, 0)
    outputC = assignMatrix(r, s, 0)

    solver = Solver(name="z3")

    encodeConv2dPython(solver, n, m, p, q, r, s, x, w, outputPython)
    encodeConv2dC(solver, n, m, p, q, r, s, x, w, outputC)

    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(r) for j in range(s)]
    result = solver.solve(assumptions)

    if result:
        print("conv2d.py and conv2d.c are not equivalent.")
    else:
        print("conv2d.py and conv2d.c are equivalent.")