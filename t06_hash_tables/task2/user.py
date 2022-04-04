"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з розв’язанням колізій методом ланцюжків.
"""


SIZE = 100003

table = []


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def _hash(key: int):
    return key % SIZE


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table = [None for _ in range(SIZE)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    i = _hash(key)
    node = table[i]
    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = table[i]
    table[i] = node


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    i = _hash(key)
    node = table[i]
    while node is not None:
        if node.key == key:
            return node.value
        node = node.next
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    i = _hash(key)
    node = table[i]
    if node is not None:
        if node.key == key:
            table[i] = node.next
        else:
            prev = node
            node = node.next
            while node is not None:
                if node.key == key:
                    prev.next = node.next
                prev = node
                node = node.next
