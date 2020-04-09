#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class ListWithCurrent:

    def __init__(self):
        self.head = None
        self.curr = None

    def empty(self):
        return self.head is None

    def reset(self):
        self.curr = self.head

    def next(self):
        if self.empty() or not self.curr.next:
            raise StopIteration
        else:
            self.curr = self.curr.next

    def current(self):
        return self.curr.item if not self.empty() else None

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.head = self.curr = node
        else:
            node.next = self.curr.next
            self.curr.next = node

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.head = self.curr = node
        elif self.head is self.curr:
            node.next = self.curr
            self.head = node
        else:
            prev = self.head
            while prev.next is not self.curr:
                prev = prev.next
            node.next = self.curr
            prev.next = node
            
    def delete(self):
        if self.empty():
            return
        elif self.head is self.curr:
            if self.curr.next:
                self.head = self.curr = self.curr.next
            else:
                self.__init__()
        else:
            prev = self.head
            while prev.next is not self.curr:
                prev = prev.next
            prev.next = self.curr.next
            self.curr = self.curr.next if self.curr.next else prev

    def damp(self):
        array = []
        current = self.head
        while current:
            array.append(current.item)
            current = current.next
        return array


def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = ListWithCurrent()


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


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return lst.damp()


if __name__ == '__main__':
    t = ListWithCurrent()
    t.insert_after(1)
    t.insert_before(0)
    print(t.damp())
    t.next()
    print(t.current())
