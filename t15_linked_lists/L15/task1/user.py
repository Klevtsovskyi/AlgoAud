#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None

    def empty(self):
        return self.head is None

    def reset(self):
        self.curr = self.head

    def next(self):
        if self.empty() or self.curr.next is None:
            raise StopIteration
        else:
            self.curr = self.curr.next

    def current(self):
        if self.empty():
            return None
        else:
            return self.curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.head = self.curr = node
        else:
            node.next = self.curr.next
            self.curr.next = node


def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = LinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def reset():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.reset()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    lst.insert_after(item)


