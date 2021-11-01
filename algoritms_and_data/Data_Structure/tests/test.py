import random

import pytest
from queue import Queue
from linkedlist import LinkedList
from stack import Stack
from hashtable import HashTable
from binarytree import BinarySearchTree, Node
from graph import Graph, Vertex

from random import randint

"""                         TESTING LINKED LIST                    """


@pytest.fixture()
def linker_list():
    return LinkedList()


data_test_linked_list = [['a', 'b', 'c'],
             ['aasfasf', 'sdgwdhwd', 'sdfhsfhsfeh'],
             ['auf qubgekrgb', 'irng95hgb 18yt 19th3g', '823-t th43 bg3 4th4bt'],
             [1535, 'bgsnrh5', 13.2]]


@pytest.mark.parametrize("value", data_test_linked_list)
def test_linked_list(linker_list, value):
    """Testing Linked List"""

    # TEST VALUES
    a = 'test_value'
    a_index = 2

    """         check append function       """
    count_len = 0
    assert linker_list.length == count_len
    for element in value:
        count_len += 1
        linker_list.append(element)
        assert linker_list.length == count_len

    # check next() function
    for element in value:
        assert next(linker_list) == element

    # check lookup function
    for index, element in enumerate(value):
        assert linker_list.lookup(element) == index

    """         check insert function           """
    linker_list.insert(a, a_index)
    assert linker_list.lookup(a) == a_index, f"Index mast be {a_index}"

    """         check delete function           """
    # Check TypeError
    with pytest.raises(TypeError, match=r"index must be <class 'int'>, not <class 'str'>"):
        linker_list.delete(a)
    # Check IndexError
    with pytest.raises(IndexError, match=r"Index error, index outside list"):
        linker_list.delete(linker_list.length+1)

    # Check if deleta
    linker_list.delete(a_index)
    assert linker_list.lookup(a) == None, "must be None"

    """         check prepand function           """
    linker_list.prepend(a)
    assert linker_list.lookup(a) == 0, "Index must be 0"


"""                         TESTING QUEUE                    """


@pytest.fixture()
def queue():
    return Queue()


data_test_linked_list = [['a', 'b', 'c'],
             ['aasfasf', 'sdgwdhwd', 'sdfhsfhsfeh'],
             ['auf qubgekrgb', 'irng95hgb 18yt 19th3g', '823-t th43 bg3 4th4bt'],
             [1535, 'bgsnrh5', 13.2]]


@pytest.mark.parametrize("value", data_test_linked_list)
def test_queue(queue, value):
    """                 Testing QUEUE               """
    """         check enqueue function       """


    count_len = 0
    # Check start length
    assert queue.length == count_len

    # first element in queue
    first_element = value[0]

    for element in value:
        count_len += 1
        queue.enqueue(element)
        assert queue.length == count_len, f"Length must be {count_len}"

        # check if element in queue
        assert queue.peek() == first_element, f"Element must be {first_element}"

    # Check dequeue function
    for element in value:
        assert queue.dequeue() == element, f"Must be {element}"
        count_len -= 1


"""                         TESTING STACK                    """

@pytest.fixture()
def stack():
    return Stack()


data_test_linked_list = [['a', 'b', 'c'],
             ['aasfasf', 'sdgwdhwd', 'sdfhsfhsfeh'],
             ['auf qubgekrgb', 'irng95hgb 18yt 19th3g', '823-t th43 bg3 4th4bt'],
             [1535, 'bgsnrh5', 13.2]]


@pytest.mark.parametrize("value", data_test_linked_list)
def test_stack(stack, value):
    """Testing QUEUE"""
    """         check push function       """


    count_len = 0
    # Check start length
    assert stack.length == count_len
    for element in value:
        count_len += 1
        stack.push(element)
        assert stack.length == count_len, f"Length must be {count_len}"

    count_len = stack.length
    revers_value = value
    revers_value.reverse()

    # Check peek function
    assert stack.peek() == revers_value[0], f"Must be {revers_value[0]}"


    # Check pop function
    for element in revers_value:
        count_len -= 1
        assert stack.pop() == element, f"Must be {element}"
        assert stack.length == count_len, f"Must be {count_len}"


