from typing import override, List, Tuple

from attr import dataclass

from search.algorithms.breadth_first_search import BreadthFirstSearch
from search.search import State, Printer


@dataclass(frozen=True)
class MazeState(State):
    row: int
    col: int

    @override
    def is_goal(self):
        return Maze.is_goal(self)

    @override
    def next_states(self) -> List['MazeState']:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        new_states = [self._moved(d)
                      for d in directions
                      if Maze.allowed(self._moved(d))]

        return new_states

    def _moved(self, direction: Tuple[int, int]) -> 'MazeState':
        return MazeState(self.row + direction[0], self.col + direction[1])


class Maze:
    _maze = [[' ', 'W', ' ', ' ', 'G'],
             [' ', 'W', ' ', 'W', ' '],
             [' ', 'W', ' ', ' ', ' '],
             [' ', ' ', 'W', 'W', ' '],
             [' ', ' ', ' ', ' ', ' ']]
    _rows = len(_maze)
    _cols = len(_maze[0])

    @staticmethod
    def is_goal(state: MazeState) -> bool:
        return Maze._maze[state.row][state.col] == 'G'

    @staticmethod
    def allowed(state: MazeState) -> bool:
        return (0 <= state.row < Maze._rows
                and 0 <= state.col < Maze._cols
                and Maze._maze[state.row][state.col] != 'W')


if __name__ == '__main__':
    start = MazeState(0, 0)
    search = BreadthFirstSearch()
    path_to_goal = search.search(start)
    Printer.print(path_to_goal)
