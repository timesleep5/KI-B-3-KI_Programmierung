from typing import List, override

from search.search import Search, State, Frontier


class Queue(Frontier):
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data: List[List[State]] = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0  # number of cells starting from front that are not None, number of items
        self._front = 0  # inner representation of the first element of the circular list

    @override
    def push(self, path: List[State]):
        if self._size == self._capacity():
            self._resize(2 * self._capacity())
        next_available_cell = (self._front + self._size) % self._capacity()
        self._data[next_available_cell] = path
        self._size += 1

    @override
    def pop(self) -> List[State]:
        if self._is_empty():
            raise ValueError('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity()
        self._size -= 1
        return answer

    @override
    def __bool__(self) -> bool:
        return not self._is_empty()

    def _is_empty(self):
        return self._size == 0

    def _resize(self, new_size):
        old = self._data
        self._data = [None] * new_size
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def _capacity(self):
        return len(self._data)


class BreadthFirstSearch(Search):
    @override
    def get_frontier(self, start: State) -> Frontier:
        frontier = Queue()
        frontier.push([start])
        return frontier