"""                         TESTING HASH TABLE                    """

@pytest.fixture()
def hashtable():
    return HashTable()


data_test_linked_list = [['a', 'b', 'c'],
             ['aasfasf', 'sdgwdhwd', 'sdfhsfhsfeh'],
             ['auf qubgekrgb', 'irng95hgb 18yt 19th3g', '823-t th43 bg3 4th4bt'],
             [1535, 'bgsnrh5', 13.2]]


@pytest.mark.parametrize("value", data_test_linked_list)
def test_hash_table(hashtable, value):
    """Testing QUEUE"""

    """         check insert function       """
    counter = 0
    # test length of hash table
    assert hashtable.length == 0, "Length must be 0"

    for index, element in enumerate(value):
        hashtable.insert(index, element)
        counter += 1
        assert hashtable.length == counter, f"Length must be {counter}"

        # Check if element in hashtable
        assert hashtable.lookup(element) == index, f"Index of {element} must be {index}"

        # Check KeyError
        with pytest.raises(KeyError):
            hashtable.lookup(index)

    """ Check delete function  """
    value.reverse()
    counter = hashtable.length
    for index, value in enumerate(value):

        with pytest.raises(ValueError):
            hashtable.delete(str(value))

        with pytest.raises(IndexError, match=r"Index error, index outside list"):
            hashtable.delete(hashtable.length + 10)

        hashtable.delete(counter)
        counter -= 1
        assert hashtable.length == counter, f'Length of hashteble must be {counter}'


"""                         TESTING Binary Search Tree                    """

@pytest.fixture()
def bst():
    return BinarySearchTree()

def gen_rand_list():
    """Generate random list"""
    n, m = random.randint(10, 20), random.randint(10, 20)

    res = [[randint(1, 10) for j in range(m)] for i in range(n)]
    return res

# Genetate random lust
data_test_linked_list = gen_rand_list()


@pytest.mark.parametrize("value", data_test_linked_list)
def test_binary_tree(bst, value):
    """Testing Binary Search Tree"""

    """         check insert function       """
    counter = 0
    # test length of bst
    assert bst.length == 0, "Length must be 0"

    for index, element in enumerate(value):
        bst.insert(element)
        counter += 1

        res = bst.lookup(element)
        assert isinstance(res, Node), "Type must be <class 'binarytree.Node'"

        assert bst.length == counter, f"Length must be {counter}"

    """Check delete function"""
    counter = bst.length
    with pytest.raises(TypeError, match=r"Type must be <class 'int'>"):
            bst.delete("a")

    bst.delete(value[len(value)//2])
    counter -= 1
    assert bst.length == counter, f'Length of bst must be {counter}'


"""                         TESTING GRAPH                    """

@pytest.fixture()
def graph():
    return Graph()


# Genetate random lust
data_test_graph = [[('a', 'b'), ('a', 'c'), ('c', 'b')],
                   [('a', 'f'), ('e', 'c'), ('k', 'b')],
                   [(5, 'b'), ('a', 33), ('c', 'b')]]


@pytest.mark.parametrize("value", data_test_graph)
def test_binary_tree(graph, value):
    """Testing graph"""

    """         check insert function       """
    # test length of bst
    assert graph.length == 0, "Length must be 0"

    for index, element in enumerate(value):
        graph.insert(element[0], element[1])

        assert graph.length != 0, "Length shouldn't be 0 "

        res = graph.lookup(element[0])
        assert isinstance(res, Vertex), "Type of res must be <class 'graph.Vertex'>"

    item = value[0][0]
    graph.delete(item)
    assert graph.lookup(item) == False, "Must be False"
