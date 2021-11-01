"""My Data Strucures"""


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class LinkedList:
    """LinkedList class

    prepend - add an element to the beginning of the list,
    append - add to the end of the list,
    lookup - find the index of an element by value (the first one found),
    insert - insert an element at a specific index with shift of elements to the right,
    delete - delete an element by index,
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
        """  prepend - add an element to the beginning of the list """
        new_head = Node(data)
        new_head.next_data = self.head
        self.head = new_head
        self.length += 1

    def append(self, new_data):
        """  append - add to the end of the list """
        new_node = Node(data=new_data)

        # if self.head is empty, its will be start of list
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last = self.head
        while (last.next_data):
            last = last.next_data
        last.next_data = new_node
        self.length += 1

    def insert(self, data, index):
        """ insert - insert an element at a specific index with shift of elements to the right"""
        if not isinstance(index, int):
            raise ValueError(f"index must be <class 'int'>, not {type(index)}")

        if index == 0:
            # If index == 0, then start self.prepend(data)
             self.prepend(data)
        elif index > self.length:
            print("Index error, index outside list")
        else:
            last = self.head
            for temp_index in range(self.length):

                if temp_index == index-1:
                    # if find index
                    new_head = Node(data)

                    new_head.next_data = last.next_data
                    last.next_data = new_head
                    self.length += 1
                    return
                last = last.next_data
            raise IndexError("End of list, element not found")

    def delete(self, index):
        """  delete - delete an element by index """
        if not isinstance(index, int):
            raise TypeError(f"index must be <class 'int'>, not {type(index)}")

        if index > self.length:
            # Is index > then length of list.
            raise IndexError("Index error, index outside list")

        priv = self.head
        last = self.head

        if index == 0:
            self.head = self.head.next_data
            self.length -= 1
            return

        for temp_index in range(self.length):
            if temp_index == index:
                # if find index
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
                    return last.data
                elif count > self.length:
                    self.start = 0
                    raise StopIteration
                count += 1

    def __next__(self):
        return self.get_item()

    def __len__(self):
        """Add len function"""
        return self.length
