from dataclasses import dataclass
from typing import List, Tuple

from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.search import State, Printer

N = 3


@dataclass(frozen=True)
class TileState(State):
    tiles: Tuple[Tuple[int, ...], ...]
    GOAL = tuple(tuple(N * row + col for col in range(N)) for row in range(N))

    def is_goal(self) -> bool:
        return self.tiles == self.GOAL

    def next_states(self) -> List['State']:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        empty_indexes = self.find_empty()
        states = []
        for dir in dirs:
            switch_row = empty_indexes[0] + dir[0]
            switch_col = empty_indexes[1] + dir[1]
            if 0 <= switch_row < N and 0 <= switch_col < N:
                switchable = [[self.tiles[row][col] for col in range(N)] for row in range(N)]
                switchable[switch_row][switch_col], switchable[empty_indexes[0]][empty_indexes[1]] = \
                    switchable[empty_indexes[0]][empty_indexes[1]], switchable[switch_row][switch_col]
                unswitchable = tuple(tuple(row) for row in switchable)
                states.append(TileState(unswitchable))
        return states

    def find_empty(self) -> Tuple[int, int]:
        for row in range(N):
            for col in range(N):
                if self.tiles[row][col] == 0:
                    return row, col


if __name__ == '__main__':
    start = TileState((
        (7, 2, 4),
        (5, 0, 6),
        (8, 3, 1)
    ))
    search = BreadthFirstSearch()
    path = search.search(start)
    Printer.print(path)
