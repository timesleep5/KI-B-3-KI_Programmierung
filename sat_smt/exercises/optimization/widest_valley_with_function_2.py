from z3 import *

from sat_smt.utils import print_if_solvable

values = [3, 2, 1, 2, 3, 2, 1, 2]
N = len(values)

start, end = Ints('start end')
width = Int('width')

valley = Function('valley', IntSort(), IntSort())
fill_valley = And([valley(i) == values[i] for i in range(N)])

valley_definition = And(
    [Implies(And([start <= i, i <= end]), And([values[i] <= valley(start), values[i] <= valley(end)])) for i in
     range(N)])
bounds = And([0 <= start, start <= end, end < N])
width_rule = end - start == width

solver = Optimize()
solver.add(fill_valley)
solver.add(valley_definition)
solver.add(bounds)
solver.add(width_rule)
solver.maximize(width)
print_if_solvable(solver)
