import math
from typing import Callable


class Term:
    def evaluate(self, env) -> float:
        pass

    def differentiate(self, variable: str) -> 'Term':
        pass

    def simplify(self) -> 'Term':
        return self

    def variables(self) -> list:
        pass

    def __add__(self, other) -> 'Term':
        if isinstance(other, int) or isinstance(other, float):
            other = Number(other)
        if isinstance(other, str):
            other = Variable(other)

        if isinstance(other, Term):
            return Plus(self, other)

    def __sub__(self, other) -> 'Term':
        if isinstance(other, int) or isinstance(other, float):
            other = Number(other)
        if isinstance(other, str):
            other = Variable(other)

        if isinstance(other, Term):
            return Diff(self, other)

    def __mul__(self, other) -> 'Term':
        if isinstance(other, int) or isinstance(other, float):
            other = Number(other)
        if isinstance(other, str):
            other = Variable(other)

        if isinstance(other, Term):
            return Mul(self, other)

    def __div__(self, other) -> 'Term':
        if isinstance(other, int) or isinstance(other, float):
            other = Number(other)
        if isinstance(other, str):
            other = Variable(other)

        if isinstance(other, Term):
            return Div(self, other)

    def __truediv__(self, other) -> 'Term':
        if isinstance(other, int) or isinstance(other, float):
            other = Number(other)
        if isinstance(other, str):
            other = Variable(other)

        if isinstance(other, Term):
            return Div(self, other)


class Number(Term):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        if isinstance(other, Number):
            return self.value == other.value
        return False

    def evaluate(self, env) -> float:
        return self.value

    def differentiate(self, variable: str) -> Term:
        return Number(0)

    def variables(self) -> list:
        return []


class Variable(Term):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __eq__(self, other) -> bool:
        if isinstance(other, Variable):
            return self.name == other.name
        return False

    def evaluate(self, env) -> float:
        return env[self.name]

    def differentiate(self, variable: str) -> Term:
        if self.name == variable:
            return Number(1)
        return Number(0)

    def variables(self) -> list:
        return [self.name]


class BinaryOperation(Term):
    name: str
    operation: Callable

    def __init__(self, left: Term, right: Term):
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.left} {self.name} {self.right})'

    def __eq__(self, other):
        if isinstance(other, BinaryOperation):
            return self.name == other.name and \
                self.left == other.left and \
                self.right == other.right
        return False

    def evaluate(self, env):
        left = self.left.evaluate(env)
        right = self.right.evaluate(env)
        return self.operation(left, right)

    def variables(self) -> list:
        return self.left.variables() + self.right.variables()


class Plus(BinaryOperation):
    name = '+'
    operation = lambda self, x, y: x + y

    def differentiate(self, variable: str) -> Term:
        left = self.left.differentiate(variable)
        right = self.right.differentiate(variable)
        return left + right

    def simplify(self) -> Term:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.variables() == [] and right.variables() == []:
            return Number(left.evaluate({}) + right.evaluate({}))
        if left.variables() == []:
            left = Number(left.evaluate({}))
        if right.variables() == []:
            right = Number(right.evaluate({}))

        if left == Number(0):
            return right
        if right == Number(0):
            return left

        return left + right


class Diff(BinaryOperation):
    name = '-'
    operation = lambda self, x, y: x - y

    def differentiate(self, variable: str) -> Term:
        left = self.left.differentiate(variable)
        right = self.right.differentiate(variable)
        return left - right

    def simplify(self) -> Term:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.variables() == [] and right.variables() == []:
            return Number(left.evaluate({}) - right.evaluate({}))
        if left.variables() == []:
            left = Number(left.evaluate({}))
        if right.variables() == []:
            right = Number(right.evaluate({}))

        if left == Number(0):
            return right
        if right == Number(0):
            return left

        return left - right


class Mul(BinaryOperation):
    name = '*'
    operation = lambda self, x, y: x * y

    def differentiate(self, variable: str) -> Term:
        left = self.left.differentiate(variable) * self.right
        right = self.left * self.right.differentiate(variable)
        return Plus(left, right)

    def simplify(self) -> Term:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.variables() == [] and right.variables() == []:
            return Number(left.evaluate({}) * right.evaluate({}))
        if left.variables() == []:
            left = Number(left.evaluate({}))
        if right.variables() == []:
            right = Number(right.evaluate({}))

        if left == Number(0) or right == Number(0):
            return Number(0)
        if left == Number(1):
            return right
        if right == Number(1):
            return left

        return left * right


class Div(BinaryOperation):
    name = '/'
    operation = lambda self, x, y: x / y

    def differentiate(self, variable: str) -> Term:
        numerator_left = self.left.differentiate(variable) * self.right
        numerator_right = self.left * self.right.differentiate(variable)
        numerator = numerator_left - numerator_right
        denominator = self.right * self.right  # todo change to pow
        return numerator / denominator

    def simplify(self) -> Term:
        left = self.left.simplify()
        right = self.right.simplify()

        if left.variables() == [] and right.variables() == []:
            return Number(left.evaluate({}) * right.evaluate({}))
        if left.variables() == []:
            left = Number(left.evaluate({}))
        if right.variables() == []:
            right = Number(right.evaluate({}))

        if right == Number(0):
            raise ZeroDivisionError(f'{left}/{right} not allowed)')
        if right == Number(1):
            return left
        if left == Number(0):
            return Number(0)

        return left / right


class Pow(BinaryOperation):
    name = '**'
    operation = lambda self, x, y: x ** y

    def differentiate(self, variable: str) -> Term:
        base = self.left.simplify()
        power = self.right.simplify()
        # todo

    def simplify(self) -> Term:
        pass
        # todo


class UnaryOperation(Term):
    name: str
    operation: Callable

    def __init__(self, argument: Term):
        self.argument = argument

    def __str__(self):
        return f'{self.name}{self.argument}'

    def __eq__(self, other):
        if isinstance(other, UnaryOperation):
            return self.name == other.name and \
                self.argument == other.argument
        return False

    def variables(self) -> list:
        return self.argument.variables()


class Exp(UnaryOperation):
    name = 'exp'
    operation = lambda self, x: math.exp(x)

    def simplify(self) -> Term:
        argument = self.argument.simplify()
        if argument.variables() == []:
            return Number(math.exp(argument.evaluate({})))

        return Exp(argument)

    def differentiate(self, variable: str) -> Term:
        return self * self.argument.differentiate(variable)

    def evaluate(self, env):
        return math.exp(self.argument.evaluate(env))


class Neg(UnaryOperation):
    name = '-'
    operation = lambda self, x: -x

    def simplify(self) -> Term:
        argument = self.argument.simplify()
        if argument.variables() == []:
            return Number(-argument.evaluate({}))

        return Neg(argument)

    def differentiate(self, variable: str) -> Term:
        return Neg(self.argument.differentiate(variable))

    def evaluate(self, env):
        return -self.argument.evaluate(env)


x = Variable('x')

sigmoid = Number(1) / (Number(1) + Exp(Neg(x)))
print(sigmoid.differentiate('x').simplify())
