""" A stack stores items in a last-in, first-out (LIFO) order. """


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class Stack:
    """ class for Stack
    push - add an item to the stack,
    pop - remove the last element,
    peek - get the value of the extreme element of the stack"""

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        """push - add an item to the stack"""
        new_head = Node(data)
        new_head.next_data = self.head
        self.head = new_head
        self.length += 1

    def pop(self):
        """ pop - remove the last element"""
        if self.length > 0:

            res = self.head.data
            self.head = self.head.next_data
            self.length -= 1
            return res
        raise IndexError("Stack is empty")

    def peek(self):
        """peek - get the value of the extreme element of the stack"""
        if self.length > 0:
            res = self.head.data
            return res
        raise IndexError("Stack is empty")

    def __len__(self):
        """Add len function"""
        return self.length
