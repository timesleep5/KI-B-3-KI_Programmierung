from z3 import *

from sat_smt.utils import print_if_solvable

american, british, canadian, irish = Ints('american british canadian irish')
butterflies, dolphins, horses, turtles = Ints('butterflies dolphins horses turtles')
bowling, handball, swimming, tennis = Ints('bowling handball swimming tennis')
black, blue, red, white = Ints('black blue red white')

nationalities = [american, british, canadian, irish]
pets = [butterflies, dolphins, horses, turtles]
sports = [bowling, handball, swimming, tennis]
colors = [black, blue, red, white]

distinct = And([Distinct(xs) for xs in [nationalities, pets, sports, colors]])
bounds = And([And([1 <= x, x <= 4]) for x in nationalities + pets + sports + colors])

c1 = Abs(bowling - swimming) == 3
c2 = handball + 2 == irish
c3 = black == 2
c4 = horses + 2 == red
c5 = american == turtles - 1
c6 = bowling > tennis
c7 = handball + 2 == white

constraints = [c1, c2, c3, c4, c5, c6, c7]

rule = And([distinct, bounds] + constraints)
solver = Solver()
solver.add(rule)
print_if_solvable(solver)
