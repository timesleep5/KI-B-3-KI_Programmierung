from search.exercises.ionescu_search import search, bfs_frontier

start = tuple()
N = 8


def is_goal(state):
    return len(state) == N


def successors(state):
    return [
        set_row(state, row)
        for row in range(N)
        if allowed(state, row)
    ]


def set_row(state, row):
    return tuple(state + (row,))


def allowed(state, current_row):
    current_col = len(state)
    forbidden = set(state) | set(
        diag
        for col, row in enumerate(state)
        for diag in (row + (current_col - col), row - (current_col - col))
    )
    return current_row not in forbidden


print(search((0,), bfs_frontier, is_goal, successors))
