"""A hash table organizes data so you can quickly look up values for a given key."""


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None
        self.hash = None


class HashTable:
    """HashTable class
    insert - добавить элемент с ключом (индекс = хеш_функция(ключ)),
    lookup - получить значение по ключу,
    delete - удалить значение по ключу
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, key):
        """Find index of element"""
        print(hash(key))
        key = hash(key)
        last = self.head
        res = None
        for i in range(self.length):
            if key != last.hash:
                last = last.next_data
            elif key == last.hash:
                res = last.data
                break
        if res is None:
            raise KeyError(f'Variable {hash} not found')
        return res

    def insert(self, data, key):
        """  prepend - добавить в начало списка элемент """
        new_head = Node(data)
        new_head.next_data = self.head
        new_head.hash = hash(key)
        self.head = new_head
        self.length += 1



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

    def __len__(self):
        """Add len function"""
        return self.length
