import curses
from os import system, name
from curses import wrapper, echo, window
import logo

class Game:
    '''
    Логика игры
    '''

    def __init__(self, word: str) -> None:
        '''
        self.word: хранит слово
        self.letters: хранит угаданые буквы
        self.attempts: количество попыток
        self.game_status: состояние игры, True/False игра идёт/завершилась
        self.unguessed_lettrs: неугадные буквы
        '''
        self.word = list(word.upper())
        self.letters = ['_' for i in range(len(word))]
        self.attempts = 8
        self.game_status = 'RUN'
        self.unguessed_lettrs = ['_' for i in range(8)]



    def check_word(self, letter: str,) -> int:
        '''
        Проверяет на вхождение буквы в слово
        '''
        if letter in self.word:
            if letter in self.letters:
                return 2
            return 1
        else: return 0



    def input_letter(self, letter: str) -> None:
        '''
        Управляет вводом букв
        '''

        if self.check_word(letter) == 0:


            self.unguessed_lettrs[-self.attempts] = letter

            self.attempts -= 1

            if self.attempts >= 1:
                self.write_man()
            elif self.attempts == 0:
                self.game_status = 'LOSE'

            return f'Не верно, буквы {letter} в этом слове нет'

        elif self.check_word(letter) == 1:
            self.find_letter_in_word(letter)

            if self.word == self.letters:
                self.game_status = 'WIN'
            return f'Правильно, буква {letter} есть в этом слове'

        elif self.check_word(letter) == 2:
            return f"Попробуй снова, буква {letter.capitalize()} уже открыта"


    def find_letter_in_word(self, letter):
        '''
        находит и индексы буквы и сеняет их в self.letters
        '''

        res = [i for i, x in enumerate(self.word) if x == letter]

        for i in res:
            self.letters[i] = letter

    def write_man(self):
        hanman = {
            7 : [12, 4, 'O'],
            6 : [13, 4, '|'],
            5 : [14, 4, '|'],
            4 : [13, 3, '\\'],
            3 : [13, 5, '/'],
            2 : [15, 3, '/'],
            1 : [15, 5, '\\'],
        }
        x, y, symbol = hanman[self.attempts]
        self.stdckr.addstr(x, y, f'{symbol}')


    def init_window(self, stdscr):
        '''
        Функция отвечает за отображение
        '''
        self.stdckr = stdscr
        stdscr.clear()

        # верхняя граница
        border = '/' * 60
        stdscr.addstr(0, 0, f'{border}')
        # рисуем лого
        stdscr.addstr(1, 0, f'{logo.hagman_logo}')
        # рисуем виселицу
        stdscr.addstr(9, 3, f'{logo.postament}')
        # нижняя граница
        stdscr.addstr(22, 0, f'{border}')

        # рисуем ячейки под буквы
        let = " ".join(self.letters)
        stdscr.addstr(19, 5, f'{let}')

        # рисуем остаток попыток
        stdscr.addstr(10, 20, 'Осталось попыток:')
        stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)

        # рисуем нугаданные буквы
        ung = " ".join(self.unguessed_lettrs)
        stdscr.addstr(12, 20, 'Неугаданные буквы:')
        stdscr.addstr(14, 20, f'{ung}')

        while self.game_status == 'RUN':            
            letter = str(stdscr.get_wch())

            if letter.isalpha():

                msg = self.input_letter(letter.upper())

                stdscr.addstr(16, 20, f'{msg}')
                stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)
                stdscr.addstr(19, 5, f'{" ".join(self.letters)}')
                stdscr.addstr(14, 20, f'{" ".join(self.unguessed_lettrs)}')

        if self.game_status == "WIN":
            stdscr.addstr(10, 20, logo.win_game, curses.A_BOLD)
            stdscr.addstr(12, 6, '(Я вижил!)', curses.A_BOLD)
            stdscr.refresh()
            stdscr.getkey()

        elif self.game_status == 'LOSE':
            stdscr.addstr(12, 6, '(Помереть!)', curses.A_BOLD)
            stdscr.addstr(16, 20, f'Проигрыш, загаданое слово: {"".join(self.word)}     ')
            stdscr.refresh()
            stdscr.getkey()
        

    def run(self):
        wrapper(self.init_window)
        echo()




def main():
    game = Game('кошка')
    game.run()

if __name__ == '__main__':
    main()