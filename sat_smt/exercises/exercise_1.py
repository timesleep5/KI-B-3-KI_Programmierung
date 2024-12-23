from z3 import *

Aus, Bra, Ger = Ints("Aus Bra Ger")
Nats = [Aus, Bra, Ger]

Cats, Dogs, Fishes = Ints("Cats Dogs Fishes")
Pets = [Cats, Dogs, Fishes]

Bas, Foo, Socc = Ints("Bas Foo Socc")
Sports = [Bas, Foo, Socc]

Blue, Green, Red = Ints("Blue Green Red")
Cols = [Blue, Green, Red]

All = Nats + Pets + Sports + Cols

interval = [And(x >= 1, x <= 3) for x in All]
distinct = [Distinct(xs) for xs in [Nats, Pets, Sports, Cols]]
conds = [
    Bra != 2,
    Dogs == Bas,
    Red == Foo + 2,
    Fishes == Cats - 1,
    Dogs == Green + 1,
    Ger == 3
]

solver = Solver()
solver.add(interval + distinct + conds)
print(solver.check())
print(solver.model())
