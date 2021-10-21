""" Quick sort """


def quick_sort(uns_lst):
    """ Algorithm of Quick sort """

    lst = uns_lst

    index_list = list()
    index_list.append([0, len(uns_lst) - 1])

    for indexes in index_list:

        print(indexes)
        print(lst)
        currel = indexes[0]
        pivot_ind = indexes[1]

        while pivot_ind > currel:
            # print(f"currel: {currel}, pivot_ind: {pivot_ind}, lst[pivot_ind]: {lst[pivot_ind]}")

            pivot = lst[pivot_ind]

            if lst[currel] > pivot:
                lst[pivot_ind], lst[currel] = lst[currel], lst[pivot_ind - 1]

                lst[pivot_ind - 1] = pivot
                pivot_ind -= 1
                # print(f"lst[pivot_ind - 1]: {lst[pivot_ind - 1]}, pivot_ind: {pivot_ind}")

            else:
                currel += 1

        low = indexes[0]
        high = indexes[1]

        if pivot_ind > 1 and low < pivot_ind - 1:
            index_list.append((low, pivot_ind - 1))

        if pivot_ind < len(lst) - 1 and pivot_ind + 1 < high:
            index_list.append((pivot_ind + 1, high))

    return lst

