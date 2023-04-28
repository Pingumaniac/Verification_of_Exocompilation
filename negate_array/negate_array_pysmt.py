from pysmt.shortcuts import *

def negateArrayPython(n, x, res):
    for i in range(n):
        res[i] = -x[i] + -(x[i]) - -(x[i] + 0.0)

def negateArrayC(n, x, res):
    for i in range(n):
        res[i * 1] = -x[i * 1] + -(x[i * 1]) - -(x[i * 1] + 0.0)

def encodeNegateArrayPython(solver, n, x, res):
    for i in range(n):
        solver.add_assertion(Equals(res[i], Plus(-x[i], Minus(-(x[i]), -(x[i] + 0.0)))))

def encodeNegateArrayC(solver, n, x, res):
    for i in range(n):
        solver.add_assertion(Equals(res[i * 1], Plus(-x[i * 1], Minus(-(x[i * 1]), -(x[i * 1] + 0.0)))))

def assignMatrix(X):
    return [Real(i) for i in range(X)]

if __name__ == '__main__':
    n = 10  # You can change the size of the vectors
    x = assignMatrix(n)
    outputPython = assignMatrix(n)
    outputC = assignMatrix(n)

    solver = Solver(name='z3')

    encodeNegateArrayPython(solver, n, x, outputPython)
    encodeNegateArrayC(solver, n, x, outputC)

    for i in range(n):
        solver.add_assertion(Not(Equals(outputPython[i], outputC[i])))

    result = solver.solve()
    
    if result:
        print("negate_array.py and negate_array.c are not equivalent.")
    else:
        print("negate_array.py and negate_array.c are equivalent.")