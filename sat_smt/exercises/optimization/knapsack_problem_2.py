from z3 import *

from sat_smt.utils import print_if_solvable

weights = [1, 2, 3]
values = [1, 3, 5]
max_capacity = 8
N = len(values)

counts = [Int(f'of_{i}') for i in range(N)]

weight, value = Ints('weight value')

weight_rule = Sum([weights[i] * counts[i] for i in range(N)]) == weight
value_rule = Sum([values[i] * counts[i] for i in range(N)]) == value
max_weight_rule = weight <= max_capacity
bounds = And([counts[i] >= 0 for i in range(N)])

solver = Optimize()
solver.add(weight_rule)
solver.add(value_rule)
solver.add(max_weight_rule)
solver.add(bounds)
solver.maximize(value)
print_if_solvable(solver)
