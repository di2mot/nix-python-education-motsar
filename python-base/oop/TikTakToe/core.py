"""Til-Tak-Koe by Di2mot"""

class TikTakToe:
    """Игра Крестики-Нолики"""

    def __init__(self):
        self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.aiPlayer = 'X'
        self.huPlayer = 'O'
        self.game_status = 'STOP'
        self.game = True
        # чей ход
        self.player_step = self.aiPlayer
        self.available_moves = 9
        self.status = None


    def check_win(self):
        """Сверяет победные комбинации"""
        status = False
        for row in self.win_comb:
            if self.field[row[0]] == self.field[row[1]] == self.field[row[2]]:
                status = True
        if self.available_moves == 0:
            self.game = False
        return status

    def check_available_moves(self):
        """Проверка на доступность хода"""
        status = True
        if self.available_moves <= 1:
            # Draw - ничья
            self.status = 'Draw \nout of moves'
            self.game = False
            status = False
            print('Ничья, ходы кончились!')
        return status

    def write_field_test(self):
        print(f'{self.field[0]}|{self.field[1]}|{self.field[2]}')
        print(f'------')
        print(f'{self.field[3]}|{self.field[4]}|{self.field[5]}')
        print(f'------')
        print(f'{self.field[6]}|{self.field[7]}|{self.field[8]}')

    def _check_correct_input(self, position=None) -> int:
        """Check correct input"""
        res = False
        if isinstance(position, int) and position in self.field:
            res = True
        return res
        # if not position:
        #     while True:
        #         pos = input('Input the number: ')
        #         if pos.isalnum():
        #             if int(pos) in self.field:
        #                 res = int(pos)
        #                 break
        # else:
        #     if isinstance(position, int) and position in self.field:
        #         res = position
        # return res

    def _change_player(self):
        """меняем ход игрока"""
        if self.player_step == self.aiPlayer:
            self.player_step = self.huPlayer
        else:
            self.player_step = self.aiPlayer
        # уменьшаю доступные ходы на 1
        self.available_moves -= 1

    def game_test(self):

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

    def main_loop(self):

        ...

    def run(self):
        ...
if __name__ == "__main__":
    game = TikTakToe()
    game.game_test()
