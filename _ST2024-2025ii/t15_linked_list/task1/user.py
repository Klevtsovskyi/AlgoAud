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
        self._head = None
        self._curr = None

    def empty(self):
        return self._head is None

    def reset(self):
        self._curr = self._head

    def next(self):
        if self.empty() or self._curr.next is None:
            raise StopIteration
        self._curr = self._curr.next

    def current(self):
        return self._curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self._head = self._curr = node
            return

        node.next = self._curr.next
        self._curr.next = node


lst: LinkedList


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
    """ Робить перший елемент списку, поточним.

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
