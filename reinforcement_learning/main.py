from reinforcement_learning.tic_tac_toe_game import Player, UserEngine, MenaceEngine, TicTacToeGame

from reinforcement_learning.trainer import Trainer

if __name__ == '__main__':
    trainer = Trainer(30_000)
    trainer.train()
    menace = trainer.get_menace()

    player_1 = Player('Korbi', UserEngine())
    player_2 = Player('Menace', MenaceEngine(menace))

    game = TicTacToeGame(player_1, player_2, 3)
    game.start()
