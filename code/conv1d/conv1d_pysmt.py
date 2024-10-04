from pysmt.shortcuts import *

def encodeConv1dPython(solver, n, m, r, x, w, res):
    for i in range(r):
        solver.add_assertion(Equals(res[i], Real(0)))
        for j in range(n):
            if j < i + 1 and j >= i - (m - 1):
                solver.add_assertion(Equals(res[i], Plus(res[i], Times(x[j], w[i - j]))))

def encodeConv1dC(solver, n, m, r, x, w, res):
    for i in range(r):
        solver.add_assertion(Equals(res[i], Real(0)))
        for j in range(n):
            if j < i + 1 and j >= i - (m - 1):
                solver.add_assertion(Equals(res[i], Plus(res[i], Times(x[j], w[i - j]))))

def assignMatrix(X):
    return [Real(i) for i in range(X)]

if __name__ == '__main__':
    # Feel free to change these values
    n = 7  # The size of the input signal x
    m = 3  # The size of the kernel w
    r = 4  # The size of the result signal res

    x = assignMatrix(n)
    w = assignMatrix(m)
    
    outputPython = assignMatrix(r)
    outputC = assignMatrix(r)

    solver = Solver(name="z3")

    encodeConv1dPython(solver, n, m, r, x, w, outputPython)
    encodeConv1dC(solver, n, m, r, x, w, outputC)

    assumptions = [Not(Equals(outputPython[i], outputC[i])) for i in range(r)]
    solver.add_assertion(And(assumptions))
    result = solver.solve(assumptions)

    if result:
        print("conv1d.py and conv1d.c are not equivalent.")
    else:
        print("conv1d.py and conv1d.c are equivalent.")
