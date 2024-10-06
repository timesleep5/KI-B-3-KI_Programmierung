from random import random
from typing import override

from reinforcement_learning.menace import Menace, State


class Engine:
    def next_input(self, state: State) -> int:
        raise NotImplementedError()


class UserEngine(Engine):
    @override
    def next_input(self, state: State) -> int:
        self._print_state_and_options(state)
        valid_actions = state.indexed_actions()
        chosen_action = None
        while chosen_action not in valid_actions:
            action_string = input('Enter an option: ')
            if action_string.isnumeric():
                chosen_action = int(action_string)
        return chosen_action

    @staticmethod
    def _print_state_and_options(state: State):
        valid_actions = state.valid_actions()
        indexed_actions = [str(i * action) if action > 0 else '_' for i, action in enumerate(valid_actions)]
        options_lines = str(State(''.join(indexed_actions))).split("\n")
        state_lines = str(state).split("\n")
        for i in range(len(state_lines)):
            print(f'{state_lines[i]}\t\t{options_lines[i]}')


class MenaceEngine(Engine):
    def __init__(self, menace: Menace):
        self.menace = menace

    @override
    def next_input(self, state: State) -> int:
        return self.menace.choose_action_with_policy(state)


class Player:
    def __init__(self, name: str, engine: Engine):
        self.name = name
        self.engine = engine
        self.wins = 0

    def get_next_action(self, state: State) -> int:
        return self.engine.next_input(state)

    def win(self):
        self.wins += 1

    def summary(self):
        print(f'{self.name} won {self.wins} times.')

    def __eq__(self, other):
        return self.name == other.name


class PlayerSwapper:
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.last_player = self.player_2

    def next(self):
        next_player = self.player_1 if self.last_player == self.player_2 else self.player_2
        self.last_player = next_player
        return next_player

    def shuffle_players(self):
        if random() < 0.5:
            self.player_1, self.player_2 = self.player_2, self.player_1
            self.last_player = self.player_2


class TicTacToeGame:
    def __init__(self, player_1: Player, player_2: Player, rounds: int):
        self.player_swapper = PlayerSwapper(player_1, player_2)
        self.rounds = rounds

    def start(self):
        for _ in range(self.rounds):
            self.player_swapper.shuffle_players()
            state = State()
            current_player: Player
            self._print_with_border('new game')
            while not state.is_final():
                current_player = self.player_swapper.next()
                print(f'\n{current_player.name}\'s turn ({state.determine_turn()})')
                action = current_player.get_next_action(state)
                state = state.with_new_action(action)
                print(f'{current_player.name} chose {action}:\n{state}')
            self._handle_end_of_game(state.winner(), current_player)
        self._handle_end_of_all_games()

    @staticmethod
    def _handle_end_of_game(winner, player: Player):
        content: str
        if winner is None:
            content = 'It\'s a tie, nobody won!'
        else:
            content = f'{player.name} won!'
            player.win()
        print(content)

    def _handle_end_of_all_games(self):
        self._print_with_border('End of all games!')
        self.player_swapper.next().summary()
        self.player_swapper.next().summary()

    def _print_with_border(self, text: str):
        border = '~' * 30
        content = f'\n\n{border}\n{text}\n{border}'
        print(content)
