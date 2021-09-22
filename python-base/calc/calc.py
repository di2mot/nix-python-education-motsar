'''Simple calculator'''

class Calc:
    '''
    Класса представляет 4 базовых операции, сложения, вычитания, умножения и деления
    При создании экземпляра класа принимает два возможных значения, i и r
    i - выводит на печать
    r - возвращает int значение
    '''

    def __init__(self, mode='i'):
        self.mode = mode

    def _get_back(self, frst_arg: int, scnd_arg: int, res: int, action: str) -> int:
        '''
        Возвращает результат математических операций
        Еели режим работы mode='i' - интерактивный режим, печатает результат в консоль,
        если режим работы mode='r' - возвращает значение int or float
        :param frst_arg: int or float
        :param scnd_arg: int or float
        :param res: int or float
        :param action: str: +, -, /, *
        :return: int or str
        '''

        if self.mode == 'i':
            print(f'{frst_arg} {action} {scnd_arg} = {res}')
            output = True
        elif self.mode == 'r':
            output = res
        return output

    @staticmethod
    def _check_type(frst_arg: int, scnd_arg: int,) -> bool:
        '''
        Проводит проверку типов
        :param frst_arg: int or float
        :param scnd_arg: int or float
        :return: bool
        '''
        if isinstance(frst_arg, (int, float)) and isinstance(scnd_arg, (int, float)):
            output = True
        else:
            raise TypeError(f'Математические между {type(frst_arg)} и {scnd_arg} невозможны')
        return output

    def sum(self, frst_arg: int, scnd_arg: int) -> int:
        '''
        Функция сложения, на вход принимает два аргумента, типа int or float
        :param frst_arg: int or float
        :param scnd_arg: int or float
        '''
        if self._check_type(frst_arg, scnd_arg):
            res = frst_arg + scnd_arg
            output = self._get_back(frst_arg, scnd_arg, res, '+')
        return output

    def subtr(self, frst_arg: int, scnd_arg: int) -> int:
        '''
        Функция вычитания, на вход принимает два аргумента, типа int or float
        :param frst_arg: int or float
        :param scnd_arg: int or float
        '''
        if self._check_type(frst_arg, scnd_arg):
            res = frst_arg - scnd_arg
            output = self._get_back(frst_arg, scnd_arg, res, '-')
        return output


    def mltp(self, frst_arg: int, scnd_arg: int) -> int:
        '''
        Функция умножения, на вход принимает два аргумента, типа int or float
        :param frst_arg: int or float
        :param scnd_arg: int or float
        '''
        if self._check_type(frst_arg, scnd_arg):
            res = frst_arg * scnd_arg
            output = self._get_back(frst_arg, scnd_arg, res, '*')
        return output

    def dvsn(self, frst_arg: int, scnd_arg: int) -> int:
        '''
        Функция деления, на вход принимает два аргумента, типа int or float
        :param frst_arg: int or float
        :param scnd_arg: int or float
        '''
        if self._check_type(frst_arg, scnd_arg):
            res = frst_arg / scnd_arg
            output = self._get_back(frst_arg, scnd_arg, res, '/')
        return output
print(isinstance('a', (int, float)))
if __name__ == '__main__':

    calc = Calc('i')

    ARG_A = 10
    ARG_B = 2

    print('Calculator, mode="i"')
    calc.sum(ARG_A, ARG_B)
    calc.subtr(ARG_A, ARG_B)
    calc.mltp(ARG_A, ARG_B)
    calc.dvsn(ARG_A, ARG_B)

    clc = Calc('r')
    print('Calculator, mode="r"')
    print(clc.sum(ARG_A, ARG_B))
    print(clc.subtr(ARG_A, ARG_B))
    print(clc.mltp(ARG_A, ARG_B))
    print(clc.dvsn(ARG_A, ARG_B))
