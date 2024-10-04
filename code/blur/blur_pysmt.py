from pysmt.shortcuts import *


def encodeBlurPython(solver, n, m, k_size, image, kernel, res):
    for i in range(n):
        for j in range(m):
            solver.add_assertion(Equals(res[i][j], Real(0)))
            for k in range(k_size):
                for l in range(k_size):
                    if i + k >= 1 and i + k - n < 1 and j + l >= 1 and j + l - m < 1:
                        solver.add_assertion(Equals(res[i][j], Plus(res[i][j], Times(kernel[k][l], image[i + k - 1][j + l - 1]))))

def encodeBlurC(solver, n, m, k_size, image, kernel, res):
    for i in range(n):
        for j in range(m):
            solver.add_assertion(Equals(res[i][j], Real(0)))
            for k in range(k_size):
                for l in range(k_size):
                    if i + k >= 1 and i + k - n < 1 and j + l >= 1 and j + l - m < 1:
                        solver.add_assertion(Equals(res[i][j], Plus(res[i][j], Times(kernel[k][l], image[i + k - 1][j + l - 1]))))


def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == '__main__':
    n, m = 7, 7  # You can change the image size
    k_size = 3  # You can change the kernel size

    image = assignMatrix(n, m)
    kernel = assignMatrix(k_size, k_size)
    outputPython = assignMatrix(n, m)
    outputC = assignMatrix(n, m)
    
    solver = Solver(name='z3')

    encodeBlurPython(solver, n, m, k_size, image, kernel, outputPython)
    encodeBlurC(solver, n, m, k_size, image, kernel, outputC)

    for i in range(n):
        for j in range(m):
            solver.add_assertion(Not(Equals(outputPython[i][j], outputC[i][j])))
    result = solver.solve()
    
    if result:
        print("blur.py and blur.c are not equivalent.")
    else:
        print("blur.py and blur.c are equivalent.")