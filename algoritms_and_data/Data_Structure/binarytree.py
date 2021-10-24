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

    insert - добавить элемент,
    lookup - найти элемент по значению и вернуть ссылку на него (узел),
    delete - удалить элемент по значению
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, data):
        """lookup - найти элемент по значению и вернуть ссылку на него (узел)"""

        last = self.head

        while last:
            if last.data < data:
                last = last.right
            elif last.data > data:
                last = last.left
            elif last.data == data:
                return last

    def insert(self, data):
        """insert - добавить элемент"""

        if self.head is None:
            self.head = Node(data=data)
            self.length += 1
            return

        last = self.head

        while True:
            if last.data > data:
                if last.left is None:
                    last.left = Node(data)
                    break
                last = last.left

            elif last.data < data:
                if last.right is None:
                    last.right = Node(data)
                    break
                else:
                    last = last.right
            else:
                break

    @staticmethod
    def _min_value(last):
        """find min value in left"""
        while last.left is not None:
            last = last.left
        return last

    def delete(self, data):
        """delete - удалить элемент по значению"""
        # check case tree is empty
        if self.head is None:
            raise IndexError("Not find in tree")

        last = self.head

        self._delete(last, data)

    def _delete(self, last, data):
        """recursive function"""
        # if value not found in tree
        # print(last)
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





