from z3 import *

from sat_smt.utils import print_if_solvable

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
values = [-7, -3, -2, 9000, 5, 8]
N = len(values)

indices = [Bool(f'index_{i}') for i in range(N)]
zero_sum = Sum([If(indices[i], values[i], 0) for i in range(N)]) == 0
subset_length = Int('subset_length')
subset_length_rule = Sum(indices) == subset_length

rule = And([zero_sum, subset_length_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(subset_length)
print_if_solvable(solver)
