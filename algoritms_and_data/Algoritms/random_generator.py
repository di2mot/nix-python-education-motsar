import numpy


class RandomNumbers:
    """ Generates sequences of random numbers and compares them"""

    def __init__(self, start=-10, stop=100, amount=100):
        self.unsorted_numbers = None
        self.sorted_numbers = None
        self._start = start
        self._stop = stop
        self._amount = amount
        self.make_numbers()

    @staticmethod
    def _create_random_numbers(start, stop, amount):
        """"""
        v1 = list(numpy.random.randint(start, stop, amount))
        return v1

    def make_numbers(self):
        """  """
        start = self._start
        stop = self._stop
        amount = self._amount
        sequence = self._create_random_numbers(start, stop, amount)
        self.unsorted_numbers = sequence
        self.sorted_numbers = sorted(sequence)

    def check_result(self, numbers):
        """Checker"""

        res = None
        if self.sorted_numbers == numbers:
            res = True
        else:
            res = False
        return res


