from z3 import *

from sat_smt.utils import print_if_solvable

without_function = False

xs = [3, 2, 1, 2, 3, 2, 1, 2]

N = len(xs)
left, right = Ints('left right')
left_right_range = (0 <= left) & (left <= right) & (right < N)

solver = Optimize()
solver.add(left_right_range)

if without_function:
    valley = And(
        [
            Implies(
                (left <= i) & (i <= right) & (k == left) & (j == right),
                (xs[k] >= xs[i]) & (xs[j] >= xs[i])
            )
            for i in range(N)
            for j in range(i + 1, N)
            for k in range(0, i)
        ]
    )

    solver.add(valley)
else:
    Xs = Function("Xs", IntSort(), IntSort())
    valley = And(
        [
            Implies(
                (left <= i) & (i <= right),
                (Xs(left) >= Xs(i)) & (Xs(right) >= Xs(i))
            )
            for i in range(N)
        ]
    )
    Xs_is_xs = And([Xs(i) == xs[i] for i in range(N)])

    solver.add(valley)
    solver.add(Xs_is_xs)

solver.maximize(right - left)
print_if_solvable(solver)
