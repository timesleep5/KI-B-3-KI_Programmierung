from z3 import *

Max = lambda m, n: If(m > n, m, n)

a, b, c = Ints('a b c')
x = Real('x')
y = Int('y')
T = lambda X: X ** 2 + a * X + b

cond = ForAll(a,
              ForAll(b,
                     ForAll(x,
                            ForAll(c,
                                   Implies(
                                       And(
                                           Implies(
                                               T(x) == 0,
                                               Exists(y, x == y),
                                               Exists(x, T(x) == 0)
                                           ),
                                           T(c) == 13
                                       ),
                                       Max(T(c - 1), T(c + 1)) == 28
                                   )
                                   )
                            )
                     )
              )

# much simpler (Nullstellenform):
x1, x2, c = Ints('x1 x2 c')
T = lambda X: (X - x1) * (X - x2)

cond = ForAll(x1,
              ForAll(x2,
                     ForAll(c,
                            Implies(
                                T(c) == 13,
                                Max(T(c - 1), T(c + 1)) == 28
                            )
                            )
                     )
              )
# output: unknown

# even better: show that the opposite is unsat
cond = And(
    T(c) == 13,
    Max(T(c - 1), T(c + 1)) != 28
)
# output: unsat --> proof!

solver = Solver()
solver.add(cond)
print(solver.check())


# continue at VL 3, 00:33:30
