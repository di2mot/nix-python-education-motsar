"""Til-Tak-Koe by Di2mot"""
import logging
import os

class TikTakToe:
    """Tic Tak Toe game class"""

    def __init__(self):
        """Init"""
        self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.players = {'ai_player': 'X', 'hy_player': 'O'}
        self.game = True
        # чей ход
        self.player_step = self.players['ai_player']
        self.available_moves = 9
        self.status = None
        self.logger = logging
        self.logging_config()

    def logging_config(self):
        """Logging configs"""
        _log_filename = 'wins.log'
        self.logger.basicConfig(filename=_log_filename,
                                level=logging.INFO,
                                format='%(asctime)s - %(message)s')


    def check_win(self):
        """Check wins combinations"""
        win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        status = False
        for row in win_comb:
            if self.field[row[0]] == self.field[row[1]] == self.field[row[2]]:
                status = True
                self.logger.info(f'Winner is {self.player_step}')
        return status

    def check_available_moves(self):
        """Check available moves"""
        status = True
        if self.available_moves <= 1:
            # Draw - ничья
            self.status = 'Draw \nout of moves'
            self.game = False
            status = False
            self.logger.info('Draw out of moves!')
            print('Draw out of moves!')
        return status

    def write_field_test(self):
        """Write a field"""
        print(f'{self.field[0]}|{self.field[1]}|{self.field[2]}')
        print('------')
        print(f'{self.field[3]}|{self.field[4]}|{self.field[5]}')
        print('------')
        print(f'{self.field[6]}|{self.field[7]}|{self.field[8]}')

    def _check_correct_input(self, position=None) -> int:
        """Check correct input"""
        res = False
        if isinstance(position, int) and position in self.field:
            res = True
        # return res
        elif position is None:
            while True:
                pos = input('Input the number: ')
                if pos.isalnum():
                    if int(pos) in self.field:
                        res = int(pos)
                        break
        else:
            if isinstance(position, int) and position in self.field:
                res = position
        return res

    def _change_player(self):
        """меняем ход игрока"""
        if self.player_step == self.players['ai_player']:
            self.player_step = self.players['hy_player']
        else:
            self.player_step = self.players['ai_player']
        # уменьшаю доступные ходы на 1
        self.available_moves -= 1

    def game_test(self):
        """Test game"""

        while self.game:
            # draw game field
            self.write_field_test()

            print(f"Ход игрока: {self.player_step}")

            position = self._check_correct_input()

            self.field[position] = self.player_step

            if self.check_win():
                print(f'Победа за {self.player_step}')
                self.game = False

            self._change_player()

    @staticmethod
    def clear_logging():
        """Clear logging"""
        print('Clear log')
        os.system(r' >wins.log')


if __name__ == "__main__":
    game = TikTakToe()
    game.game_test()
