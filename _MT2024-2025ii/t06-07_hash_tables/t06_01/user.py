"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""


EMPTY = "EMTPY"
DELETED = "DELETED"


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class HashTable:

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | int] = [EMPTY for _ in range(size)]
        self._values: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def hash(self, key):
        return key % self._size

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values
        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.set(_keys[i], _values[i])

    def set(self, key, value):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        j = -1
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return

            if j == -1 and self._keys[i] == DELETED:
                j = i

            i = (i + 1) % self._size

        if j == -1:
            j = i
            self._count += 1

        self._keys[j] = key
        self._values[j] = value

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size

    def delete(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._keys[i] = DELETED
                self._values[i] = DELETED
                return
            i = (i + 1) % self._size


hash_table: HashTable


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global hash_table
    hash_table = HashTable()


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


if __name__ == "__main__":
    init()
    set(15, "15")
    set(4, "4")
    set(27, "27")
    set(37, "37")
    delete(27)
    print(hash_table._keys)
    set(16, "16")
    print(hash_table._keys)

