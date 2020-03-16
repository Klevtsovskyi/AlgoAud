''' a9_1_23from5.py

https://www.e-olymp.com/uk/problems/1540

Чи можна так розставити 5 заданих чисел та знаки арифметичних
операцій (+, -,*), щоб вийшов вираз, значення якого дорівнює 23?
Вважати, що усі три зазначені операції мають однаковий пріоритет і
виконуються послідовно зліва направо.

Вхідні дані:
Кожний рядок містить п'ять натуральних чисел від 1 до 50.
Останній рядок містить п'ять нулів та не обробляється.

Вихідні дані:
Для кожного тесту вивести в окремому рядку слово "Possible",
якщо можна так розставити числа та знаки зазначених арифметичних
операцій, щоб вийшов вираз зі значенням 23. Якщо цього зробити
не можливо, то вивести "Impossible".
'''

OPS = ('__add__', '__sub__', '__mul__')

def twenty_three(nums):

    def _tt(val: int, ns: tuple):
        if not ns:
            return val == 23
        
        for i in range(len(ns)):
            for op in OPS:
                if _tt(getattr(val, op)(ns[i]), ns[:i] + ns[i+1:]) is True:
                    return True

    tt = any([_tt(nums[i], nums[:i] + nums[i+1:]) for i in range(len(nums))])
    return 'Possible' if tt else 'Impossible'

if __name__ == '__main__':
    data = [(1, 1, 1, 1, 1),
            (1, 2, 3, 4, 5),
            (2, 3, 5, 7, 11),
            (5, 5, 5, 5, 3),
            (2, 2, 2, 2, 7),
            (2, 2, 5, 7, 10),
            (2, 24, 40, 17, 1),
           ]
    for t in data:
        print(t, twenty_three(t))
    '''
    result = []
    while True:
        data = tuple(map(int, input().split()))
        if any(data):
            result.append(twenty_three(data))
        else:
            print(*result, sep='\n')
            break
    '''
