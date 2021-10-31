"""Tik-Tak-Koe by Di2mot"""
import logging
import os


class TikTakToe:
    """Tic Tak Toe game class"""

    def __init__(self):
        """Init"""
        self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.players = {'ai_player': 'X', 'hy_player': 'O'}
        self.game = False
        self.player_step = 'X'
        self.available_moves = 9
        self.status = None
        self.score = {"X": 0, "O": 0}
        self.logger = logging
        self.logging_config()

    def logging_config(self):
        """Logging configs"""
        _log_filename = 'wins.log'
        self.logger.basicConfig(filename=_log_filename,
                                level=logging.INFO,
                                format='%(asctime)s - %(message)s')

    def _get_player(self, player: int) -> str:
        """Return str of player name"""

        if player > 1:
            raise IndexError("Index out of list")

        player_name = list(self.players.keys())[player]
        return player_name

    def _input_payer_name(self, player_number):
        """Input name of player"""

        while True:
            old_name = self._get_player(player_number)
            value = self.players.pop(old_name)
            new_name = input(f"Input name of {value} player:    ")
            self.players[new_name] = value

            return

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

        if self.available_moves <= 0:
            # Draw - ничья
            self.status = 'Draw. Out of moves'
            self.game = False
            status = False
            self.logger.info('Draw out of moves!')
            print('Draw out of moves!')
        return status

    def write_field_test(self):
        """Write a field"""

        print('------')
        print(f'{self.field[0]}|{self.field[1]}|{self.field[2]}')
        print('------')
        print(f'{self.field[3]}|{self.field[4]}|{self.field[5]}')
        print('------')
        print(f'{self.field[6]}|{self.field[7]}|{self.field[8]}')
        print('------')

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
        """Change players"""

        if self.player_step == self.players[self._get_player(0)]:
            self.player_step = self.players[self._get_player(1)]
        else:
            self.player_step = self.players[self._get_player(0)]

    def run_game(self):
        """Game"""

        while self.game:
            # draw game field
            print(f"{self._get_player(0)} | {self._get_player(1)}")
            pl0_score = self.score[self.players[self._get_player(0)]]
            pl1_score = self.score[self.players[self._get_player(1)]]

            if self.status:
                print(f"{pl0_score} | {pl1_score}")

            self.write_field_test()

            self.check_available_moves()

            if self.game:
                print(f"Player turn: {self.player_step}")

                position = self._check_correct_input()
                self.field[position] = self.player_step

            if self.check_win():
                print(f'Победа за {self.player_step}')
                self.score[self.player_step] += 1
                self.game = False
            self._change_player()
            # уменьшаю доступные ходы на 1
            self.available_moves -= 1

    def _restore_game(self):
        self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.available_moves = 9

    def menu(self):
        """Game menu"""
        while True:
            print("New Game: 1")
            print("Watch log: 2")
            print("Clear log: 3")
            print("Exit: 0")
            res = int(input("Enter number "))
            if res == 1:
                self.game = True
                return
            if res == 2:
                self._watch_log()
            if res == 3:
                self._clear_logging()
            if res == 0:
                exit()

    def main_loop(self):
        """Main loop"""
        self.menu()
        self._input_payer_name(1)
        self._input_payer_name(0)
        self.player_step = self.players[self._get_player(0)]

        while True:
            self.run_game()

            print('Want play again? Y/N')
            res = input(' ')

            if res.upper() == 'Y':
                self.game = True
                self.status = True
                self._restore_game()
            elif res.upper() == 'N':
                return False

    def run(self):
        """Start game"""
        self.main_loop()

    @staticmethod
    def _clear_logging():
        """Clear logging"""
        print('Clear log')
        os.system(r' >wins.log')

    @staticmethod
    def _watch_log():
        with open('wins.log', 'r') as file:
            for line in file:
                print(line)
        input("push Enter to continue")
        return


if __name__ == "__main__":
    game = TikTakToe()
    game.run()
