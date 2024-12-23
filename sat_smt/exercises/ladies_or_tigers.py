from z3 import *

from sat_smt.utils import print_if_solvable


def solve(rule):
    solver = Solver()
    solver.add(rule)
    print_if_solvable(solver)


lady_in_room_1, lady_in_room_2 = Bools("lady_in_room_1 lady_in_room_2")


class Day1:
    def trials(self):
        print('Day 1')
        self.trial_1()
        self.trial_2()
        self.trial_3()

    @staticmethod
    def trial_1():
        print('\nTrial 1')
        sign_1 = And(lady_in_room_1, Not(lady_in_room_2))
        sign_2 = lady_in_room_1 != lady_in_room_2
        rule = sign_1 != sign_2
        solve(rule)

    @staticmethod
    def trial_2():
        print('\nTrial 2')
        sign_1 = Or(lady_in_room_1, lady_in_room_2)
        sign_2 = Not(lady_in_room_1)
        rule = sign_1 == sign_2
        solve(rule)

    @staticmethod
    def trial_3():
        print('\nTrial 3')
        sign_1 = Or(Not(lady_in_room_1), lady_in_room_2)
        sign_2 = lady_in_room_1
        rule = sign_1 == sign_2
        solve(rule)


class Day2:
    def trials(self):
        print('Day 2')
        self.trial_4()
        self.trial_5()
        self.trial_6()
        self.trial_7()
        self.trial_8()

    @staticmethod
    def trial_4():
        print('\nTrial 4')
        sign_1 = And(lady_in_room_1, lady_in_room_2)
        sign_2 = And(lady_in_room_1, lady_in_room_2)
        rule = And(lady_in_room_1 == sign_1, lady_in_room_2 != sign_2)
        solve(rule)

    @staticmethod
    def trial_5():
        print('\nTrial 5')
        sign_1 = Or(lady_in_room_1, lady_in_room_2)
        sign_2 = lady_in_room_1
        rule = And(lady_in_room_1 == sign_1, lady_in_room_2 != sign_2)
        solve(rule)

    @staticmethod
    def trial_6():
        print('\nTrial 6')
        sign_1 = lady_in_room_1 == lady_in_room_2
        sign_2 = lady_in_room_1
        rule = And(lady_in_room_1 == sign_1, lady_in_room_2 != sign_2)
        solve(rule)

    @staticmethod
    def trial_7():
        print('\nTrial 7')
        sign_1 = lady_in_room_1 != lady_in_room_2
        sign_2 = lady_in_room_1
        rule = And(lady_in_room_1 == sign_1, lady_in_room_2 != sign_2)
        solve(rule)

    @staticmethod
    def trial_8():
        print('\nTrial 8')
        sign_a_1 = Not(lady_in_room_1)
        sign_a_2 = Not(lady_in_room_2)
        sign_b = Not(Or(lady_in_room_1, lady_in_room_2))
        rule = Or([And([lady_in_room_1 == sign_a_1, lady_in_room_2 != sign_b]),
                   And([lady_in_room_1 == sign_b, lady_in_room_2 != sign_a_2])])
        solve(rule)


if __name__ == '__main__':
    day = Day2()
    day.trials()
