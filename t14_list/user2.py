#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних двобічно зв'язний список з поточним елементом.
"""

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.curr = None
        self.size = 0

    def empty(self): return self.curr is None
    def len(self): return self.size
    def set_first(self): self.curr = self.first
    def set_last(self): self.curr = self.last

    def next(self):
        if not self.empty() and self.curr.next:
            self.curr = self.curr.next
        else:
            raise StopIteration

    def prev(self):
        if not self.empty() and self.curr.prev:
            self.curr = self.curr.prev
        else:
            raise StopIteration

    def current(self):
        return self.curr.item if self.curr else None

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.curr = self.first = self.last = node
        else:
            node.prev = self.curr
            if self.curr.next:
                node.next = self.curr.next
                node.next.prev = node
            else:
                self.last = node
            node.prev.next = node
        self.size += 1

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.curr = self.first = self.last = node
        else:
            node.next = self.curr
            if self.curr.prev:
                node.prev = self.curr.prev
                node.prev.next = node
            else:
                self.first = node
            node.next.prev = node
        self.size += 1

    def damp(self):
        array = []
        current = self.first
        while current:
            array.append(current.item)
            current = current.next
        return array

    def delete(self):
        if self.empty():
            return
        elif self.first is self.curr:
            if self.curr.next:
                self.first = self.curr = self.curr.next
                self.curr.prev = None
            else:
                self.__init__()
                return
        else:
            self.curr.prev.next = self.curr.next
            if self.curr.next:
                self.curr.next.prev = self.curr.prev
                self.curr = self.curr.next
            else:
                self.last = self.curr = self.curr.prev
        self.size -= 1

    def swap_prev(self):
        if self.curr.prev:
            prev = self.curr.prev
            self.curr.prev = prev.prev
            prev.next = self.curr.next
            if prev.prev:
                prev.prev.next = self.curr
            else:
                self.first = self.curr
            if self.curr.next:
                self.curr.next.prev = prev
            else:
                self.last = prev
            self.curr.next = prev
            prev.prev = self.curr

    def swap_next(self):
        if self.curr.next:
            self.curr.item, self.curr.next.item = self.curr.next.item, self.curr.item
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

    Переставляє поточний елемент на останній елемент списку
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


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return lst.damp()


def len():
    """ Повертає кількість елементів у списку

    :return: кількість елементів у списку
    """
    return lst.len()


def swap_prev():
    """ Міняє місцями поточний елемент списку з попереднім
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не перший у списку
    Поточний елемент лишається не змінним
    """
    lst.swap_prev()


def swap_next():
    """ Міняє місцями поточний елемент списку з наступним
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не останній у списку
    Поточний елемент лишається не змінним
    """
    lst.swap_next()


if __name__ == '__main__':
    init()
    insert_after(0)
    insert_after(2)
    insert_before(-2)
    insert_after(1)
    insert_before(-1)
    print(damp())
