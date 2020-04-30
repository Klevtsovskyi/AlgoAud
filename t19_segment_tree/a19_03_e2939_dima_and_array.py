''' a19_03_e2939_dima_and_array.py

https://www.e-olymp.com/uk/problems/2939

Мама подарувала хлопчику Дімі масив довжиною n. Масив цей не простий,
а особливий. Діма може вибрати три числа i, j та d (1 ≤ i ≤ j ≤ n,
-1000 ≤ d ≤ 1000), і усі елементи з індексами від i до j магічно стають
рівним d. Діма бавиться зі своїм масивом, а мама час від часу задає йому
питання - яка сума усіх чисел у масиві з індексами від f до t? Діма легко
справився з цими запитаннями, а чи зможете Ви?

Вхідні дані:
У першому рядку знаходиться два цілих числа n та q (1 ≤ n ≤ 5 * 10^5,
1 ≤ q ≤ 10^5) - кількість елементів у масиві і сумарна кількість операцій та
запитів відповідно. У наступному рядку задано n чисел a1, a2, ..., an
(-1000 ≤ ai ≤ 1000) - початковий стан масиву. У наступних q рядках задані
операції та запити. Перший символ у рядку може бути = або ?. Якщо рядок
починається з =, то це операція присвоювання. Далі йдуть i, j та d,
обмеження на які задано вище. Якщо рядок починається з ?, то це запит.
Далі йдуть числа f і t (1 ≤ f, t ≤ n).

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

    def update(self, left, right, item):
        ''' Міняє елементи на позиції від left до right (включно) на елемент item.'''
        left += self.size
        right += self.size
        for i in range(left, right + 1):
            self.items[i] = item # Змінюємо елементи від left до right на item
        while left != 1:       # Поки не дійшли до кореня
            left = left // 2   # Беремо індекс батька зліва
            right = right // 2 # та справа
            # На краях елементи завжди різні, тому рахуємо їх окремо
            self.items[left] = self.items[left * 2] + self.items[left * 2 + 1]
            self.items[right] = self.items[right * 2] + self.items[right * 2 + 1]
            # Всередині елементи завжди однакові, тому рахуємо тільки один з них
            item = self.items[left * 2 + 2] + self.items[left * 2 + 3]
            for i in range(left + 1, right):
                self.items[i] = item

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
                tree.update(int(command[1]) - 1, int(command[2]) - 1, int(command[3]))
            elif command[0] == '?':
                print(tree.sum(int(command[1]) - 1, int(command[2]) - 1))
