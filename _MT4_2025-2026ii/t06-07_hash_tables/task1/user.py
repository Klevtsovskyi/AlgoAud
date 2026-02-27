"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class HashTable:

    def __init__(self, size=11):
        self.size: int = size
        self.keys: list = [EMPTY for _ in range(size)]
        self.values: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    def hash(self, key: int):
        return key % self.size

    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        _keys = self.keys
        _values = self.values
        self.__init__(self.size)

        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.set(_keys[i], _values[i])

    def set(self, key: int, value: str) -> None:
        if self.count > 0.7 * self.size:
            self.rehash()

        i = self.hash(key)
        j = -1
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                self.values[i] = value
                return

            if j == -1 and self.keys[i] is DELETED:
                j = i

            i = (i + 1) % self.size

        if j == -1:
            j = i
            self.count += 1

        self.keys[j] = key
        self.values[j] = value

    def get(self, key: int) -> str | None:
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.size
        return None

    def delete(self, key: int) -> None:
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                self.keys[i] = DELETED
                self.values[i] = DELETED
                return
            i = (i + 1) % self.size


hash_table = HashTable()


def init():
    """ Викликається 1 раз на початку виконання програми. """
    pass


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    hash_table.set(key, value)


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    return hash_table.get(key)


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    hash_table.delete(key)


if __name__ == '__main__':
    hash_table.set(55, "55")
    hash_table.set(20, "20")
    hash_table.set(9, "9")
    hash_table.set(31, "31")

    print(hash_table.keys)

    hash_table.delete(55)
    hash_table.delete(31)

    print(hash_table.keys)

    hash_table.set(10, "10")
    hash_table.set(64, "64")
    hash_table.set(73, "73")
    hash_table.set(80, "80")
    hash_table.set(1, "1")
    hash_table.set(13, "13")
    hash_table.set(3, "3")

    print(hash_table.keys)
