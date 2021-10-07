"""Control class in MVC"""
import tkinter as tk
import os
from core import TikTakToe
from gui import GuiApp



class GameModel(GuiApp, TikTakToe):
    """Control class"""

    def __init__(self):
        """Init"""
        root = tk.Tk()
        GuiApp.__init__(self, master=root)
        TikTakToe.__init__(self)
        self.master.title("Tic-Tak-Toe")
        self.master.maxsize(1000, 1000)
        self.mainloop()

    def create_new_game(self):
        """Созадётся новая игра
        Для этого все переменные сбрасываются в исходное состояние
        """
        self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.available_moves = 9
        self.game = True
        self.create_game_field_1()

    def clear_logging(self):
        """Logging"""
        print('log is clean')
        os.system(r' >wins.log')

    def say_hi(self, *args):
        """Главная функция игры которая рулит всем"""
        rown, coln, position = args
        if self.game:
            if self._check_correct_input(int(position)):
                self.buttons[rown][coln]['text'] = self.player_step
                self.field[position] = self.player_step

                if self.check_win():
                    self.status = f'Победа за\n {self.player_step}'
                    self.game = False
                    self.game_res()
                if not self.check_available_moves():
                    self.game_res()
                self._change_player()
