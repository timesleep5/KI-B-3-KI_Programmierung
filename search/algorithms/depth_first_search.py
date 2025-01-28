from typing import List, override

from search.search import Frontier, State, Search


class Stack(Frontier):
    def __init__(self):
        self._data = []

    @override
    def push(self, path: List[State]):
        self._data.append(path)

    @override
    def pop(self) -> List[State]:
        if self._is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()

    @override
    def __bool__(self) -> bool:
        return not self._is_empty()

    def _is_empty(self):
        return len(self._data) == 0


class DepthFirstSearch(Search):
    @override
    def get_frontier(self, start: State) -> Frontier:
        frontier = Stack()
        frontier.push([start])
        return frontier
