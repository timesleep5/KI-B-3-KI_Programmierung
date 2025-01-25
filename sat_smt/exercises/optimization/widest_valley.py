from z3 import *

from sat_smt.utils import print_if_solvable

values = [3, 2, 1, 2, 3, 2, 1, 2]
N = len(values)

start, end = Ints('start end')
valley_width = Int('valley_width')

bounds = And([0 <= start, start <= end, end < N])
valley = And([
    Implies(
        And([start <= i, i <= end, start_i == start, end_i == end]),
        And([values[i] <= values[start_i], values[i] <= values[end_i]])
    )
    for i in range(N)
    for start_i in range(N)
    for end_i in range(N)
])
valley_width_rule = valley_width == end - start

rule = And([bounds, valley, valley_width_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(valley_width)
print_if_solvable(solver)
