from pysmt.shortcuts import *

def encodeGaussianBlurPython(n, m, k_size, image, kernel, res):
    for i in range(n):
        for j in range(m):
            res[i][j] = 0.0
            for k in range(k_size):
                for l in range(k_size):
                    if (i + k >= 1 and i + k - n < 1 and j + l >= 1 and j + l - m < 1):
                        res[i][j] += Times(kernel[k][l], image[i + k - 1][j + l - 1])

def encodeGaussianBlurC(n, m, k_size, image, kernel, res):
    for i in range(n):
        for j in range(m):
            res[i][j] = 0.0
            for k in range(k_size):
                for l in range(k_size):
                    if (i + k >= 1 and i + k - n < 1 and j + l >= 1 and j + l - m < 1):
                        res[i][j] += Times(kernel[k][l], image[i + k - 1][j + l - 1])

def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == '__main__':
    n, m = 7, 7  # You can change the image size
    k_size = 3  # You can change the kernel size

    image = assignMatrix(n, m)
    kernel = assignMatrix(k_size, k_size)
    outputPython = assignMatrix(n, m)
    outputC = assignMatrix(n, m)

    encodeGaussianBlurPython(n, m, k_size, image, kernel, outputPython)
    encodeGaussianBlurC(n, m, k_size, image, kernel, outputC)

    solver = Solver(name="z3")

    # Add the constraints
    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(n) for j in range(m)]
    result = solver.solve(assumptions)

    if result:
        print("gausian_blur.py and gaussian_blur.c are not equivalent.")
    else:
        print("gausian_blur.py and gaussian_blur.c are equivalent.")