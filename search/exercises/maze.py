from dataclasses import dataclass
from typing import List

from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.search import State, Printer

maze = [
    ['O', 'W', 'O', 'O', 'G'],
    ['O', 'W', 'O', 'W', 'O'],
    ['O', 'W', 'O', 'O', 'O'],
    ['O', 'O', 'W', 'W', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
]


@dataclass(frozen=True)
class MazeState(State):
    row: int
    col: int

    def is_goal(self) -> bool:
        return maze[self.row][self.col] == 'G'

    def next_states(self) -> List['State']:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        states = []
        for dir in dirs:
            new_row = self.row + dir[0]
            new_col = self.col + dir[1]
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[new_row]) and maze[new_row][new_col] != 'W':
                states.append(MazeState(new_row, new_col))
        return states


if __name__ == '__main__':
    start = MazeState(4, 0)
    search = BreadthFirstSearch()
    path = search.search(start)
    Printer.print(path)
