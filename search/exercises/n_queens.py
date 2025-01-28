from dataclasses import dataclass
from typing import List, Tuple

from search.algorithms.depth_first_search import DepthFirstSearch
from search.search import State, Printer

N = 8


@dataclass(frozen=True)
class QueenState(State):
    rows: Tuple[int, ...]

    def is_goal(self) -> bool:
        return len(self.rows) == N

    def next_states(self) -> List['State']:
        states = [
            self._set(row)
            for row in range(N)
            if self._allowed(row)
        ]
        return states

    def _set(self, row):
        new_rows = tuple(self.rows + (row,))
        return QueenState(new_rows)

    def _allowed(self, row):
        current_col = len(self.rows)
        forbidden = set(self.rows) | set(
            diag
            for col, row in enumerate(self.rows)
            for diag in (row + (current_col - col), row - (current_col - col))
        )
        return row not in forbidden

    class _Printer:
        @staticmethod
        def print(rows: Tuple[int, ...]) -> str:
            board = [['.' for _ in range(N)] for _ in range(N)]
            for col, row in enumerate(rows):
                board[row][col] = 'Q'
            return '\n'.join([' '.join(row) for row in board])

    def __repr__(self):
        return self._Printer.print(self.rows)



if __name__ == '__main__':
    start = QueenState((7,))
    search = DepthFirstSearch()
    path = search.search(start)
    Printer.print(path)
