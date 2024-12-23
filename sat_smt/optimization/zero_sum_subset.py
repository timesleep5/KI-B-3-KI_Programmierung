from z3 import *

manual_optimization = False

xs = [-7, -3, -2, 9000, 5, 6, 7]
N = len(xs)
ys = [Bool(f'ys[{i}]') for i in range(N)]
zero_sum = Sum([If(ys[i], xs[i], 0) for i in range(N)]) == 0
length = Int("length")
length_computation = Sum([If(ys[i], 1, 0) for i in range(N)]) == length


def print_model(model):
    print([xs[i] for i in range(N) if model[ys[i]]])


if manual_optimization:
    solver = Solver()
    solver.add(zero_sum)
    solver.add(length_computation)
    solver.push()

    target = 0
    solver.add(length > target)

    model = None

    while solver.check() == sat:
        model = solver.model()
        l = model[length]
        solver.pop()
        target = l
        solver.add(length > target)

    print_model(model)
    
else:
    solver = Optimize()
    solver.add(zero_sum)
    solver.add(length_computation)

    solver.maximize(length)

    if solver.check() == sat:
        model = solver.model()
        print_model(model)
