from z3 import *

from sat_smt.utils import print_if_solvable, unique_solution

cost = [4, 8, 3, 7, 2]
stops = [1, 2, 3, 4, 5]
refills = [5, 10, 9, 8, 0]
initial_fuel = 10
N = len(cost)

consumed = Function('consumed', IntSort(), IntSort())
fill_consumed = And([consumed(i) == Sum([cost[j] for j in range(i + 1)]) for i in range(N)])

refills_taken = [Bool(f'at_{i}') for i in stops]
refilled = Function('refilled', IntSort(), IntSort())
fill_refilled = And([refilled(i) == Sum([If(refills_taken[j], refills[j], 0) for j in range(i)]) for i in range(N)])

fuel_levels = Function('fuel_levels', IntSort(), IntSort())
fill_fuel = And([fuel_levels(i) == initial_fuel + refilled(i) - consumed(i) for i in range(N)])
fuel_rule = And([fuel_levels(i) >= 0 for i in range(N)])

stops_total = Int('stops_total')
stops_total_rule = Sum([If(refills_taken[i], 1, 0) for i in range(N)]) == stops_total

rule = And([fill_consumed, fill_refilled, fill_fuel, fuel_rule, stops_total_rule])
o = Optimize()
o.add(rule)
o.minimize(stops_total)
print_if_solvable(o)
unique_solution(o, refills_taken)
