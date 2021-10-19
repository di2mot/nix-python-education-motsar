"""Graph"""
from linkedlist import LinkedList


class Vertex:
    """class by Vertex

    Создаётся экземпляр класа Vertex где
    vertex_name - одна из вершин графа
    edges - все вершины с которыми соприкосается дннный граф
    """

    def __init__(self, vertex_name=None):
        self.vertex_name = vertex_name
        self.edges = LinkedList()


class Graph:
    """
    insert- добавить узел и связи с другими узлами по ссылкам,
    lookup - найти узел по значению и вернуть ссылку на него,
    delete - удалить узел по ссылке и связи с другими узлами"""

    def __init__(self):
        # vertexes - список всех вершин в графе
        self.vertexes = LinkedList()
        self.length = 0
        self.vert_name_list = LinkedList()

    def insert(self, vertex_name, vertexes):
        """insert- добавить узел и связи с другими узлами по ссылкам"""
        print("-" * 100, "\ndef insert\n", "-" * 100)
        print(f"33. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")
        print(f"34. self.vert_name_list.lookup({vertexes}) {self.vert_name_list.lookup(vertexes)}")

        # проверяю, есть ли элементы в списке вершин

        if self.vert_name_list.lookup(vertex_name) is None:
            # print(f"39. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")
            temp = Vertex(vertex_name)
            temp.edges.append(vertexes)

            # append new vertex to list of vertexes
            self.vertexes.append(temp)
            self.vert_name_list.append(vertex_name)
            self.length += 1
        print(f"47. self.vert_name_list.lookup({vertex_name}) {self.vert_name_list.lookup(vertex_name)}")

        if self.vert_name_list.lookup(vertexes) is None:
            # print(f"50. self.vert_name_list.lookup({vertexes}) {self.vert_name_list.lookup(vertexes)}")
            temp = Vertex(vertexes)
            temp.edges.append(vertex_name)

            # append new vertex to list of vertexes
            self.vertexes.append(temp)
            self.vert_name_list.append(vertexes)
            self.length += 1
        print(f"58. self.vert_name_list.lookup({vertexes}) {self.vert_name_list.lookup(vertexes)}")

        print(f"60. self.lookup('a'): {self.lookup('a')}")
        self._insert(vertex_name, vertexes)
        print(f"62. CHECK: self._insert({vertex_name}, {vertexes}): COMPLETE")
        # а теперь делаем операцию наоборот
        self._insert(vertexes, vertex_name)
        print(f"65. CHECK: self._insert({vertexes}, {vertex_name}): COMPLETE")

    def _insert(self, vertex_name, vertexes):
        """Функция для поиска и добавления вершины и связи между ними """
        # проходим по списку вершин
        find = False
        print(f"71. vertex_name: {vertex_name}, vertexes: {vertexes}, self.vertexes.length: {self.vertexes.length}")

        for i in range(self.vertexes.length):
            # линк это ссылка на вершину, т.е. на class Vertex
            link = next(self.vertexes)
            # print(vertex_name, vertexes, link)
            # когда получили вершину, проверяем, это та вершина что нам нужно или нет
            # если link.vertex_name та что нам нужно
            print(f"79. LINK: {link}")
            if link is not None:
                break
            if link.vertex_name == vertex_name:
                # если link.vertex_name та что нам нужно, проверяем,
                # содержит ли она нужную вязь vertexes, и если не содержит
                # добавляем новую связь
                find = True
                if not link.edges.lookup(vertexes):
                    link.edges.append(vertexes)
                break
        if not find:
            print(f"91. APPEND {vertexes} to list of vertexes")
            temp = Vertex(vertex_name)
            temp.edges.append(vertexes)
            # append new vertex to list of vertexes
            self.vertexes.append(temp)




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



    def delete(self):
        ...



