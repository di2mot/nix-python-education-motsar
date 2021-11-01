"""Binary Search Tree
A binary search tree is a binary tree where the nodes are ordered in a specific way.
"""


class Node:
    """class by Node"""

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    """Binary Search Tree class

    insert - add an element,
    lookup - find an element by value and return a link to it (node),
    delete - delete an element by value
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, data):
        """lookup - find an element by value and return a link to it (node)"""

        last = self.head

        while last:
            if last.data < data:
                last = last.right
            elif last.data > data:
                last = last.left
            elif last.data == data:
                return last

    def insert(self, data):
        """insert - add an element,"""
        if not isinstance(data, int):
            raise TypeError("Type must be <class 'int'>")

        if self.head is None:
            self.head = Node(data=data)
            self.length += 1
            return

        last = self.head

        while True:
            if last.data > data:
                if last.left is None:
                    last.left = Node(data)
                    self.length += 1
                    break
                last = last.left

            elif last.data < data:
                if last.right is None:
                    last.right = Node(data)
                    self.length += 1
                    break
                else:
                    last = last.right
            else:
                self.length += 1
                break

    @staticmethod
    def _min_value(last):
        """find min value in left"""
        while last.left is not None:
            last = last.left
        return last

    def delete(self, data):
        """ delete - delete an element by value"""
        if not isinstance(data, int):
            raise TypeError("Type must be <class 'int'>")
        # check case tree is empty
        if self.head is None:
            raise ValueError("Not find in tree")

        last = self.head
        self._delete(last, data)
        self.length -= 1

    def _delete(self, last, data):
        """recursive function"""
        # if value not found in tree
        if last is None:
            raise ValueError("Not <binarytree.Node object>")

        if data < last.data:
            last.left = self._delete(last=last.left, data=data)

        elif data > last.data:
            last.right = self._delete(last=last.right, data=data)

        else:
            if last.left is None:
                last = last.right
                return last

            if last.right is None:
                last = last.left
                return last

            temp = self._min_value(last.right)
            last.data = temp.data
            last.right = self._delete(last.right, temp.data)

        return last

    def printTree(self):
        last = self.head

        def printer(last):
            if last.left:
                printer(last.left)
            print(last.data)
            if last.right:
                printer(last.right)
        printer(last)

    root = Node(12)





