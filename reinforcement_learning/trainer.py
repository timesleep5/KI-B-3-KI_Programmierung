from reinforcement_learning.menace import Menace, State


class Trainer:
    def __init__(self, training_rounds: int):
        self.menace = Menace()
        self.training_rounds = training_rounds
        self.wins = [0, 0, 0]

    def train(self):
        print('training...')
        for _ in range(self.training_rounds):
            self.play_game()
        print('training complete!')
        self.print_summary()

    def play_game(self):
        state = State()
        history = []
        while not state.is_final():
            action = self.menace.choose_action_with_probability(state)
            history.append((state, action))
            state = state.with_new_action(action)
        winner = state.winner()
        self.menace.update(history, winner)
        self.register_winner(winner)

    def register_winner(self, winner):
        if winner == State.X_SYMBOL:
            self.wins[0] += 1
        elif winner == State.O_SYMBOL:
            self.wins[1] += 1
        else:
            self.wins[2] += 1

    def print_summary(self):
        content = f'X Wins: {self.wins[0]}\nO Wins: {self.wins[1]}\nTies: {self.wins[2]}'
        print(content)
        print()

    def get_menace(self) -> Menace:
        return self.menace
