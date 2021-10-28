"""A hash table organizes data so you can quickly look up values for a given key."""


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None
        self.hash = None


class HashTable:
    """HashTable class
    insert - add an element with a key (index = hash_function (key)),
    lookup - get value by key,
    delete - delete a value by key
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, key):
        """Find index of element"""
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
        """  insert - add an element with a key (index = hash_function (key)) """
        new_head = Node(data)
        new_head.next_data = self.head
        new_head.hash = hash(key)
        self.head = new_head
        self.length += 1

    def delete(self, index):
        """  delete - delete a value by key """
        if not isinstance(index, int):
            raise ValueError(f"index must be <class 'int'>, not {type(index)}")

        if index > self.length:
            # If the index is longer than the list, then the error is raised.
            raise IndexError("Index error, index outside list")

        priv = self.head
        last = self.head
        for temp_index in range(self.length+1):
            if temp_index == index:

                # found the desired index
                if last:
                    priv.next_data = last.next_data
                else:
                    priv.next_data = last
                self.length -= 1
                return
            priv = last
            last = last.next_data

    def __len__(self):
        """Add len function"""
        return self.length
