from z3 import *

from sat_smt.utils import print_if_solvable

without_function = False

ws = [1, 2, 3]
vs = [1, 3, 5]
Max = 8

N = len(ws)
solver = Optimize()

if without_function:
    ns = [Int(f"ns[{i}]") for i in range(N)]
    ns_range = [ns[i] >= 0 for i in range(N)]
    weight = Int("weight")
    tot_weight = Sum([ns[i] * ws[i] for i in range(N)]) == weight
    max_weight = weight <= Max

    value = Int("value")
    tot_value = Sum([ns[i] * vs[i] for i in range(N)]) == value

    solver.add(ns_range)
    solver.add(tot_weight)
    solver.add(max_weight)
    solver.add(tot_value)
    solver.maximize(value)
else:
    ns = Function("ns", IntSort(), IntSort())
    ns_range = [ns(i) >= 0 for i in range(N)]
    max_weight = Sum([ns(i) * ws[i] for i in range(N)]) <= Max

    solver.add(ns_range)
    solver.add(max_weight)
    solver.maximize(Sum([ns(i) * vs[i] for i in range(N)]))

print_if_solvable(solver)
