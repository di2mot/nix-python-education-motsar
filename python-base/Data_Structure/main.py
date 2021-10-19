from linkedlist import LinkedList
from queue import Queue
from stack import Stack
from hashtable import HashTable
from binarytree import BinarySearchTree
from graph import Graph

import hashlib

link = LinkedList()
# link.append('a')
# link.append('b')
# link.append('c')
# link.append('d')
# link.append('e')
# for i in range(4):
#     print(next(link))
# print(link.lookup('d'))
# link.prepend('f')
# print(link.lookup('d'))
# link.insert('g', 3)
# print(link.lookup('c'))
# link.delete(3)
# print(link.lookup('c'))
# print("len: ", len(link))

que = Queue()
# que.enqueue(1)
# que.enqueue(2)
# print(que.peek())
# print(len(que))
# print("dequeue", que.dequeue())
# print("peek ", que.peek())
# print("len: ", len(que))

stk = Stack()
# stk.push(1)
# stk.push(2)
# stk.push(3)
# print((stk.pop()))
# print((stk.pop()))

# a = 'aaa'
# print(hash(a))


hsh = HashTable()
# hsh.insert(1, 'a')
# hsh.insert(2, 'b')
# hsh.insert(3, 'c')
# hsh.insert(4, 'd')
# hsh.insert(5, 'e')
# hsh.insert(6, 'f')
# print(hsh.lookup('d'))

bts = BinarySearchTree()
# bts.insert(12)
# bts.insert(34)
# bts.insert(10)
# bts.insert(52)
# bts.insert(20)
# bts.insert(25)
# bts.insert(19)
# bts.insert(76)
# bts.insert(90)
# bts.insert(68)
# bts.insert(40)
# bts.insert(27)
# bts.insert(28)
# bts.insert(26)
# bts.PrintTree()

# bts.delete(10)
# bts.PrintTree()
# bts.delete(34)
# bts.PrintTree()
# bts.insert(98)
# bts.PrintTree()

# print(bts.lookup(27))
l = LinkedList()
graph = Graph()
graph.insert("a", "b")
graph.insert("a", "c")
graph.insert("b", "c")
graph.lookup("c")