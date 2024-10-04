from pysmt.shortcuts import *

def addVecPython(n, x, y, res):
    for i in range(n):
        res[i] = x[i] + y[i]

def addVecC(n, x, y, res):
    for i in range(n):
        res[i * 1] = x[i * 1] + y[i * 1]

def encodeAddVecPython(solver, n, x, y, res):
    for i in range(n):
        solver.add_assertion(Equals(res[i], Plus(x[i], y[i])))

def encodeAddVecC(solver, n, x, y, res):
    for i in range(n):
        solver.add_assertion(Equals(res[i * 1], Plus(x[i * 1], y[i * 1])))


def assignMatrix(X):
    return [Real(i) for i in range(X)]

if __name__ == '__main__':
    n = 10  # You can change the size of the vectors
    x = assignMatrix(n)
    y = assignMatrix(n)
    outputPython = assignMatrix(n)
    outputC = assignMatrix(n)

    solver = Solver(name='z3')

    encodeAddVecPython(solver, n, x, y, outputPython)
    encodeAddVecC(solver, n, x, y, outputC)

    for i in range(n):
        solver.add_assertion(Not(Equals(outputPython[i], outputC[i])))
    result = solver.solve()

    if result:
        print("add_vec.py and add_vec.c are not equivalent.")
    else:
        print("add_vec.py and add_vec.c are equivalent.")