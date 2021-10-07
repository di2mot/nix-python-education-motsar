"""GUI for Tic Tak Toe"""
import tkinter as tk


class GuiApp(tk.Frame):
    """GUI"""
    def __init__(self, master=None):
        """Init"""
        super().__init__(master)
        self.master = master
        self.buttons = []
        # self.aiPlayerName = 'X'
        # self.huPlayerName = 'O'
        self.player_step = 'X'
        self.game = True
        self.status = None
        self.score = [0, ':', 0]

        # сюда добавить ники игроков
        self.players_names = {"X": '', "O": ''}

        self.create_menu()
        # self.create_game_field_1()
        self.pack()

    def create_game_field_1(self):
        """Create a game field"""

        game_field_0 = tk.Button(self)
        game_field_1 = tk.Button(self)
        game_field_2 = tk.Button(self)
        game_field_3 = tk.Button(self)
        game_field_4 = tk.Button(self)
        game_field_5 = tk.Button(self)
        game_field_6 = tk.Button(self)
        game_field_7 = tk.Button(self)
        game_field_8 = tk.Button(self)

        position = 0

        self.buttons = [
                 [game_field_0, game_field_1, game_field_2],
                 [game_field_3, game_field_4, game_field_5],
                 [game_field_6, game_field_7, game_field_8]]

        rown = 0

        for row in self.buttons:
            coln = 0
            for col in row:
                col["width"] = 4
                col["height"] = 4
                col["font"] = ('Verdana', 15, 'bold')
                col["background"] = 'lavender'
                col["text"] = " "
                col["command"] = lambda position=position, rown=rown, coln=coln: \
                    self.say_hi(rown, coln, position)
                col.grid(row=rown+1, column=coln, sticky='nsew')
                position += 1
                coln += 1
            rown += 1

    def create_menu(self):
        """Создаю меню"""

        player_1 = tk.Button(self)
        player_1["width"] = 10
        player_1["height"] = 5
        player_1["text"] = "player_1"
        # self.watch_log["command"] = self.create_game_field_1
        player_1.grid(row=0, column=0, sticky='nsew')

        player_2 = tk.Button(self)
        player_2["width"] = 10
        player_2["height"] = 5
        player_2["text"] = "player_2"
        player_2.grid(row=0, column=2, sticky='nsew')

        players = tk.Label(self)
        players["width"] = 10
        players["height"] = 5
        players["text"] = f"SCORE\n{self.score[0]}{self.score[1]}{self.score[2]}"
        players.grid(row=0, column=1, sticky='nsew')

        input_player_1 = tk.Entry(self)
        input_player_1["width"] = 10
        # self.input_player_1["height"] = 5
        input_player_1["text"] = "player_1"
        # self.watch_log["command"] = self.create_game_field_1
        input_player_1.grid(row=1, column=0, sticky='nsew')

        input_player_2 = tk.Entry(self)
        input_player_2["width"] = 10
        # self.input_player_2["height"] = 5
        input_player_2["text"] = "player_2"
        input_player_2.grid(row=1, column=2, sticky='nsew')

        new_game = tk.Button(self)
        new_game["width"] = 10
        new_game["height"] = 5
        new_game["text"] = "New Game"
        new_game["command"] = self.create_new_game
        new_game.grid(row=1, column=1, sticky='nsew')

        watch_log = tk.Button(self)
        watch_log["width"] = 10
        watch_log["height"] = 5
        watch_log["text"] = "Clear log"
        # self.watch_log["command"] = self.create_game_field_1
        watch_log.grid(row=2, column=1, sticky='nsew')

        clear_log = tk.Button(self)
        clear_log["width"] = 10
        clear_log["height"] = 5
        clear_log["text"] = "Watch log"
        watch_log["command"] = self.clear_logging
        clear_log.grid(row=3, column=1, sticky='nsew')

        self.create_control_buttons()
        self.create_plugs()

    def create_control_buttons(self):
        """Control buttons"""
        quit_game = tk.Button(self)
        quit_game['fg'] = "red"
        quit_game['text'] = "QUIT"
        quit_game['command'] = self.master.destroy
        quit_game.grid(row=4, column=2, sticky='nsew')

        menu = tk.Button(self)
        menu['fg'] = "red"
        menu['text'] = "Menu"
        menu['command'] = self.create_menu
        menu.grid(row=4, column=1, sticky='nsew')

    def create_plugs(self):
        """ Заглушки """
        left_empty = tk.Label(self)
        left_empty.grid(row=1, column=0, sticky='nsew')

        left_empty_0 = tk.Label(self)
        left_empty_0.grid(row=2, column=0, sticky='nsew')

        left_empty_1 = tk.Label(self)
        left_empty_1.grid(row=3, column=0, sticky='nsew')

        right_empty = tk.Label(self)
        right_empty.grid(row=1, column=2, sticky='nsew')

        right_empty_1 = tk.Label(self)
        right_empty_1.grid(row=2, column=2, sticky='nsew')
        right_empty_0 = tk.Label(self)
        right_empty_0.grid(row=3, column=2, sticky='nsew')

    @staticmethod
    def say_hi(*args):
        """Controlling how buttons works"""
        print(args)

    def game_result(self, player):
        """Выведит посередине экрана победителя"""
        win_game = tk.Label(self)
        win_game["text"] = f'Winner\n{self.players_names[player]}'

    def create_new_game(self):
        """Create a new game"""
        self.create_game_field_1()

    def game_res(self):
        """Game result"""
        new_game = tk.Button(self)
        new_game["width"] = 10
        new_game["height"] = 5
        new_game["text"] = f"{self.status}"
        new_game["command"] = self.create_menu
        new_game.grid(row=1, column=1, sticky='nsew')

    @staticmethod
    def clear_logging():
        """Do logging"""
        print('Lol')


def run():
    """Run gui"""
    root = tk.Tk()
    app = GuiApp(master=root)
    app.master.title("Tic-Tak-Toe")
    app.master.maxsize(1000, 1000)
    app.mainloop()


if __name__ == "__main__":
    run()
