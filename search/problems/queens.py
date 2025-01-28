from dataclasses import dataclass
from typing import Tuple, override, List

from search.algorithms.a_star_search import AStarSearch
from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.search import State, Printer, Timer

N = 8


@dataclass(frozen=True, repr=False)
class BoardState(State):
    queens: Tuple[int, ...]

    @override
    def is_goal(self) -> bool:
        return len(self.queens) == N

    @override
    def next_states(self) -> List['BoardState']:
        next_states = [self._set(col) for col in range(N) if self._allowed(col)]
        return next_states

    def _set(self, col: int) -> 'BoardState':
        new_queens = tuple(self.queens)
        new_queens += (col,)
        return BoardState(new_queens)

    def _allowed(self, col: int) -> bool:
        current_row = len(self.queens)
        forbidden = set(self.queens) | set(
            diag
            for row, col in enumerate(self.queens)
            for diag in (col + (current_row - row), col - (current_row - row))
        )
        return col not in forbidden

    class _Printer:
        @staticmethod
        def print(queens: Tuple[int, ...]) -> str:
            board = [['.' for _ in range(N)] for _ in range(N)]
            for row, col in enumerate(queens):
                board[row][col] = 'Q'
            return '\n'.join([' '.join(row) for row in board])

    def __repr__(self):
        return self._Printer.print(self.queens)


if __name__ == '__main__':
    start = BoardState((0,))
    breadth_first_search = BreadthFirstSearch()
    a_star_search = AStarSearch(lambda path: -len(path))

    breadth_path = Timer.timer(lambda: breadth_first_search.search(start), 'breadth first search')
    a_star_path = Timer.timer(lambda: a_star_search.search(start), 'A* search (basically depth first by filter)')

    print('Breadth first search path:')
    Printer.print(breadth_path)
    #
    # print('A* search path:')
    # Printer.print(a_star_path)
