"""
Реалізуйте структуру даних двобічнозв`язний список з поточним елементом.
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.front = None
        self.back = None
        self.curr = None

    def empty(self):
        return self.front is None

    def set_first(self):
        self.curr = self.front

    def set_last(self):
        self.curr = self.back

    def next(self):
        if self.empty() or self.curr.next is None:
            raise StopIteration

        self.curr = self.curr.next

    def prev(self):
        if self.empty() or self.curr.prev is None:
            raise StopIteration

        self.curr = self.curr.prev

    def current(self):
        if self.empty():
            raise RuntimeError

        return self.curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.back = self.curr = node
            return

        node.next = self.curr.next
        node.prev = self.curr
        if self.curr is self.back:
            self.back = node
        else:
            self.curr.next.prev = node
        self.curr.next = node

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.back = self.curr = node
            return

        node.prev = self.curr.prev
        node.next = self.curr
        if self.curr is self.front:
            self.front = node
        else:
            self.curr.prev.next = node
        self.curr.prev = node

    def delete(self):
        if self.empty():
            return

        if self.front is self.back:
            self.front = self.back = self.curr = None
            return

        if self.curr is self.front:
            self.front = self.curr.next
        else:
            self.curr.prev.next = self.curr.next

        if self.curr is self.back:
            self.back = self.curr.prev
        else:
            self.curr.next.prev = self.curr.prev

        if self.curr.next is None:
            self.curr = self.curr.prev
        else:
            self.curr = self.curr.next


lst: DoublyLinkedList


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
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_first()


def set_last():
    """ Робить останній елемент списку, поточним

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

