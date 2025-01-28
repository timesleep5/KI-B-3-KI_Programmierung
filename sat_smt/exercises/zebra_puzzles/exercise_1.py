from z3 import *

from sat_smt.utils import print_if_solvable

australian, brazilian, german = Ints('australian brazilian german')
cats, dogs, fishes = Ints('cats dogs fishes')
basketball, football, soccer = Ints('basketball football soccer')
blue, green, red = Ints('blue green red')
nationalities = [australian, brazilian, german]
pets = [cats, dogs, fishes]
sports = [basketball, football, soccer]
colors = [blue, green, red]

distinct = And([Distinct(xs) for xs in [nationalities, pets, sports, colors]])
bounds = And([And([1 <= x, x <= 3]) for x in nationalities + pets + sports + colors])

c1 = brazilian != 2
c2 = dogs == basketball
c3 = football == red - 2
c4 = fishes == cats - 1
c5 = dogs == green + 1
c6 = german == 3

constraints = [c1, c2, c3, c4, c5, c6]
rule = And([distinct, bounds] + constraints)
solver = Solver()
solver.add(rule)
print_if_solvable(solver)