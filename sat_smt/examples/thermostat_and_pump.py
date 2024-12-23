from z3 import *
from sat_smt.utils import unique_solution

p, t, w = Bools('pump_broken thermostat_broken warning_light_on')

# SAT form:
first = Or(t, p)
second = Or(Not(t), p)
third = Or(Not(p), Not(w), Not(t))
fourth = w

# SMT form:
second = Implies(t, p)
third = Implies(And(p, w), Not(t))

solver = Solver()
solver.add(first, second, third, fourth)
print(solver.check())
print(solver.model())
print(unique_solution(solver, [t, p, w]))
