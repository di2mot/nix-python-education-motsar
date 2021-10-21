import math

from random_generator import RandomNumbers
from binary_search import binary_search
from quick_sort import quick_sort
from factorial_algoritm import factorial


rand = RandomNumbers(1, 20, 15)
lst = list(rand.sorted_numbers)
uns_lst = list(rand.unsorted_numbers)
number = 5

def test_quick_sort(lst, uns_lst):
    assert quick_sort(uns_lst) == lst, "Expected True"


def test_binary_search(lst):
    ind = 73
    assert binary_search(lst, lst[ind]) == ind, "Expected True"


def test_quick_sort(uns_lst, lst):
    assert quick_sort(uns_lst) == lst, "Expected True"


def test_factorial(number):
    assert factorial(number) == math.factorial(number),  f"Expected {math.factorial(number)}"



