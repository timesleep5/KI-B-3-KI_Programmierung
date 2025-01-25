from z3 import *

from sat_smt.utils import print_if_solvable

max_capacity = 8
weights = [1, 2, 3]
values = [1, 3, 5]
N = len(weights)

value = Int('value')

count_f = Function("ns", IntSort(), IntSort())
fill_count_f = And([count_f(i) >= 0 for i in range(N)])
max_weight_rule = Sum([count_f(i) * weights[i] for i in range(N)]) <= max_capacity
value_rule = Sum([count_f(i) * values[i] for i in range(N)]) == value

rule = And([fill_count_f, max_weight_rule, value_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(value)
print_if_solvable(solver)
