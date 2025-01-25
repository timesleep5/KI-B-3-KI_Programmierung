from z3 import *

from sat_smt.utils import print_if_solvable

values = [3, 2, 1, 2, 3, 2, 1, 2]
N = len(values)

start, peak, end = Ints('start peak end')
peak_length = Int('peak_length')

bounds = And([0 <= start, start <= peak, peak <= end, end < N])
increasing_left = And([Implies(And([start <= i, i < peak]), values[i] <= values[i + 1]) for i in range(N - 1)])
decreasing_right = And([Implies(And([peak <= i, i < end]), values[i] >= values[i + 1]) for i in range(N - 1)])
peak_length_rule = peak_length == end - start

rule = And([bounds, increasing_left, decreasing_right, peak_length_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(peak_length)
print_if_solvable(solver)
