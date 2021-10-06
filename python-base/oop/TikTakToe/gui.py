import tkinter as tk


class GuiApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.buttons = []
        self.aiPlayerName = 'X'
        self.huPlayerName = 'O'
        self.player_step = 'X'
        self.game = True
        self.status = None

        # сюда добавить ники игроков
        self.players_names = {"X":'', "O":''}

        self.create_menu()
        # self.create_game_field_1()
        self.pack()

    def create_game_field_1(self):
        position = 0
        self.game_field_0 = tk.Button(self)
        self.game_field_1 = tk.Button(self)
        self.game_field_2 = tk.Button(self)
        self.game_field_3 = tk.Button(self)
        self.game_field_4 = tk.Button(self)
        self.game_field_5 = tk.Button(self)
        self.game_field_6 = tk.Button(self)
        self.game_field_7 = tk.Button(self)
        self.game_field_8 = tk.Button(self)

        self.buttons = [[self.game_field_0, self.game_field_1, self.game_field_2],
                 [self.game_field_3, self.game_field_4, self.game_field_5],
                 [self.game_field_6, self.game_field_7, self.game_field_8]]
        rown = 0
        for row in self.buttons:
            coln = 0
            for col in row:
                col["width"] = 4
                col["height"] = 4
                col["font"] = ('Verdana', 15, 'bold')
                col["background"] = 'lavender'
                col["text"] = " "
                col["command"] = lambda position=position, rown=rown, coln=coln: self.say_hi(rown, coln, position)
                col.grid(row=rown+1, column=coln, sticky='nsew')
                position += 1
                coln += 1
            rown += 1


    def create_menu(self):
        self.player_1 = tk.Button(self)
        self.player_1["width"] = 10
        self.player_1["height"] = 5
        self.player_1["text"] = "player_1"
        # self.watch_log["command"] = lambda: self.create_game_field_1()
        self.player_1.grid(row=0, column=0, sticky='nsew')

        self.player_2 = tk.Button(self)
        self.player_2["width"] = 10
        self.player_2["height"] = 5
        self.player_2["text"] = "player_2"
        self.player_2.grid(row=0, column=2, sticky='nsew')

        self.players = tk.Label(self)
        self.players["width"] = 10
        self.players["height"] = 5
        self.players["text"] = "SCORE\n00"
        self.players.grid(row=0, column=1, sticky='nsew')

        self.input_player_1 = tk.Entry(self)
        self.input_player_1["width"] = 10
        # self.input_player_1["height"] = 5
        self.input_player_1["text"] = "player_1"
        # self.watch_log["command"] = lambda: self.create_game_field_1()
        self.input_player_1.grid(row=1, column=0, sticky='nsew')

        self.input_player_2 = tk.Entry(self)
        self.input_player_2["width"] = 10
        # self.input_player_2["height"] = 5
        self.input_player_2["text"] = "player_2"
        self.input_player_2.grid(row=1, column=2, sticky='nsew')






        self.new_game = tk.Button(self)
        self.new_game["width"] = 10
        self.new_game["height"] = 5
        self.new_game["text"] = "New Game"
        self.new_game["command"] = lambda: self.create_new_game()
        self.new_game.grid(row=1, column=1, sticky='nsew')
        # self.hi_there.pack(side="top")

        self.watch_log = tk.Button(self)
        self.watch_log["width"] = 10
        self.watch_log["height"] = 5
        self.watch_log["text"] = "Watch log"
        # self.watch_log["command"] = lambda: self.create_game_field_1()
        self.watch_log.grid(row=2, column=1, sticky='nsew')

        self.clear_log = tk.Button(self)
        self.clear_log["width"] = 10
        self.clear_log["height"] = 5
        self.clear_log["text"] = "Clear log"
        # self.watch_log["command"] = lambda: self.create_game_field_1()
        self.clear_log.grid(row=3, column=1, sticky='nsew')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.quit.grid(row=4, column=2, sticky='nsew')

        menu = tk.Button(self, text="Menu", fg="red",
                              command=self.create_menu)
        menu.grid(row=4, column=1, sticky='nsew')

        """ Заглушки """
        self.left_empty = tk.Label(self)
        self.left_empty.grid(row=1, column=0, sticky='nsew')
        self.left_empty_0 = tk.Label(self)
        self.left_empty_0.grid(row=2, column=0, sticky='nsew')
        self.left_empty_1 = tk.Label(self)
        self.left_empty_1.grid(row=3, column=0, sticky='nsew')

        self.right_empty = tk.Label(self)
        self.right_empty.grid(row=1, column=2, sticky='nsew')
        self.right_empty_0 = tk.Label(self)
        self.right_empty_0.grid(row=2, column=2, sticky='nsew')
        self.right_empty_0 = tk.Label(self)
        self.right_empty_0.grid(row=3, column=2, sticky='nsew')



    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["width"] = 25
        self.hi_there["height"] = 5
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self, rown, coln, position=0):
        print(f"hi there, everyone {position}!")
        self.buttons[rown][coln]['text'] = self.player_step
        print(f"Вернулась кнопка: {self.buttons[rown][coln]}")

    def game_result(self, player):
        """Выведит посередине экрана победителя"""
        self.win_game = tk.Label(self)
        self.win_game["text"] = f'Winner\n{self.players_names[player]}'

    def create_new_game(self, i):
        self.create_game_field_1()

    def game_res(self):
        self.new_game = tk.Button(self)
        self.new_game["width"] = 10
        self.new_game["height"] = 5
        self.new_game["text"] = f"{self.status}"
        self.new_game["command"] = lambda: self.create_menu()
        self.new_game.grid(row=1, column=1, sticky='nsew')


def run():
    root = tk.Tk()
    app = GuiApp(master=root)
    app.master.title("Tic-Tak-Toe")
    app.master.maxsize(1000, 1000)
    app.mainloop()

if __name__ == "__main__":
    run()