from z3 import *

from sat_smt.utils import print_if_solvable

cs = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 1]]

slots = [Int(f'committee_{i}') for i in range(len(cs))]

bounds = And([And([1 <= x, x <= len(cs)]) for x in slots])
no_interceptions = And([
    Implies(
        And([slots[i] == slots[j], i != j]),
        len(cs[i]) + len(cs[j]) == len(set(cs[i] + cs[j]))
    )
    for i in range(len(slots))
    for j in range(len(slots))
])

number_of_slots = Int('number_of_slots')
number_of_slots_rule = len(set(
    i
    for i in range(1, len(cs) + 1)
    for j in range(len(slots))
    if slots[j] == i
)) == number_of_slots


rule = And([bounds, no_interceptions, number_of_slots_rule])
o = Optimize()
o.add(rule)
o.minimize(number_of_slots)

print_if_solvable(o)
