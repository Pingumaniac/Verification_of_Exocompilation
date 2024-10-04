from pysmt.shortcuts import *

def encodeSimpleBlurSplitPython(n, m, k_size, image, kernel, res):
    for i in range(n):
        for j1 in range(m // 2):
            for j2 in range(2):
                res[i][j1 * 2 + j2] = 0.0
    
    for i in range(n):
        for j1 in range(m // 2):
            for j2 in range(2):
                for k in range(k_size):
                    for l in range(k_size):
                        if (i + k >= 1 and i + k - n < 1 and j1 * 2 + j2 + l >= 1 and j1 * 2 + j2 + l - m < 1):
                            res[i][j1 * 2 + j2] += kernel[k][l] * image[i + k - 1][j1 * 2 + j2 + l - 1]

def encodeSimpleBlurSplitC(n, m, k_size, image, kernel, res):
    for i in range(n):
        for j1 in range(m // 2):
            for j2 in range(2):
                res[i][j1 * 2 + j2] = 0.0
    
    for i in range(n):
        for j1 in range(m // 2):
            for j2 in range(2):
                for k in range(k_size):
                    for l in range(k_size):
                        if (i + k >= 1 and i + k - n < 1 and j1 * 2 + j2 + l >= 1 and j1 * 2 + j2 + l - m < 1):
                            res[i][j1 * 2 + j2] += kernel[k][l] * image[i + k - 1][j1 * 2 + j2 + l - 1]

def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == '__main__':
    n, m = 7, 7  # You can change the image size
    k_size = 3  # You can change the kernel size

    image = assignMatrix(n, m)
    kernel = assignMatrix(k_size, k_size)
    outputPython = assignMatrix(n, m)
    outputC = assignMatrix(n, m)

    encodeSimpleBlurSplitPython(n, m, k_size, image, kernel, outputPython)
    encodeSimpleBlurSplitC(n, m, k_size, image, kernel, outputC)

    solver = Solver(name='z3')

    # Add the constraints
    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(n) for j in range(m)]
    result = solver.solve(assumptions)

    if result:
        print("The simple blur split functions are not equivalent.")
    else:
        print("The simple blur split functions are equivalent.")
