from z3 import *

from sat_smt.utils import print_if_solvable

values = [3, 2, 1, 2, 3, 2, 1, 2]
N = len(values)

start, end = Ints('start end')
valley_width = Int('valley_width')

bounds = And([0 <= start, start <= end, end < N])
values_f = Function('values_f', IntSort(), IntSort())
fill_values_f = And([values_f(i) == values[i] for i in range(N)])
valley = And([
    Implies(
        And([start <= i, i <= end]),
        And([values_f(i) <= values_f(start), values_f(i) <= values_f(end)])
    ) for i in range(N)
])
valley_width_rule = valley_width == end - start

rule = And([bounds, valley, fill_values_f, valley_width_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(valley_width)
print_if_solvable(solver)
