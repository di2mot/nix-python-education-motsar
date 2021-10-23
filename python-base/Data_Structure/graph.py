"""Graph"""
from linkedlist import LinkedList


class Vertex:
    """class by Vertex

    Создаётся экземпляр класа Vertex где
    vertex_name - одна из вершин графа
    edges - все вершины с которыми соприкосается дннный граф
    """

    def __init__(self, vertex_name=None):
        self.edges = LinkedList()
        self.vertex_name = vertex_name

class VertCarier:
    def __init__(self):
        self.vertexes = LinkedList()

class Graph:
    """
    insert- добавить узел и связи с другими узлами по ссылкам,
    lookup - найти узел по значению и вернуть ссылку на него,
    delete - удалить узел по ссылке и связи с другими узлами """

    def __init__(self):
        # vertex_edges - список всех вершин в графе
        self.vertexes = LinkedList()
        self.length = 0
        self.vert_name_list = LinkedList()

    def insert(self, vertex_name, vertex_edges):
        """insert- добавить узел и связи с другими узлами по ссылкам"""
        print("-" * 100, "\ndef insert\n", "-" * 100)
        # print(f"33. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")
        # print(f"34. self.vert_name_list.lookup({vertex_edges}) {self.vert_name_list.lookup(vertex_edges)}")

        # проверяю, есть ли элементы в списке вершин
        if self.vert_name_list.lookup(vertex_name) is None:
            print(f"39. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")
            self._insert(vertex_name, vertex_edges)
        print(f"40. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")

        temp_link = self._lookup(vertex_name)
        # print(f"44. temp_link: {temp_link.edges.lookup(vertex_edges)}")

        if self.vert_name_list.lookup(vertex_edges) is None:
            print(f"47. self.vert_name_list.lookup({vertex_edges}) {self.vert_name_list.lookup(vertex_edges)}")
            self._insert(vertex_edges, vertex_name)

        print(f"50. self.vert_name_list.lookup({vertex_edges}) {self.vert_name_list.lookup(vertex_edges)}, {vertex_edges}")
        print(f"61. self._lookup: {self._lookup(vertex_edges)}")

        # self._append(vertex_name, vertex_edges)
        # self._append(vertex_edges, vertex_name)

    def _append(self, vertex, edges):
        link = self._lookup(vertex)
        print(link)
        link.edges.append(edges)


    def _insert(self, vertex_name, vertex_edges):
        """Функция для поиска и добавления вершины и связи между ними """
        temp = Vertex(vertex_name)
        temp.edges.append(vertex_edges)
        temp.vertex_name = vertex_name
        # append new vertex to list of vertex_edges
        self.vertexes.append(temp)
        self.vert_name_list.append(vertex_name)
        self.length += 1




    def lookup(self, vertex):
        """lookup - найти узел по значению и вернуть ссылку на него"""
        print("-" * 100, "\n START def lookup\n", "-" * 100)
        if self.vert_name_list.lookup(vertex) is None:
            print(f"Vertex {vertex} not found in Graph. Make graph.insert(vertex, edges)")
            return False
        print(f"106. self.vert_name_list.lookup(vertex): {self.vert_name_list.lookup(vertex)}")
        for i in range(self.vert_name_list.length):
            link = next(self.vertexes)
            print(f"109. i: {i}, link = next(self.vertexes): {link}. link.vertex_name: {link.vertex_name}")
            if link.vertex_name == vertex:
                print(f"111. link.vertex_name: {link.vertex_name}")
                print("-" * 100, "\n END def lookup\n", "-" * 100)
                return link

    def _lookup(self, vertex):
        """lookup gelp function"""
        # print(vertex)
        res = False
        for i in range(self.vert_name_list.length):
            print(f"97. self.vertexes: {self.vertexes}")
            link = next(self.vertexes)
            print(link)
            if link.vertex_name == vertex:
                print(f"101. _lookup.link.vertex_name: {link.vertex_name}")
                res = link
        return res


    def delete(self, vertex):
        """delete function"""
        # print(vertex)
        for i in range(self.vert_name_list.length):
            link = next(self.vertexes)
            print(f"112. link.vertex_name: {link.vertex_name}")
            v = link.edges.lookup('a')
            print(f"114. v: {v}")




