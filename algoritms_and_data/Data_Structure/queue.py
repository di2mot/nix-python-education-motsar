"""A queue stores items in a first-in, first-out (FIFO) order."""


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class Queue:
    """queue class

    enqueue - add an element to the end of the queue,
    dequeue - remove an element from the head of the queue,
    peek - get the value of the element at the head of the queue"""

    def __init__(self):
        self.start = None
        self.head = None
        self.length = 0

    def enqueue(self, new_data):
        """enqueue - add an element to the end of the queue,"""
        new_node = Node(data=new_data)
        # print(new_node)

        # if self.head is empty, its will be start of list
        if self.head is None:
            self.start = new_node
            self.head = new_node
            self.length += 1
            return

        last = self.head
        # print(self.head)
        while (last.next_data):
            last = last.next_data
        last.next_data = new_node
        self.length += 1

    def peek(self):
        """dequeue - remove an element from the head of the queue"""
        return self.head.data

    def dequeue(self):
        """peek - get the value of the element at the head of the queue"""

        res = self.head.data
        self.head = self.head.next_data
        self.length -= 1
        return res

    def __len__(self):
        """Add len function"""
        return self.length
