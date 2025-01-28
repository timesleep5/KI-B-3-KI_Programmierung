from dataclasses import dataclass
from random import choice
from typing import List, Tuple, override

from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.search import State, Printer

number = 5


@dataclass(frozen=True, repr=False)
class TileState(State):
    GOAL = tuple(tuple(row * number + col for col in range(number)) for row in range(number))
    tiles: Tuple[Tuple[int, ...], ...]

    @override
    def is_goal(self) -> bool:
        return self.tiles == self.GOAL

    @override
    def next_states(self) -> List['TileState']:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        next_states = [self._swapped(d)
                       for d in directions
                       if self._allowed(d)]
        return next_states

    def _zero_position(self) -> Tuple[int, int]:
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                if tile == 0:
                    return i, j

    def _swapped(self, direction: Tuple[int, int]) -> 'TileState':
        zero_row, zero_col = self._zero_position()
        swap_row = zero_row + direction[0]
        swap_col = zero_col + direction[1]
        new_tiles = list(list(row) for row in self.tiles)
        tmp = new_tiles[swap_row][swap_col]
        new_tiles[swap_row][swap_col] = new_tiles[zero_row][zero_col]
        new_tiles[zero_row][zero_col] = tmp
        new_tiles = tuple(tuple(row) for row in new_tiles)
        return TileState(new_tiles)

    def _allowed(self, direction: Tuple[int, int]) -> bool:
        zero_row, zero_col = self._zero_position()
        swap_row = zero_row + direction[0]
        swap_col = zero_col + direction[1]
        row_allowed = 0 <= swap_row < len(self.tiles)
        col_allowed = 0 <= swap_col < len(self.tiles[0])
        return row_allowed and col_allowed

    class _Printer:
        @staticmethod
        def print(tiles: Tuple[Tuple[int, ...], ...]) -> str:
            max_length = max(len(str(num)) for row in tiles for num in row)
            string = ''
            for row in tiles:
                row_str = ' | '.join(f'{num:0{max_length}d}' for num in row)
                string += f'| {row_str} |\n'
            return string

    def __repr__(self):
        return self._Printer.print(self.tiles)


class RandomStartMaker:
    def make(self):
        start = tuple(TileState.GOAL)
        state = TileState(start)
        for _ in range(30):
            state = choice(state.next_states())
        return state


if __name__ == '__main__':
    start = RandomStartMaker().make()
    search = BreadthFirstSearch()
    path_to_goal = search.search(start)
    Printer.print(path_to_goal)
