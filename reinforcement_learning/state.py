from typing import Union, List


class State:
    SIZE = 3
    BOARD_CELLS = SIZE * SIZE
    NONE_SYMBOL = '_'
    X_SYMBOL = 'X'
    O_SYMBOL = 'O'

    def __init__(self, board: str = None):
        self._board = self.NONE_SYMBOL * self.BOARD_CELLS if board is None else board
        self._winner_def = {
            self.X_SYMBOL * self.SIZE: self.X_SYMBOL,
            self.O_SYMBOL * self.SIZE: self.O_SYMBOL
        }
        self._winner = None

    def with_new_action(self, position: int) -> 'State':
        if self._board[position] != self.NONE_SYMBOL:
            raise ValueError(f'Cell at position {position} is already occupied!')
        symbol = self.determine_turn()
        new_board = ''.join([symbol if i == position else self._board[i] for i in range(len(self._board))])
        return State(new_board)

    def determine_turn(self) -> str:
        x_count = self._board.count(self.X_SYMBOL)
        o_count = self._board.count(self.O_SYMBOL)
        # x starts
        return self.X_SYMBOL if x_count <= o_count else self.O_SYMBOL

    def is_final(self) -> bool:
        rows = set(
            ''.join([self._board[row * self.SIZE + col] for col in range(self.SIZE)]) for row in range(self.SIZE))
        columns = set(
            ''.join([self._board[row * self.SIZE + col] for row in range(self.SIZE)]) for col in range(self.SIZE))
        diagonals = {''.join([self._board[diag] for diag in (0, 4, 8)]),
                     ''.join([self._board[diag] for diag in (2, 4, 6)])}
        lines = rows | columns | diagonals
        for line in lines:
            if line in self._winner_def.keys():
                self._winner = self._winner_def[line]
                return True
        remaining_moves = self._board.count(self.NONE_SYMBOL)
        return remaining_moves == 0

    def winner(self) -> Union[str, None]:
        return self._winner

    def valid_actions(self) -> List[int]:
        return [1 if cell == self.NONE_SYMBOL else 0 for cell in self._board]

    def indexed_actions(self) -> List[int]:
        return [i * action for i, action in enumerate(self.valid_actions())]

    def __hash__(self):
        return hash(self._board)

    def __eq__(self, other: 'State'):
        return self._board == other._board

    def __repr__(self):
        grid = [self._board[i:i + 3] for i in range(0, 9, 3)]

        string = ''
        for row in grid:
            string += ' | '.join(row) + '\n'

        return string
