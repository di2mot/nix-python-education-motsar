import math
import pytest

from random_generator import RandomNumbers
from binary_search import binary_search
from quick_sort import quick_sort
from factorial_algoritm import factorial

@pytest.mark.parametrize('input', [3, 7, 12, 21, 37, 73])
def test_quick_sort(input):
    rand = RandomNumbers(1, 100, input)
    lst = list(rand.sorted_numbers)
    uns_lst = list(rand.unsorted_numbers)
    assert quick_sort(uns_lst) == lst, "Expected True"


@pytest.mark.parametrize('input', [3, 7, 12, 21, 37, 73])
def test_binary_search(input):
    rand = RandomNumbers(1, 100, 100)
    lst = list(rand.sorted_numbers)
    assert binary_search(lst, lst[input]) == lst.index(lst[input]), "Expected True"


def test_error_binary_search():
    lst = list()
    with pytest.raises(ValueError, match=r'List is empty'):
        binary_search(lst, 5)


def test_quick_sort():
    rand = RandomNumbers(1, 100, 100)
    lst = list(rand.sorted_numbers)
    uns_lst = list(rand.unsorted_numbers)
    assert quick_sort(uns_lst) == lst, "Expected True"


@pytest.mark.parametrize('input', [3, 7, 12, 21, 37, 73])
def test_factorial(input):
    assert factorial(input) == math.factorial(input),  f"Expected {math.factorial(input)}"
