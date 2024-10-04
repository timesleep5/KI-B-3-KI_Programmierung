import time
from abc import ABC
from collections.abc import Callable
from typing import List


class State:
    def next_states(self) -> List['State']:
        raise NotImplementedError('State is an interface')

    def is_goal(self) -> bool:
        raise NotImplementedError('State is an interface')

    def __hash__(self) -> int:
        raise NotImplementedError('State is an interface')

    def __eq__(self, other: 'State') -> bool:
        raise NotImplementedError('State is an interface')


class Frontier:
    def pop(self) -> List[State]:
        raise NotImplementedError('Frontier is an interface')

    def push(self, path: List[State]) -> None:
        raise NotImplementedError('Frontier is an interface')

    def __bool__(self) -> bool:
        raise NotImplementedError('Frontier is an interface')


class Search(ABC):
    def get_frontier(self, start: State) -> Frontier:
        raise NotImplementedError('Search is an abstract class')

    def search(self, start: State) -> List[State]:
        frontier = self.get_frontier(start)
        explored = set()
        while frontier:
            path = frontier.pop()
            current_state = path[-1]
            if current_state.is_goal():
                return path
            for state in current_state.next_states():
                if state not in explored:
                    explored.add(state)
                    new_path = path + [state]
                    frontier.push(new_path)
        raise ValueError('No path found')


class Printer:
    @staticmethod
    def print(states: List[State]) -> None:
        for state in states:
            print(state)
            print('-------------------------------------')


class Timer:
    @staticmethod
    def timer(executable: Callable, method: str) -> List[State]:
        start_time = time.time()

        res = executable()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time of {method}: {elapsed_time:.4f} seconds")

        return res
