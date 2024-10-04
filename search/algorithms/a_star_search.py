from typing import override, Callable, List

from search.search import Search, State, Frontier


class SortedList(Frontier):
    def __init__(self, sorting_function: Callable):
        self.sorting_function = sorting_function
        self._data = []

    @override
    def push(self, path: List[State]) -> None:
        self._data.append(path)

    @override
    def pop(self) -> List[State]:
        if self._is_empty():
            raise ValueError('List is empty')
        self._data.sort(key=self.sorting_function)
        return self._data.pop()

    @override
    def __bool__(self) -> bool:
        return not self._is_empty()

    def _is_empty(self):
        return len(self._data) == 0


class AStarSearch(Search):
    def __init__(self, sorting_function: Callable):
        self.sorting_function = sorting_function

    @override
    def get_frontier(self, start: State) -> Frontier:
        frontier = SortedList(self.sorting_function)
        frontier.push([start])
        return frontier
