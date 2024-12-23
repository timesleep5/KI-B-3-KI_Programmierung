from z3 import *

xs = [3, 2, 1, 2, 3, 2, 1, 2]
N = len(xs)
l, p, r = Ints("left peak right")
l_p_r_range = And(0 <= l, l <= p, p <= r, r < N)
peak_cond_up = And([
    Implies(And(l <= i, i <= j, j <= p), xs[i] <= xs[j])
    for i in range(N)
    for j in range(i + 1, N)
])  # range(l, p + 1) for j in range(i + 1, p + 1)])
peak_cond_down = And([
    Implies(And(p <= i, i <= j, j <= r), xs[i] >= xs[j])
    for i in range(N)
    for j in range(i + 1, N)
])

solver = Optimize()
solver.add(l_p_r_range)
solver.add(peak_cond_up)
solver.add(peak_cond_down)

solver.maximize(r - l)

if solver.check() == sat:
    model = solver.model()
    start = model[l].as_long()
    end = model[r].as_long() + 1
    print([xs[i] for i in range(start, end)])

# Umformulierungen:
And([If(And(l <= i, i <= j, j <= p), xs[i] <= xs[j], True) for i in range(N) for j in range(i + 1, N)])
And([Implies(And(l <= i, i <= j, j <= p), xs[i] <= xs[j]) for i in range(N) for j in range(i + 1, N)])
And([Or(Not(And(l <= i, i <= j, j <= p), xs[i] <= xs[j])) for i in range(N) for j in range(i + 1, N)])
And([Or(l > i, i > j, j > p, xs[i] <= xs[j]) for i in range(N) for j in range(i + 1, N)])
And([(l > i) | (i > j) | (j > p) | (xs[i] <= xs[j]) for i in range(N) for j in range(i + 1, N)])
