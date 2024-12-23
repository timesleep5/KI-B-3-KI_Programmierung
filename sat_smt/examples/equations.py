from z3 import *
from utils import unique_solution

x, y, z = Reals('x y z')

eq1 = x + y + z == 25
eq2 = 5 * x + 3 * y + 2 * z == 0
eq3 = y - z == 6

solver = Solver()
solver.add(eq1, eq2, eq3)
print(solver.check())
print(solver.model())
print(unique_solution(solver, [x, y, z]))
