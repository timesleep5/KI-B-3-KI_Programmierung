from dataclasses import dataclass
from typing import Tuple, override, List

from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.algorithms.depth_first_search import DepthFirstSearch
from search.search import Timer, State, Printer


@dataclass(frozen=True, repr=False)
class SudokuState(State):
    cells: Tuple[Tuple[int, ...], ...]

    @override
    def is_goal(self) -> bool:
        return all([0 not in row for row in self.cells])

    @override
    def next_states(self) -> List['SudokuState']:
        row, col = self._next_empty_cell()
        next_states = [self._fill(row, col, value) for value in range(1, 10) if self._allowed(row, col, value)]
        return next_states

    def _fill(self, row: int, col: int, value: int) -> 'SudokuState':
        new_cells = list(list(row) for row in self.cells)
        new_cells[row][col] = value
        new_cells = tuple(tuple(row) for row in new_cells)
        return SudokuState(new_cells)

    def _allowed(self, row_index: int, col_index: int, value: int) -> bool:
        row = self.cells[row_index]
        col = [row[col_index] for row in self.cells]
        box_row_start = row_index // 3 * 3
        box_row_end = box_row_start + 3
        box_col_start = col_index // 3 * 3
        box_col_end = box_col_start + 3
        box = [self.cells[row][col]
               for row in range(box_row_start, box_row_end)
               for col in range(box_col_start, box_col_end)]
        allowed = (value not in row
                   and value not in col
                   and value not in box)

        return allowed

    def _next_empty_cell(self) -> Tuple[int, int]:
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j

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
        return self._Printer.print(self.cells)


if __name__ == '__main__':
    start = SudokuState((
        (5, 3, 0, 0, 7, 0, 0, 0, 0),
        (6, 0, 0, 1, 9, 5, 0, 0, 0),
        (0, 9, 8, 0, 0, 0, 0, 6, 0),
        (8, 0, 0, 0, 6, 0, 0, 0, 3),
        (4, 0, 0, 8, 0, 3, 0, 0, 1),
        (7, 0, 0, 0, 2, 0, 0, 0, 6),
        (0, 6, 0, 0, 0, 0, 2, 8, 0),
        (0, 0, 0, 4, 1, 9, 0, 0, 5),
        (0, 0, 0, 0, 8, 0, 0, 0, 0)
    ))
    breadth_first_search = BreadthFirstSearch()
    depth_first_search = DepthFirstSearch()

    breadth_path = Timer.timer(lambda: breadth_first_search.search(start), 'breadth first search')
    depth_path = Timer.timer(lambda: depth_first_search.search(start), 'depth first search')

    print('Breadth first search path:')
    Printer.print(breadth_path)
    #
    # print('Depth first search path:')
    # Printer.print(depth_path)
