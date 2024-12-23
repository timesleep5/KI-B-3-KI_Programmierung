from z3 import *
from examples.utils import unique_solution

x1, x2, x3, x4 = Bools('x1 x2 x3 x4')

# also possible: t1 = Or(Or(x1, Not(x2)), Not(x3))
# also possible: t1 = Or([x1, Not(x2), Not(x3)])
t1 = Or(x1, Not(x2), Not(x3))
t2 = Or(Not(x1), x4)
t3 = Or(x2, Not(x4))

cond = And(t1, t2, t3)

solver = Solver()
solver.add(cond)
# possible as well:
# solver.add(t1)
# solver.add(t2)
# solver.add(t3)
# or
# solver.add([t1, t2, t3])


print('is it satifiable?', solver.check())
model = solver.model()
print('model:', model)
print('model of x1:', model[x1])
solver.add(x1 != model[x1])
print('model with a different x1:', solver)

# saves the current state
solver.push()

# temporarily add another condition
solver.add(x1 != model[x1])

# restores the state of push()
solver.pop()

print('is the model unique?', unique_solution(solver, [x1, x2, x3, x4]))
