#!/usr/bin/python3
"""a class Square that manages: size
"""


class Node:
    """a class Node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if value is None:
            self.__data = value
        else:
            if not isinstance(value, int):
                raise TypeError('data must be an integer')
            else:
                self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not value:
            self.__next_node = value
        else:
            if not isinstance(value, Node):
                raise TypeError('next_node must be a Node object')
            else:
                self.__next_node = value


class SinglyLinkedList:
    """a class SinglyLinkedList
    """
    def __init__(self):
        self.__head = Node(None)

    def __str__(self):
        ss = ""
        cur = self.__head
        while cur.next_node is not None:
            ss += str(cur.data)
            ss += '\n'
            cur = cur.next_node
        ss += str(cur.data)
        ss += '\n'
        return ss[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        cur = self.__head
        if cur is None:
            self.__head = new
        elif cur.data is None:
            cur.data = value
        else:
            if value <= cur.data:
                new.next_node = self.__head
                self.__head = new
            else:
                while cur.next_node is not None:
                    if value < cur.next_node.data:
                        break
                    cur = cur.next_node
                new.next_node = cur.next_node
                cur.next_node = new
