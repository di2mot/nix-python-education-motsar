""" Quick sort """


def quick_sort(uns_lst: list) -> list:
    """Algorithm of Quick sort"""
    if len(uns_lst) == 0:
        raise ValueError("List is empty")
    if len(uns_lst) == 1:
        return uns_lst[0]

    lst = uns_lst

    while True:
        status = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                status = False
                x = lst[i]
                y = lst[i + 1]
                lst[i], lst[i + 1] = y, x
        if status:
            return lst
