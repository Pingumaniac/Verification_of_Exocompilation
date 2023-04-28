from pysmt.shortcuts import *

def encodeMatMulPython(M, N, K, A, B, C):
    for i in range(M):
        for j in range(N):
            for k in range(K):
                C[i][j] += Times(A[i][k], B[k][j])

def encodeMatMulC(M, N, K, A, B, C):
    for i in range(M):
        for j in range(N):
            for k in range(K):
                # Note: C has a different way of representing a 2D array
                # C[(i) * (N) + (j) * (1)] += A[(i) * (K) + (k) * (1)] * B[(k) * (N) + (j) * (1)];
                C[i][j * 1] += Times(A[i][k * 1], B[k][j * 1])

def assignMatrix(X, Y):
    return [[Real(i + j) for j in range(Y)] for i in range(X)]

if __name__ == '__main__':
    # Set the dimensions of matrices A, B, and C
    M, N, K = 2, 2, 2

    # Set the input matrices A, B with Real values
    A = assignMatrix(M, K)
    B = assignMatrix(K, N)
    
    # Set the output matrices outputPython and outputC with Real values
    outputPython =  assignMatrix(M, N)
    outputC = assignMatrix(M, N)

    # Execute both matrix multiplication implementations with the given input matrices
    encodeMatMulPython(M, N, K, A, B, outputPython)
    encodeMatMulC(M, N, K, A, B, outputC)

    s = Solver(name="z3")

    # Define the constraints: the elements of outputPython and outputC shall not be equal
    assumptions = [Not(Equals(outputPython[i][j], outputC[i][j])) for i in range(M) for j in range(N)]
    # Add the constraints to the solver
    s.add_assertion(And(assumptions))

    if s.solve():
        print("matmul.py and matmul.c are not equivalent.")
    else:
        print("matmul.py and matmul.c are equivalent.")