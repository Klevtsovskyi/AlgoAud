"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з розв’язанням колізій методом ланцюжків.
"""

class Node:

    def __init__(self, key: int, value: str):
        self.key: int = key
        self.value: str = value
        self.next: [None | Node] = None


size: int = 1000003
slots: list[None | Node]


def hash(key: int):
    return key % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    i = hash(key)
    node = slots[i]
    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = slots[i]
    slots[i] = node


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    i = hash(key)
    node = slots[i]
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
    i = hash(key)
    node = slots[i]
    if node is None:
        return
    if node.key == key:
        slots[i] = node.next
        return

    prev = node
    node = node.next
    while node is not None:
        if node.key == key:
            prev.next = node.next
            return
        prev = node
        node = node.next

