"""
Реалізуйте структуру даних зв`язний список з поточним елементом та реалізуйте додаткові операції для роботи зі списком
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.front = None
        self.curr = None

    def empty(self):
        return self.front is None

    def reset(self):
        self.curr = self.front

    def next(self):
        if self.empty():
            raise StopIteration
        if self.curr.next is None:
            raise StopIteration

        self.curr = self.curr.next

    def current(self):
        if self.empty():
            raise RuntimeError

        return self.curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.curr = node
            return

        node.next = self.curr.next
        self.curr.next = node

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.curr = node
            return

        if self.front is self.curr:
            node.next = self.front
            self.front = node
            return

        prev = self.front
        while prev.next is not self.curr:
            prev = prev.next

        node.next = self.curr
        prev.next = node

    def delete(self):
        if self.empty():
            return

        if self.front is self.curr:
            self.front = self.curr = self.front.next
            return

        prev = self.front
        while prev.next is not self.curr:
            prev = prev.next

        prev.next = self.curr.next
        if self.curr.next is None:
            self.curr = prev
        else:
            self.curr = self.curr.next

    def damp(self):
        array = []
        curr = self.front
        while curr is not None:
            array.append(curr.item)
            curr = curr.next
        return array


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


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    lst.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.delete()


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return lst.damp()

