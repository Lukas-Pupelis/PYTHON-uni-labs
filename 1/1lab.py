
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Task 1: Generate 64 evenly spaced values between -1.3 and 2.5
interval = np.linspace(-1.3, 2.5, 64)
print("Task 1: Interval\n", interval)

# Task 2: Construct a repeating array given an array and N = 3
original_array = np.array([1, 2, 3, 4])
N = 3
repeated_array = np.tile(original_array, N)
print("Task 2: Repeated Array\n", repeated_array)

# Task 3: Create an array of repeated elements
element = 3
repetitions = 4
repeated_elements = np.repeat(element, repetitions)
print("Task 3: Repeated Elements\n", repeated_elements)

# Task 4: Create a 10x10 array of zeros framed by ones
framed_array = np.zeros((10, 10))
framed_array[0, :] = 1
framed_array[-1, :] = 1
framed_array[:, 0] = 1
framed_array[:, -1] = 1
print("Task 4: Framed Array\n", framed_array)

# Task 5: Create an 8x8 checkerboard pattern array
checkerboard_array = np.zeros((8, 8), dtype=int)
checkerboard_array[1::2, ::2] = 1
checkerboard_array[::2, 1::2] = 1
print("Task 5: Checkerboard Array\n", checkerboard_array)

# Task 6: Create an array of size n×n, where the position (i, j) equals i+j
n = 5  # Example size
ij_matrix = np.add.outer(range(n), range(n))
print("Task 6: IJ Matrix\n", ij_matrix)

# Task 7: Create a random 5×5 array and sort rows based on the second column
random_matrix = np.random.rand(5, 5)
sorted_matrix = random_matrix[random_matrix[:, 1].argsort()]
print("Task 7: Sorted Random Matrix\n", sorted_matrix)

# Task 8: Calculate the eigenvalues and eigenvectors of a matrix
matrix_for_eigen = np.array([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(matrix_for_eigen)
print("Task 8: Eigenvalues\n", eigenvalues)
print("Task 8: Eigenvectors\n", eigenvectors)

# Task 9: Compute derivatives
x = sp.symbols('x')
function = 0.5 * x**2 + 5 * x + 4
derivative_sympy = sp.diff(function, x)
coefficients = [0.5, 5, 4]
p = np.poly1d(coefficients)
derivative_numpy = p.deriv()
print("Task 9: Derivative with SymPy\n", derivative_sympy)
print("Task 9: Derivative with NumPy\n", derivative_numpy)

# Task 10: Calculate integrals
function_exp = sp.exp(-x)
indefinite_integral = sp.integrate(function_exp, x)
definite_integral = sp.integrate(function_exp, (x, 0, 1))
print("Task 10: Indefinite Integral\n", indefinite_integral)
print("Task 10: Definite Integral\n", definite_integral)

# Task 11: Plotting a cardioid
theta = np.linspace(0, 2 * np.pi, 1000)
r = 1 - np.sin(theta)
plt.figure(figsize=(6, 6))
plt.polar(theta, r, label='Cardioid r = 1 - sin(θ)')
plt.title('Cardioid in Polar Coordinates')
plt.legend()

# Task 12: Generate and plot normal distribution
V = 0  # Mean
D = 1  # Variance
sigma = np.sqrt(D)
normal_random_numbers = np.random.normal(V, sigma, 1000)
plt.figure()
plt.hist(normal_random_numbers, bins=30, alpha=0.75, color='blue', label='Histogram of Normal Distribution')
plt.title('Normal Distribution (mean=0, variance=1)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

plt.show()
