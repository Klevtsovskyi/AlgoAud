#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних двбічнооднозв'язний список з поточним елементом.
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.curr = None
        self.first = None
        self.last = None

    def empty(self):
        return self.curr is None

    def set_first(self):
        self.curr = self.first

    def set_last(self):
        self.curr = self.last

    def next(self):
        if self.empty() or self.curr is self.last:
            raise StopIteration
        else:
            self.curr = self.curr.next

    def prev(self):
        if self.empty() or self.curr is self.first:
            raise StopIteration
        else:
            self.curr = self.curr.prev

    def current(self):
        if self.empty():
            return None
        else:
            return self.curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.curr = self.first = self.last = node
        else:
            node.prev = self.curr
            node.next = self.curr.next
            self.curr.next = node
            if node.next is None:
                self.last = node
            else:
                node.next.prev = node

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.curr = self.first = self.last = node
        else:
            node.next = self.curr
            node.prev = self.curr.prev
            self.curr.prev = node
            if node.prev is None:
                self.first = node
            else:
                node.prev.next = node

    def delete(self):
        if self.empty():
            return
        elif self.curr is self.first:
            self.curr = self.first = self.curr.next
            if self.curr is None:
                self.last = None
            else:
                self.curr.prev = None
        else:
            self.curr.prev.next = self.curr.next  # <- Помилка була тут
            if self.curr is self.last:
                self.curr = self.last = self.curr.prev
                self.curr.next = None
            else:
                self.curr.next.prev = self.curr.prev  # <- Помилка була тут
                self.curr = self.curr.next


def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = DoublyLinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def set_first():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_first()


def set_last():
    """ Зробити поточними останній елемент списку

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_last()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    lst.prev()


def current():
    """ Повертає навантаження поточного елементу.

    :return: Навантаження поточного елементу
    """
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    lst.insert_after(item)


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    lst.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    """
    lst.delete()

