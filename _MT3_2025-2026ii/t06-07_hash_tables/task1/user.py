"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class HashTable:

    def __init__(self, size=11):
        self._keys = [EMPTY for _ in range(size)]
        self._values = [EMPTY for _ in range(size)]
        self._size = size
        self._count = 0

    def hash(self, key: int):
        return key % self._size

    def rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values

        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.set(_keys[i], _values[i])

    def set(self, key: int, value: str):
        if self._count > 0.7 * self._size:
            self.rehash()

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

    def get(self, key: int):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size
        return None

    def delete(self, key: int):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._keys[i] = DELETED
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


if __name__ == '__main__':
    init()
    set(22, "22")
    set(1, "1")
    set(66, "66")
    set(10, "10")
    set(21, "21")
    print(hash_table._keys)
    delete(66)
    print(hash_table._keys)
    print(get(21))
    set(13, "13")
    set(41, "41")
    set(53, "53")
    set(96, "96")
    set(11, "11")
    print(hash_table._keys)



