from z3 import *

from sat_smt.utils import print_if_solvable

width = 24
height = 36

cut_off_square_length = Int('cut_off_square_length')
volume = Int('volume')

bounds = And([0 <= cut_off_square_length, cut_off_square_length < min(width, height) / 2])
volume_rule = (width - 2 * cut_off_square_length) * (height - 2 * cut_off_square_length) * cut_off_square_length == volume

rule = And([bounds, volume_rule])
solver = Optimize()
solver.add(rule)
solver.maximize(volume)
print_if_solvable(solver)
