''' a19_01_e2941_dima_and_array.py

https://www.e-olymp.com/uk/problems/2941

Мама подарувала хлопчику Дімі масив довжиною n. Масив цей не простий,
а особливий. Діма може вибрати два числа i та d (1 ≤ i ≤ n, -1000 ≤ d ≤ 1000),
і елемент з індексом i магічно стає рівним d. Діма бавиться зі своїм масивом,
а мама час від часу задає йому питання — яка сума усіх чисел у масиві з
індексами від f до t? Діма легко справився з цими запитаннями, а чи зможете Ви?

Вхідні дані:
У першому рядку знаходиться два цілих числа n та q (1 ≤ n ≤ 5 * 10^5,
1 ≤ q ≤ 10^5) - кількість елементів у масиві і сумарна кількість операцій та
запитів відповідно. У наступному рядку задано n чисел a1, a2, ..., an
(-1000 ≤ ai ≤ 1000) - початковий стан масиву. У наступних q рядках задані
операції та запити. Перший символ у рядку може бути = або ?. Якщо рядок
починається з =, то це операція присвоювання. Далі йдуть i та d, обмеження на
які описано в умові. Якщо рядок починається з ?, то це запит. Далі йдуть
числа f і t (1 ≤ f, t ≤ n).

Вихідні дані:
Для кожного запиту виведіть суму чисел у масиві з індексами від f до t,
по одному результату у рядку.
'''

from math import log2, ceil

class SegmentTree:
    ''' Дерево відрізків з операцією суми.'''

    def __init__(self, array):
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = n * [0] + array + (n - k) * [0]
        for i in range(n - 1, 0, -1):
            # Визначаємо навантаження предків
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        self.size = n

    def update(self, i, item):
        ''' Міняє елемент масиву на позиції i (початок з нуля) на item.'''
        i += self.size
        self.items[i] = item
        while i != 1:  # Поки не дійшли до кореня
            i = i // 2 # Беремо номер батька
            # Визначаємо його навантаження
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

    def sum(self, left, right):
        ''' Повертає суму елементів відрізка.'''
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1: # Якщо правий син
                result += self.items[left]
            if right % 2 == 0: # Якщо лівий син
                result += self.items[right]
            left = (left + 1) // 2   # Беремо індекс батька вузла справа
            right = (right - 1) // 2 # Беремо індекс батька вузла зліва
        return result


if __name__ == '__main__':
    with open('input.txt') as inp:
        n, q = map(int, inp.readline().split())
        array = list(map(int, inp.readline().split()))
        tree = SegmentTree(array)
        for _ in range(q):
            command = inp.readline().split()
            if command[0] == '=':
                tree.update(int(command[1]) - 1, int(command[2]))
            elif command[0] == '?':
                print(tree.sum(int(command[1]) - 1, int(command[2]) - 1))
