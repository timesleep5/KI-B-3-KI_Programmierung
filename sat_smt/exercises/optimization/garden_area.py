from z3 import *

from sat_smt.utils import print_if_solvable

wire_length = 200
x, y = Ints('x y')
area = Int('area')

bounds = And([And([0 <= z, z < wire_length/2]) for z in [x, y]])
wire_length_rule = 2 * x + 2 * y <= wire_length
area_rule = x * y == area

rule = And([wire_length_rule, area_rule, bounds])
solver = Optimize()
solver.add(rule)
solver.maximize(area)
print_if_solvable(solver)
