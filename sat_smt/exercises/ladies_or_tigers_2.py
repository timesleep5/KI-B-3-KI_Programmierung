from z3 import *

from sat_smt.utils import print_if_solvable

lady_in_room_1, lady_in_room_2 = Bools('lady_in_room_1 lady_in_room_2')


def solve(rule):
    solver = Solver()
    solver.add(rule)
    print_if_solvable(solver)


def trial_1():
    sign_1 = And([lady_in_room_1, Not(lady_in_room_2)])
    sign_2 = Xor(lady_in_room_1, lady_in_room_2)
    solve(sign_1 != sign_2)


def trial_2():
    sign_1 = Or([lady_in_room_1, lady_in_room_2])
    sign_2 = Not(lady_in_room_1)
    solve(sign_1 == sign_2)


def trial_3():
    sign_1 = Xor(Not(lady_in_room_1), lady_in_room_2)
    sign_2 = lady_in_room_1
    solve(sign_1 == sign_2)


def trial_4():
    sign_1 = And([lady_in_room_1, lady_in_room_2])
    sign_2 = And([lady_in_room_1, lady_in_room_2])
    solve(And([sign_1 == lady_in_room_1, sign_2 != lady_in_room_2]))


def trial_5():
    sign_1 = Or([lady_in_room_1, lady_in_room_2])
    sign_2 = lady_in_room_1
    solve(And([sign_1 == lady_in_room_1, sign_2 != lady_in_room_2]))


def trial_6():
    sign_1 = lady_in_room_1 == lady_in_room_2
    sign_2 = lady_in_room_1
    solve(And([sign_1 == lady_in_room_1, sign_2 != lady_in_room_2]))


def trial_7():
    sign_1 = lady_in_room_1 != lady_in_room_2
    sign_2 = lady_in_room_1
    solve(And([sign_1 == lady_in_room_1, sign_2 != lady_in_room_2]))



if __name__ == '__main__':
    trial_7()
