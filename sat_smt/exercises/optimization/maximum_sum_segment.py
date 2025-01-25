from z3 import *

from sat_smt.utils import print_if_solvable

values = [2, -3, 4, -1, 3]
N = len(values)

start, end = Ints('start end')
bounds = And([0 <= start, start <= end, end < N])
segment_sum = Int('segment_sum')
sum_rule = Sum([If(And([start <= i, i <= end]), values[i], 0) for i in range(N)]) == segment_sum

rule = And([bounds, sum_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(segment_sum)
print_if_solvable(solver)
