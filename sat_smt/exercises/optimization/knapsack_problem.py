from z3 import *

from sat_smt.utils import print_if_solvable

max_capacity = 8
weights = [1, 2, 3]
values = [1, 3, 5]
N = len(weights)

counts = [Int(f'count_of_{i}') for i in range(N)]
value = Int('value')
weight = Int('weight')

bounds = And([0 <= counts[i] for i in range(N)])
value_rule = Sum([counts[i] * values[i] for i in range(N)]) == value
weight_rule = Sum([counts[i] * weights[i] for i in range(N)]) <= max_capacity

rule = And([bounds, value_rule, weight_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(value)
print_if_solvable(solver)
