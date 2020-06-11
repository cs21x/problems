from approximation import compute_root

poly = (3, -5, 2)
x_0 = 0.1
epsilon = 0.00001
actual = compute_root(poly, x_0, epsilon)
print(round(actual[0], 1)