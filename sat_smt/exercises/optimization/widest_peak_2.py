from z3 import *

from sat_smt.utils import print_if_solvable

values = [3, 2, 1, 2, 2, 3, 2, 1, 2]
N = len(values)

start, peak, end = Ints('start peak end')
width = Int('width')

width_rule = end - start == width
bounds = And([0 <= start, start <= peak, peak <= end, end < N])
increasing_rule = And([Implies(And([start <= i, i < peak]), values[i] <= values[i + 1]) for i in range(N - 1)])
decreasing_rule = And([Implies(And([peak <= i, i < end]), values[i] >= values[i + 1]) for i in range(N - 1)])

solver = Optimize()
solver.add(width_rule)
solver.add(bounds)
solver.add(increasing_rule)
solver.add(decreasing_rule)
solver.maximize(width)
print_if_solvable(solver)
