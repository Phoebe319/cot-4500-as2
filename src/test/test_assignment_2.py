from  main.assignment_2 import neville, diff_table, newtons_forward, divided_method, spline
import numpy as np

# neville's method
x_pts = [3.6, 3.8, 3.9]
y_pts = [1.675, 1.436, 1.318]
x_neville = 3.7
neville_answer = neville(x_pts, y_pts, x_neville)
print("{}\n".format(neville_answer))

# newton's method difference table
x_values = np.array([7.2, 7.4, 7.5, 7.6])
f_x_values = np.array([23.5492, 25.3913, 26.8224, 27.4589])
h = x_values[1] - x_values[0]
x0 = x_values[0]
difference_table = diff_table(x_values, f_x_values)
print(difference_table[0][1])
print(difference_table[0][2])
print(difference_table[0][3])

# newton's method approximate f(7.3)
x_value = 7.3
approx_value = newtons_forward(x_value, 2, h, x0, f_x_values, difference_table)
print("\n{}\n".format(approx_value))

# divided method
x = [3.6, 3.8, 3.9]
f_x = [1.675, 1.436, 1.318]
f_prime_x = [-1.195, -1.188, -1.182]
result = divided_method(x, f_x, f_prime_x)
print("{}\n".format(result))

# cubic spline interpolation
x_points = [2, 5, 8, 10]
y_points = [3, 5, 7, 9]
spline(x_points, y_points)