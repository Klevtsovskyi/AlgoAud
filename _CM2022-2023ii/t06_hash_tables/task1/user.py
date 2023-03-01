"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""
import math

size = 11
count = 0
keys = []
values = []


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def rehash():
    global size
    _size = size
    _keys = keys
    _values = values

    size = 2 * size + 1
    while not is_prime(size):
        size += 2

    init()
    for i in range(_size):
        if _keys[i] is not None:
            set(_keys[i], _values[i])


def _hash(key: int) -> int:
    return key % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, keys, values
    count = 0
    keys = [None for _ in range(size)]
    values = [None for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global count

    if count / size > 0.7:
        rehash()

    curr = _hash(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            values[curr] = value
            return
        curr = (curr + 1) % size

    keys[curr] = key
    values[curr] = value
    count += 1


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    curr = _hash(key)
    while keys[curr] is not None:
        if keys[curr] == key:
            return values[curr]
        curr = (curr + 1) % size
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    global count

    curr = _hash(key)
    items = []
    while keys[curr] is not None:
        if keys[curr] != key:
            items.append((keys[curr], values[curr]))
        else:
            count -= 1

        keys[curr] = None
        values[curr] = None
        curr = (curr + 1) % size

    for k, v in items:
        set(k, v)


if __name__ == "__main__":
    init()
    for i in range(20):
        set(i, f"i")
