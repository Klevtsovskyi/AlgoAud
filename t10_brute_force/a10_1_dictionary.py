''' a10_1_dictionary.py

https://www.e-olymp.com/uk/problems/364

У тарабарській мові N символів - перші N латинських букв.
Тарабарські слова містять всі літери, причому кожна буква
зустрічається в слові один раз. Головний тарабарський філолог
склав словник, у якому всі можливі слова містяться в
алфавітному порядку. Допоможіть йому знайти слово за його номером.

Вхідні дані:
Задано кількість букв N (2 <= N <= 12) і номер слова k (1 <= k <= N!).

Вихідні дані:
Вивести тарабарське слово.
'''

def tab(n, k):
    m = 0
    chars = [chr(97 + i) for i in range(0, n)] # ord('a') = 97

    def _tab(word):
        nonlocal m
        if len(word) == n:
            m += 1
            return word

        for char in chars:
            if char not in word:
                word_next = word[:]
                word_next.append(char)
                result = _tab(word_next)
                if k == m:
                    return result
            
    return _tab([])

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(*tab(n, k), sep='')
