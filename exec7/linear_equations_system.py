import time

import numpy as np
import cvxpy as cv
import matplotlib.pyplot as plt


def run_with_numpy(matrix_size: int):
    coeffs = np.random.randint(20, size=(matrix_size, matrix_size))
    res2 = np.random.randint(20, size=matrix_size)
    start_time = time.time()
    np.linalg.solve(coeffs, res2)
    end_time = time.time()
    return end_time - start_time


def run_with_cvxpy(matrix_size: int):
    coeffs = np.random.randint(20, size=(matrix_size, matrix_size))
    res2 = np.random.randint(20, size=matrix_size)
    var_in_linear_system = cv.Variable(matrix_size)
    cont = []
    co = []
    for i in range(matrix_size):
        Sum = 0
        for j in range(matrix_size):
            Sum = Sum + (coeffs[i][j] * var_in_linear_system[j])
        c = Sum == res2[i]
        cont.append(c)


    objective = cv.Minimize(sum(var_in_linear_system))
    problem = cv.Problem(objective, co)
    start_time = time.time()
    problem.solve()
    end_time = time.time()
    return end_time - start_time




running_time_solve_with_numpy = []
running_time_solve_with_cvxpy = []
for i in range(1, 11):
    running_time_solve_with_numpy.append(run_with_numpy(i))
    running_time_solve_with_cvxpy.append(run_with_cvxpy(i))

plt.title("compare running time Numpy vs Cxvpy")
plt.plot(running_time_solve_with_numpy, 'b', running_time_solve_with_cvxpy, 'r')
plt.legend(["numpy", "cxvpy"])
plt.xlabel("size of matrix (n*n)")
plt.ylabel("running time in sec")
plt.figure(figsize=(30, 30))
plt.show()

print(run_with_cvxpy(5))
