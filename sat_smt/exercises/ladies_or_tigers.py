from z3 import *

from sat_smt.utils import print_if_solvable, unique_solution


def solve(rule):
    solver = Solver()
    solver.add(rule)
    print_if_solvable(solver)
    return solver


lady_in_room_1, lady_in_room_2, lady_in_room_3 = Bools("lady_in_room_1 lady_in_room_2 lady_in_room_3")


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


# noinspection DuplicatedCode
class Day3:
    def trials(self):
        print('Day 3')
        self.trial_9()
        self.trial_10()
        self.trial_11()

    @staticmethod
    def trial_9():
        print('\nTrial 9')
        sign_1 = Not(lady_in_room_1)
        sign_2 = lady_in_room_2
        sign_3 = Not(lady_in_room_2)

        at_least_one_lady = Or([lady_in_room_1, lady_in_room_2, lady_in_room_3])
        at_most_one_lady = And([
            Implies(lady_in_room_1, Not(lady_in_room_2)),
            Implies(lady_in_room_1, Not(lady_in_room_3)),
            Implies(lady_in_room_2, Not(lady_in_room_3))
        ])
        exactly_one_lady = And([at_least_one_lady, at_most_one_lady])

        at_most_one_sign_true = Sum(
            [1 for sign in [sign_1 == lady_in_room_1, sign_2 == lady_in_room_2, sign_3 == lady_in_room_3] if
             sign is True]
        ) <= 1

        rule = And([exactly_one_lady, at_most_one_sign_true])
        solve(rule)

    @staticmethod
    def trial_10():
        print('\nTrial 10')
        sign_1 = Not(lady_in_room_2)
        sign_2 = Not(lady_in_room_2)
        sign_3 = Not(lady_in_room_1)

        at_least_one_lady = Or([lady_in_room_1, lady_in_room_2, lady_in_room_3])
        at_most_one_lady = And([
            Implies(lady_in_room_1, Not(lady_in_room_2)),
            Implies(lady_in_room_1, Not(lady_in_room_3)),
            Implies(lady_in_room_2, Not(lady_in_room_3))
        ])
        exactly_one_lady = And([at_least_one_lady, at_most_one_lady])

        room_with_lady_has_correct_sign = And([
            Implies(lady_in_room_1, sign_1),
            Implies(lady_in_room_2, sign_2),
            Implies(lady_in_room_3, sign_3)
        ])

        one_of_other_signs_is_false = Not(And([sign_1, sign_2, sign_3]))

        rule = And([exactly_one_lady, room_with_lady_has_correct_sign, one_of_other_signs_is_false])
        solve(rule)

    @staticmethod
    def trial_11():
        print('\nTrial 11')

        room_1, room_2, room_3 = Ints('room_1 room_2 room_3')
        lady, tiger, empty = Ints('lady tiger empty')
        states = And([lady == 1, tiger == 2, empty == 3])

        sign_1 = room_3 == empty
        sign_2 = room_1 == tiger
        sign_3 = room_3 == empty

        sign_with_lady_true = And([
            Implies(room_1 == lady, sign_1),
            Implies(room_2 == lady, sign_2),
            Implies(room_3 == lady, sign_3),
        ])

        sign_with_tiger_false = And([
            Implies(room_1 == tiger, Not(sign_1)),
            Implies(room_2 == tiger, Not(sign_2)),
            Implies(room_3 == tiger, Not(sign_3)),
        ])

        rooms = [room_1, room_2, room_3]
        one_of_each = And([
            Or([room == lady for room in rooms]),
            Or([room == tiger for room in rooms]),
            Or([room == empty for room in rooms]),
        ])

        rule = And([states, sign_with_lady_true, sign_with_tiger_false, one_of_each])
        solve(rule)


class Day4:
    def trials(self):
        print('Day 4')
        self.trial_12()

    @staticmethod
    def trial_12():
        print('\nTrial 12')

        lady, tiger, empty = Ints('lady tiger empty')
        states = And([lady == 1, tiger == 2, empty == 3])

        room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9 = Ints(
            'room_1 room_2 room_3 room_4 room_5 room_6 room_7 room_8 room_9')
        rooms = [room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9]

        sign_1 = And([Implies(room == lady, i % 2 == 0) for i, room in enumerate(rooms)])
        sign_2 = room_2 == empty
        sign_4 = Not(sign_1)
        sign_5 = Xor(sign_2, sign_4)
        sign_7 = room_1 != lady
        sign_3 = Xor(sign_5, Not(sign_7))
        sign_6 = Not(sign_3)
        sign_8 = And([room_8 == tiger, room_9 == empty])
        sign_9 = And([room_9 == tiger, Not(sign_6)])

        signs = [sign_1, sign_2, sign_3, sign_4, sign_5, sign_6, sign_7, sign_8, sign_9]

        room_states = And([
            And([lady <= room, room <= empty]) for room in rooms
        ])

        sign_with_lady_true = And([
            Implies(room == lady, signs[number]) for number, room in enumerate(rooms)
        ])

        sign_with_tiger_false = And([
            Implies(room == tiger, Not(signs[number])) for number, room in enumerate(rooms)
        ])

        only_one_lady = Sum([
            room == lady for room in rooms
        ]) == 1

        room_8_hint = room_8 != empty

        rule = And([states, room_states, sign_with_lady_true, sign_with_tiger_false, only_one_lady, room_8_hint])
        solver = solve(rule)
        unique_solution(solver, rooms)


if __name__ == '__main__':
    day = Day4()
    day.trials()
