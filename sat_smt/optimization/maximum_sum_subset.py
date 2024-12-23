from z3 import *

# we are looking for a SEGMENT with start and end within which the sum of the elements is maximal
xs = [2, -3, 4, -1, 3]
N = len(xs)
left, right = Ints('left right')
left_right_range = And([0 <= left, left <= right, right < N])
segsum = Int('segsum')
segsum_value = Sum([If(left <= i < right, xs[i], 0) for i in range(N)]) == segsum

solver = Optimize()
solver.add(left_right_range)
solver.add(segsum_value)
solver.maximize(segsum_value)

if solver.check() == sat:
    model = solver.model()
    start = model[left].as_long()
    end = model[right].as_long() + 1
    print([xs[i] for i in range(start, end)])
