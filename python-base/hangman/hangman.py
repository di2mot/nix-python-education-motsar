'''Hangman by Di2mot'''
import curses
from curses import wrapper, echo
import random
from pathlib import Path
# локальный импорт
import logo as lg

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
        self.game_status = 'MENU'
        self.unguessed_lettrs = ['_' for i in range(8)]
        self.stdscr = None

    def run(self):
        '''
        запустить игру
        '''
        wrapper(self.main_loop)
        echo()

    @staticmethod
    def get_word(document='words', mode='r') -> str:
        '''
        Получат случайное слово из документа
        '''

        # костыль, у питое есть проблема с определением директории
        path = str(Path.cwd()) + f'/{document}'

        with open(path, 'r') as get_word:
            word_list = get_word.read().split()

        if mode == 'r':
            res = random.choice(word_list)
        elif mode == 'l':
            res = tuple(word_list[0:20])
        return res

    def write_words(self):
        '''
        Записывает слова в файл
        '''

        path = str(Path.cwd()) + '/prWords'

        word = ''.join(self.word)

        with open(path, 'w') as writer:
            writer.write(word)


    def check_word(self, letter: str,) -> int:
        '''
        Проверяет на вхождение буквы в слово
        '''

        if letter in self.word:

            if letter in self.letters:
                msg = 2
                # return 2
            else: msg = 1
            # return 1
        elif letter in self.unguessed_lettrs:
            msg = 2
            # return 2
        else:
            msg = 0
        #     # return 0
        return msg


    def input_letter(self, stdscr, letter: str) -> str:
        '''
        Управляет вводом букв
        '''
        msg = ''
        if self.check_word(letter) == 0:
            self.unguessed_lettrs[-self.attempts] = letter

            self.attempts -= 1
            if self.attempts >= 1:
                self.write_man(stdscr)

            elif self.attempts == 0:
                self.game_status = 'LOSE'
            msg = f'Буквы {letter} в этом слове нет' + ' '*10
            # return f'Буквы {letter} в этом слове нет' + ' '*10

        elif self.check_word(letter) == 1:
            self.find_letter_in_word(letter)

            if self.word == self.letters:
                self.game_status = 'WIN'
            msg = f'Буква {letter} есть в этом слове' + ' '*10
            # return f'Буква {letter} есть в этом слове' + ' '*10

        elif self.check_word(letter) == 2:
            msg = f"Буква {letter.capitalize()} уже была" + ' '*10
            # return f"Буква {letter.capitalize()} уже была" + ' '*10
        return msg

    def find_letter_in_word(self, letter: str):
        '''
        Находит и индексы буквы и заменяет их в self.letters
        '''

        res = [i for i, temp_x in enumerate(self.word) if temp_x == letter]
        for i in res:
            self.letters[i] = letter

    def write_man(self, stdscr):
        '''
        Рисует человечка
        '''
        line, colum, symbol = lg.hanman[self.attempts]
        stdscr.addstr(line, colum, f'{symbol}')

    def init_windows(self, stdscr):
        '''
        Функция отвечает за отображение
        '''
        stdscr.clear()
        stdscr.refresh()

        # верхняя граница
        border = '/' * 60
        stdscr.addstr(0, 0, f'{border}')
        # рисуем лого
        stdscr.addstr(1, 0, f'{lg.hagman_logo}')
        # рисуем виселицу
        stdscr.addstr(9, 3, f'{lg.postament_menu}')
        # нижняя граница
        stdscr.addstr(22, 0, f'{border}')

        for i in range(10, 18):
            stdscr.addstr(i, 19, '|')
            stdscr.addstr(i, 50, '|')
        for i in range(20, 50):
            stdscr.addstr(9, i, '_')
            stdscr.addstr(11, i, '-')
            stdscr.addstr(13, i, '-')
            stdscr.addstr(15, i, '-')
            stdscr.addstr(17, i, '_')

        # рисуем ячейки под буквы
        let = " ".join(self.letters)
        stdscr.addstr(19, 5, f'{let}')

        if self.game_status == 'MENU':
            stdscr.addstr(10, 30, 'Меню')
            stdscr.addstr(12, 21, 'Играть [И]')
            stdscr.addstr(14, 21, 'Результаты [Р]')
            stdscr.addstr(16, 21, 'Выйти [В]')

        elif self.game_status == 'RUN':
            pass


    def main_loop(self, stdscr):
        '''
        Функция отвечает за отображение
        '''
        self.stdscr = stdscr


        while self.game_status:
            # Меню игры
            # Играть (И)
            # Результаты (Р)
            # Выйти (В)

            if self.game_status == 'MENU':

                self.init_windows(stdscr)
                stdscr.refresh()
                key = str(stdscr.get_wch()).upper()


                if key in ('И', 'B'):
                    self.game_status = 'RUN'
                    # рисуем виселицу
                    count = 0
                    for i in range(10, 18):
                        stdscr.addstr(i, 0, str(lg.postament[count][0]))
                        count += 1

                    # зарисовываем старые надписи
                    for i in range(10, 18, 2):
                        stdscr.addstr(i, 21, str(' ' * 9))
                    for i in range(1, 20):
                        stdscr.addstr(i, 60, str(" " * 9))

                    # рисуем остаток попыток
                    stdscr.addstr(10, 21, 'Осталось попыток:')
                    stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)

                    # рисуем нугаданные буквы
                    ung = " ".join(self.unguessed_lettrs)
                    stdscr.addstr(12, 21, 'Неугаданные буквы:')
                    stdscr.addstr(14, 21, f'{ung}')



                elif key in ('Р', 'H'):

                    word_list = self.get_word('prWords', mode='l')

                    for i, words in enumerate(word_list):
                        stdscr.addstr(2 + i, 55, words)

                    stdscr.get_wch()

                elif key in ('В', 'D'):
                    self.game_status = False

            elif self.game_status == 'RUN':
                letter = str(stdscr.get_wch())

                if letter.isalpha():
                    msg = self.input_letter(stdscr, letter.upper())

                    stdscr.addstr(16, 20, f'{msg}')
                    stdscr.addstr(10, 40, f'{self.attempts}', curses.A_BOLD)
                    stdscr.addstr(19, 5, f'{" ".join(self.letters)}')
                    stdscr.addstr(14, 20, f'{" ".join(self.unguessed_lettrs)}')
                    stdscr.addstr(12, 6, lg.wont_live[self.attempts], curses.A_BOLD)


            elif self.game_status == "WIN":
                stdscr.addstr(10, 20, lg.win_game, curses.A_BOLD)
                stdscr.addstr(12, 6, '(Я вижил!)', curses.A_BOLD)
                self.write_words()

                stdscr.get_wch()
                self.__init__()
                self.game_status = 'MENU'


            elif self.game_status == 'LOSE':
                stdscr.addstr(12, 6, lg.wont_live[self.attempts], curses.A_BOLD)
                stdscr.addstr(16, 20, f'Проигрыш, загаданое слово: {"".join(self.word)}     ')

                stdscr.get_wch()
                self.game_status = 'MENU'
                self.__init__()


def main():
    '''
    Запускаем игру
    '''
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
