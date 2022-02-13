"""
https://www.e-olymp.com/uk/problems/364

У тарабарській мові N символів - перші N латинських букв.
Тарабарські слова містять всі літери, причому кожна буква
зустрічається в слові один раз. Головний тарабарський філолог
склав словник, у якому всі можливі слова містяться в
алфавітному порядку. Допоможіть йому знайти слово за його номером.

Вхідні дані:
Задано кількість букв N (2 <= N <= 12)
і номер слова k (1 <= k <= N!).

Вихідні дані:
Вивести тарабарське слово.

Вхідні дані #1
4 5
Вихідні дані #1
adbc
"""


def tab(n: int, k: int) -> str:
    m = 0
    chars = [chr(ord("a") + i) for i in range(n)]

    def _tab(word: str) -> str:
        nonlocal m
        if len(word) == n:
            m += 1
            return word

        for char in chars:
            if char not in word:
                sub_word = word + char
                result = _tab(sub_word)
                if k == m:
                    return result

    return _tab("")


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(tab(n, k))
