"""My Data Strucures"""

class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class LinkedList:
    """LinkedList class

    prepend - добавить в начало списка элемент,
    append - добавить в конец списка,
    lookup - найти индекс элемента по значению (первого попавшегося),
    insert - вставить элемент на конкретный индекс со сдвигом элементов направо,
    delete - удалить элемент по индексу),
    """

    def __init__(self):
        self.head = None
        self.length = 0
        self.start = 0

    def lookup(self, data):
        """Find index of element"""
        index = 0
        last = self.head
        res = None
        if last:
            while last:
                if data != last.data:
                    last = last.next_data
                elif data == last.data:
                    res = index
                    break
                index += 1
        if res is None:
            res = None
            # raise KeyError(f'Variable {data} not found')
        return res

    def prepend(self, data):
        """  prepend - добавить в начало списка элемент """
        new_head = Node(data)
        new_head.next_data = self.head
        self.head = new_head
        self.length += 1

    def append(self, new_data):
        """  append - добавить в конец списка """
        new_node = Node(data=new_data)
        # print(new_node)

        # if self.head is empty, its will be start of list
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last = self.head
        # print(self.head)
        while (last.next_data):
            last = last.next_data
        last.next_data = new_node
        self.length += 1


    def insert(self, data, index):
        """ вставить элемент на конкретный индекс со сдвигом элементов направо"""
        if not isinstance(index, int):
            raise ValueError(f"index must be <class 'int'>, not {type(index)}")

        if index == 0:
            # Если индекс == 0, то запускаем self.prepend(data)
             self.prepend(data)
        elif index > self.length:
            # Если индекс больше длинны списка, то райзим ошибку.
            print("Index error, index outside list")
        else:
            last = self.head
            for temp_index in range(self.length):
                # print(f"last.data: {last.data}, temp_index: {temp_index}")
                # if temp_index < index:
                #     # переходим к следующему элементу последоватальности
                #     last = last.next_data

                if temp_index == index-1:
                    # нашли нужный индекс
                    new_head = Node(data)

                    new_head.next_data = last.next_data
                    last.next_data = new_head
                    self.length += 1
                    return
                last = last.next_data
            raise IndexError("End of list, element not found")

    def delete(self, index):
        """  удалить элемент по индексу """
        if not isinstance(index, int):
            raise ValueError(f"index must be <class 'int'>, not {type(index)}")

        if index > self.length:
            # Если индекс больше длинны списка, то райзим ошибку.
            raise IndexError("Index error, index outside list")

        priv = self.head
        last = self.head
        for temp_index in range(self.length):
            print(f"priv: {priv.data}, last.data: {last.data}, temp_index: {temp_index}")

            if temp_index == index:
                # нашли нужный индекс
                priv.next_data = last.next_data
                self.length -= 1
                return
            priv = last
            last = last.next_data

    def get_item(self):
        """return link to object"""

        last = self.head
        if last:
            count = 0
            while last:
                if count != self.start:
                    last = last.next_data
                elif count == self.start:
                    self.start += 1
                    # print(last.data)
                    return last.data
                elif count > self.length:
                    raise StopIteration
                count += 1

    def __next__(self):
        return self.get_item()

    def __len__(self):
        """Add len function"""
        return self.length
