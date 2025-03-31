#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next: [Node | None] = None


head: [Node | None] = None
curr: [Node | None] = None


def init():
    """ Викликається один раз на початку виконання програми. """
    global head, curr
    head = None
    curr = None


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return head is None


def reset():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global curr
    curr = head


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global curr
    if empty() or curr.next is None:
        raise StopIteration
    curr = curr.next


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return curr.item


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global head, curr
    node = Node(item)
    if empty():
        head = curr = node
        return

    node.next = curr.next
    curr.next = node
