from z3 import *

lady_in_room_1, lady_in_room_2 = Bools("lady_in_room_1 lady_in_room_2")
sign_1 = And(lady_in_room_1, Not(lady_in_room_2))
sign_2 = Xor(lady_in_room_1, lady_in_room_2)
cond = Xor(sign_1, sign_2)

solver = Solver()
solver.add(cond)
print(solver.check())
print(solver.model())