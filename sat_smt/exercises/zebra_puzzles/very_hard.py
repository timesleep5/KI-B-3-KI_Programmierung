from z3 import *

from sat_smt.utils import print_if_solvable

p1, p2, p3, p4, p5 = Ints('p1 p2 p3 p4 p5')
positions = [p1 == 1, p2 == 2, p3 == 3, p4 == 4, p5 == 5]

black, green, orange, red, white = Ints('black green orange red white')
ivan, matthew, oscar, timothy, xavier = Ints('Ivan Matthew Oscar Timothy Xavier')
courthouse, library, skyscraper, theater, university = Ints('courthouse library skyscraper theater university')
conan, laika, nipon, pantex, syno = Ints('conan laika nipon pantex syno')
dutch, german, greek, irish, peruvian = Ints('Dutch German Greek Irish Peruvian')
y25, y35, y40, y55, y60 = Ints('y25 y35 y40 y55 y60')

c1 = irish == y60
c2 = skyscraper == xavier - 1
c3 = peruvian == y55
c4 = Or([red == p1, red == p5])
c5 = white < irish
c6 = german == y25
c7 = green == university
c8 = greek > white
c9 = timothy == library + 1
c10 = black == xavier+1
c11 = Abs(y55 - library) == 1
c12 = green == y35

c13 = Abs(oscar - green) == 1
c14 = nipon == y60
c15 = Abs(library - university) == 1
c16 = syno == peruvian
c17 = black == theater
c18 = white < y35
c19 = laika == y25
c20 = matthew == xavier + 1
c21 = xavier == conan
c22 = And([y40 < syno, syno < irish])

constraints = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22]

bags = [black, green, orange, red, white]
names = [ivan, matthew, oscar, timothy, xavier]
buildings = [courthouse, library, skyscraper, theater, university]
nationalities = [dutch, german, greek, irish, peruvian]
ages = [y25, y35, y40, y55, y60]
all = bags + names + buildings + nationalities + ages

ranges = [And([p1 <= x, x <= p5]) for x in all]
distinct = [Distinct(values) for values in [bags, names, buildings, nationalities, ages]]

rule = And(positions + constraints + ranges + distinct)
solver = Solver()
solver.add(rule)
print_if_solvable(solver)
