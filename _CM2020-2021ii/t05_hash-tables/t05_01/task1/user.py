"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""


M = 500009
K = 1


keys = []
values = []


def hash(key):
    return key % M


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global keys, values
    keys = [None for _ in range(M)]
    values = [None for _ in range(M)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    curr = hash(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            values[curr] = value
            return
        curr = (curr + K) % M

    keys[curr] = key
    values[curr] = value


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    curr = hash(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            return values[curr]
        curr = (curr + K) % M


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    curr = hash(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            next = (curr + K) % M
            while keys[next] is not None and next != hash(keys[next]):
                keys[curr] = keys[next]
                values[curr] = values[next]
                curr = next
                next = (next + K) % M

            keys[curr] = None
            values[curr] = None
        curr = (curr + K) % M
