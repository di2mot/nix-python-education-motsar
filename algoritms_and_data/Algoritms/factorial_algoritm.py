""" Recursive factorial implementation """


def factorial(number):
    """factorial algorithm"""
    if number == 1:
        return number
    else:
        res = number * factorial(number-1)
        return res
