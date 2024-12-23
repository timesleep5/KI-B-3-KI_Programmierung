from z3 import *

a, b, c, x = Reals('a b c x')
equation = b ** 2 * x ** 2 + (b ** 2 + c ** 2 - a ** 2) * x + c ** 2 == 0
a_greater_zero = a > 0
b_greater_zero = b > 0
c_greater_zero = c > 0
triangle_inequality_1 = a + b > c
triangle_inequality_2 = b + c > a
triangle_inequality_3 = c + a > b

solver = Solver()
solver.add(equation)
solver.add(a_greater_zero, b_greater_zero, c_greater_zero)
solver.add(triangle_inequality_1, triangle_inequality_2, triangle_inequality_3)

print(solver.check())
