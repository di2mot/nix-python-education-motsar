import curses
from curses import wrapper, echo
import logo as lg
import random
import os
from pathlib import Path

class Game:
    '''
    Логика игры
    '''

    def __init__(self) -> None:
        '''
        self.word: хранит слово
        self.letters: хранит угаданые буквы
        self.attempts: количество попыток
        self.game_status: состояние игры, True/False игра идёт/завершилась
        self.unguessed_lettrs: неугадные буквы
        '''
        self.word = list(self.get_word().upper())
        self.letters = ['_' for i in range(len(self.word))]
        self.attempts = 8
        self.game_status = 'RUN'
        self.unguessed_lettrs = ['_' for i in range(8)]

    def get_word(self) -> str:
        '''
        Получат случайное слово из документа
        '''

        word_list = []

        # костыль, у питое есть проблема с определением директории
        path = str(Path.cwd()) + '/words'

        with open(path, 'r') as f:
            word_list = f.read().split()
        word = random.choice(word_list)
        return word



    def check_word(self, letter: str,) -> int:
        '''
        Проверяет на вхождение буквы в слово
        '''
        if letter in self.word:
            if letter in self.letters:
                return 2
            return 1
        elif letter in self.unguessed_lettrs:
            return 2
        else: return 0


    def input_letter(self, letter: str) -> str:
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

            return f'Буквы {letter} в этом слове нет' + ' '*10

        elif self.check_word(letter) == 1:
            self.find_letter_in_word(letter)

            if self.word == self.letters:
                self.game_status = 'WIN'
            return f'Буква {letter} есть в этом слове' + ' '*10

        elif self.check_word(letter) == 2:
            return f"Буква {letter.capitalize()} уже была" + ' '*10


    def find_letter_in_word(self, letter: str):
        '''
        Находит и индексы буквы и заменяет их в self.letters
        '''

        res = [i for i, x in enumerate(self.word) if x == letter]

        for i in res:
            # print(i)
            self.letters[i] = letter

    def write_man(self):

        x, y, symbol = lg.hanman[self.attempts]
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
        stdscr.addstr(1, 0, f'{lg.hagman_logo}')
        # рисуем виселицу
        stdscr.addstr(9, 3, f'{lg.postament}')
        # нижняя граница
        stdscr.addstr(22, 0, f'{border}')

        # рисуем ячейки под буквы
        let = " ".join(self.letters)
        stdscr.addstr(19, 5, f'{let}')

        # рисуем остаток попыток
        stdscr.addstr(10, 21, 'Осталось попыток:')
        stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)

        # рисуем нугаданные буквы
        ung = " ".join(self.unguessed_lettrs)
        stdscr.addstr(12, 21, 'Неугаданные буквы:')
        stdscr.addstr(14, 21, f'{ung}')

        for i in range(10, 16):
            stdscr.addstr(i, 19, '|')
            stdscr.addstr(i, 50, '|')
        for i in range(20, 50):
            stdscr.addstr(9, i, '_')
            stdscr.addstr(11, i, '-')
            stdscr.addstr(13, i, '-')
            stdscr.addstr(15, i, '-')
            stdscr.addstr(17, i, '_')


        while self.game_status == 'RUN':            
            letter = str(stdscr.get_wch())

            if letter.isalpha():

                msg = self.input_letter(letter.upper())

                stdscr.addstr(16, 20, f'{msg}')
                stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)
                stdscr.addstr(19, 5, f'{" ".join(self.letters)}')
                stdscr.addstr(14, 20, f'{" ".join(self.unguessed_lettrs)}')
                stdscr.addstr(12, 6, lg.wont_live[self.attempts], curses.A_BOLD)

        if self.game_status == "WIN":
            stdscr.addstr(10, 20, lg.win_game, curses.A_BOLD)
            stdscr.addstr(12, 6, '(Я вижил!)', curses.A_BOLD)
            stdscr.refresh()
            stdscr.getkey()

        elif self.game_status == 'LOSE':
            stdscr.addstr(12, 6, lg.wont_live[self.attempts], curses.A_BOLD)
            stdscr.addstr(16, 20, f'Проигрыш, загаданое слово: {"".join(self.word)}     ')
            stdscr.refresh()
            stdscr.getkey()


    def run(self):
        wrapper(self.init_window)
        echo()


def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
