"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""

size: int = 11
count: int
keys: list[int]
values: list[str]

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def rehash():
    global size
    size = size * 2 + 1
    while not is_prime(size):
        size += 2
    _keys = keys
    _values = values
    init()
    for i in range(len(_keys)):
        if _keys[i] not in (EMPTY, DELETED):
            set(_keys[i], _values[i])


def hash(key: int) -> int:
    return key % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global keys, values, count
    count = 0
    keys = [EMPTY for _ in range(size)]
    values = [EMPTY for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global count

    if count > 0.7 * size:
        rehash()

    i = hash(key)
    j = -1
    while keys[i] is not EMPTY:
        if keys[i] == key:
            values[i] = value
            return
        if j == -1 and keys[i] == DELETED:
            j = i
        i = (i + 1) % size

    if j == -1:
        j = i
        count += 1

    keys[j] = key
    values[j] = value


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    i = hash(key)
    while keys[i] is not EMPTY:
        if keys[i] == key:
            return values[i]
        i = (i + 1) % size
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    i = hash(key)
    while keys[i] is not EMPTY:
        if keys[i] == key:
            keys[i] = DELETED
            values[i] = DELETED
            return None
        i = (i + 1) % size
    return None


if __name__ == '__main__':
    init()
    set(2, "2")
    set(49, "49")
    set(5, "5")
    set(17, "17")
    set(16, "16")

    print(keys)

    delete(5)
    delete(17)

    print(keys)

    set(60, "60")
    set(9, "9")

    print(keys)

    set(1, "1")
    set(12, "12")
    set(23, "23")

    print(keys)
