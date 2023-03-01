"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з розв’язанням колізій методом ланцюжків.
"""

size = 100001
items = []


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def _hash(key: int) -> int:
    return key % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global items
    items = [None for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    curr = _hash(key)
    node = items[curr]
    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = items[curr]
    items[curr] = node


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    curr = _hash(key)
    node = items[curr]
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
    curr = _hash(key)
    node = items[curr]
    if node is not None:
        if node.key == key:
            items[curr] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.key == key:
                prev.next = node.next
                return

            prev = node
            node = node.next


if __name__ == "__main__":
    init()

    set(2, "2")
    set(15, "15")
    set(28, "28")
    print(get(28))
    delete(28)
    print(get(28))
