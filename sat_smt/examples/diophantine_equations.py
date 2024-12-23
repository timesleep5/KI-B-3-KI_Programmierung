from z3 import *
from sat_smt.utils import unique_solution

n, m, p = Ints('n m p')
solver = Solver()
solver.add(
    2 * m == 10,
    m * n + n == 12,
    m * n - p * m == m
)
print(solver.check())
print(solver.model())
print(unique_solution(solver, [n, m, p]))
