"""Binary search"""


def binary_search(lst: list, value: int) -> int:
    """Binary search algorithm"""

    if len(lst) == 0:
        raise ValueError("List is empty")
    if len(lst) == 1:
        return lst[0]

    start = 0
    fin = len(lst) // 2
    i = 0
    while True:
        sort_slice = lst[start: fin]
        if value <= sort_slice[-1]:
            for n in range(len(sort_slice)):
                if sort_slice[n] == value:
                    return i
                i += 1
                if i > len(lst):
                    raise ValueError("Not found")
        else:
            i += fin
            start = fin
            fin = len(lst)

