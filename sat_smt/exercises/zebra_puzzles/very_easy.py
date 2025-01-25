from z3 import *

from sat_smt.utils import print_if_solvable

black, yellow, red, orange = Ints('black yellow red orange')
quincy, richard, timothy, ulysses = Ints('quincy richard timothy ulysses')
beard_oil, card_holder, keychain, wallet = Ints('beard_oil card_holder keychain wallet')
accounting, it, r_d, sales = Ints('accounting it r_d sales')
p1, p2, p3, p4 = Ints('p1 p2 p3 p4')
positions = [p1 == 1, p2 == 2, p3 == 3, p4 == 4]

c1 = keychain == p2
c2 = timothy == p2
c3 = Or([yellow == p1, yellow == p4])
c4 = it == p4
c5 = Or([beard_oil == p1, beard_oil == p4])
c6 = orange == p2
c7 = Abs(black - it) == p1

c8 = orange < ulysses
c9 = Abs(red - orange) == 1
c10 = keychain == accounting
c11 = richard == card_holder
c12 = wallet == it
c13 = Abs(sales - ulysses) == 1

shirts = [black, yellow, red, orange]
names = [quincy, richard, timothy, ulysses]
gifts = [beard_oil, card_holder, keychain, wallet]
departments = [accounting, it, r_d, sales]
all = shirts + names + gifts + departments

ranges = [And([p1 <= x, x <= p4]) for x in all]
distinct = [Distinct(values) for values in [shirts, names, gifts, departments]]
conditions = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]

rule = And(positions + conditions + ranges + distinct)
solver = Solver()
solver.add(rule)
print_if_solvable(solver)
