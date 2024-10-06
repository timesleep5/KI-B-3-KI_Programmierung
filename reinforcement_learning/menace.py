from random import randint
from typing import Union, List, Tuple

from reinforcement_learning.state import State


class Menace:
    START_DROP_NUMBER = 50
    WIN_REWARD = 5
    TIE_REWARD = 1
    LOSE_PENALTY = -1

    def __init__(self):
        self.value_function = {}

    def choose_action_with_probability(self, state: State):
        if state not in self._known_states() or sum(self.value_function[state]) < 1:
            self._initialize_new_state(state)
        action_weights = self.value_function[state]
        total = sum(action_weights)
        roll = randint(1, total)

        for i, weight in enumerate(action_weights):
            if roll <= weight:
                return i
            roll = roll - weight

    def choose_action_with_policy(self, state: State):
        action_weights = self.value_function[state]
        print(action_weights)
        max_i = 0
        for i, weight in enumerate(action_weights):
            if weight > action_weights[max_i]:
                max_i = i
        return max_i

    def _known_states(self):
        return self.value_function.keys()

    def _initialize_new_state(self, state: State) -> None:
        valid_actions = state.valid_actions()
        weighted_actions = list(map(lambda x: x * self.START_DROP_NUMBER, valid_actions))
        self.value_function[state] = weighted_actions

    def update(self, history: List[Tuple[State, int]], winner: Union[str, None]):
        if winner:
            x_pairs = history[::2]
            o_pairs = history[1::2]
            winner_pairs, loser_pairs = (x_pairs, o_pairs) if winner == State.X_SYMBOL else (o_pairs, x_pairs)
            for winner_pair in winner_pairs:
                self._adjust_weight(winner_pair, self.WIN_REWARD)
            for loser_pair in loser_pairs:
                self._adjust_weight(loser_pair, self.LOSE_PENALTY)
        else:
            for pair in history:
                self._adjust_weight(pair, self.TIE_REWARD)

    def _adjust_weight(self, pair: Tuple[State, int], adjustment: int) -> None:
        state, action = pair
        self.value_function[state][action] += adjustment
