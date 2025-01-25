from z3 import *

from sat_smt.utils import print_if_solvable

N = 8

cols = [i for i in range(N)]
rows = [Int(f'rows[{i}]') for i in range(N)]

bounds = [And([0 <= rows[i], rows[i] < N]) for i in range(N)]
not_same_row = Distinct(rows)
not_same_diagonal = And([Abs(rows[i] - rows[j]) != Abs(cols[i] - cols[j]) for i in range(N) for j in range(N) if i != j])

rule = And([not_same_row, not_same_diagonal] + bounds)
solver = Solver()
solver.add(rule)
print_if_solvable(solver)
