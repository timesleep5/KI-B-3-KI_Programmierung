# 1. reverse
def rev(iterable):
    return iterable[::-1]


# 2.fibonacci
memory = {
    0: 0,
    1: 1
}


def fibonacci(n: int) -> int:
    if n not in memory:
        memory[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memory[n]


# 3. number of shortest paths in x, y grid
def nsp(x: int, y: int) -> int:
    if 1 in (x, y):
        return max(x, y) + 1
    return nsp(x - 1, y) + nsp(x, y - 1)


# 4. number of overall paths
def np(x: int, y: int) -> int:
    pass


# 5. n queens: all solutions of 8 queens on an 8x8 board
def solve():
    pass
