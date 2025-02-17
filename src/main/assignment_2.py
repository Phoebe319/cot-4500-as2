import numpy as np

# neville's method
def neville(x_pts, y_pts, x):
    n = len(x_pts)
    P = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        P[i][i] = y_pts[i]

    for j in range(1, n):
        for i in range(n-j):
            P[i][i+j] = ((x - x_pts[i+j]) * P[i][i+j-1] - (x - x_pts[i]) * P[i+1][i+j]) / (x_pts[i] - x_pts[i+j])
    return P[0][n-1]

# difference table for newton's forward method
def diff_table(x_values, f_x_values):
    n = len(x_values)
    difference_table = np.zeros((n, n))
    difference_table[:, 0] = f_x_values
    for j in range(1, n):
        for i in range(n - j):
            # determine what degree we're calculating to determine the x interval
            if j == 1:  # degree 1
                diff_interval = x_values[i+1] - x_values[i]
            elif j == 2:  # degree 2
                diff_interval = x_values[i+2] - x_values[i]
            elif j == 3:  # degree 3
                diff_interval = x_values[i+3] - x_values[i]
            # calculation for difference table
            difference_table[i][j] = (difference_table[i+1][j-1] - difference_table[i][j-1]) / diff_interval
    return difference_table

# calculate u for newton's method
def u_calculate(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
    return temp

# factorial function for newton's method
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# main newton's method
def newtons_forward(x_value, degree, h, x0, f_x_values, difference_table):
    u = (x_value - x0) / h
    approx = f_x_values[0] # start with first f(x) value

    for i in range(1, degree+1):
        approx += (u_calculate(u, i) * difference_table[0][i]) / factorial(i)
    
    return approx

# divided method
def divided_method(x, f_x, f_prime_x):
    n = len(x)
    tmp = 0
    table = np.zeros((2*n, 5))
    table[:, 0] = [item for item in x for _ in range(2)] # set up first column
    table[:, 1] = [item for item in f_x for _ in range(2)] # set up second column
    for i in range(0, 5): # third column
        if i % 2 == 0:
            table[i, 2] = f_prime_x[tmp]
            tmp += 1
        else:
            table[i, 2] = (table[i+1, 1] - table[i, 1]) / (table[i+1, 0] - table[i, 0])
    for i in range(0, 4): # fourth column
        table[i, 3] = (table[i+1, 2] - table[i, 2]) / (table[i+2, 0] - table[i, 0])
    for i in range(0, 3): # fifth column
        table[i, 4] = (table[i+1, 3] - table[i, 3]) / (table[i+3, 0] - table[i, 0])
    return table

# cubic spline interpolation
def spline(x_points, y_points):
    h = [x_points[i+1] - x_points[i] for i in range(len(x_points) - 1)]
    
    # set up A matrix
    A = np.zeros((4, 4))
    A[0, 0] = 1
    A[3, 3] = 1
    A[1, 0] = h[0]
    A[1, 1] = 2 * (h[0] + h[1])
    A[1, 2] = h[1]
    A[2, 1] = h[1]
    A[2, 2] = 2 * (h[1] + h[2])
    A[2, 3] = h[2]
    
    # set up b matrix
    b = np.zeros(4)
    b[1] = (6/h[1]) * (y_points[2] - y_points[1]) - (6/h[0]) * (y_points[1] - y_points[0])
    b[2] = (6/h[2]) * (y_points[3] - y_points[2]) - (6/h[1]) * (y_points[2] - y_points[1])

    # calculate vector x
    x_vector = np.linalg.solve(A, b)
    print(A)
    print(b)
    print(x_vector)