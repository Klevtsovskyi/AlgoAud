''' a9_3_assignment_problem.py

https://www.e-olymp.com/uk/problems/1781

Однією з класичних задач комбінаторної оптимізації є так звана
"задача про призначення". Формулюється вона наступним чином.

Є n працівників, пронумерованих числами від 1 до n, і n робіт,
також пронумерованих числами від 1 до n. Якщо i-й працівник
виконує j-ту роботу, то йому виплачується заробітна плата у
розмірі cij грошових одиниць. Необхідно знайти таке призначення
працівників на роботи (кожен працівник виконує рівно одну роботу,
кожна робота виконується рівно одним працівником), щоб сумарна
зарплата працівників мінімальна (відповідна сума називається
вартістю призначення).

Напишіть програму, яка розвязує задачу про призначення.

Вхідні дані:
Перший рядок містить ціле число n (1 ≤ n ≤ 10).

Наступні n рядків містять по n чисел кожен. При цьому
j-те число (i + 1)-го рядка дорівнює cij (1 ≤ cij ≤ 1000).

Вихідні дані:
Виведіть мінімальну можливу вартість призначення.
'''

from sys import maxsize

def assignment(rows):

    min_salary = maxsize

    def _assignment(sal, rs):
        nonlocal min_salary

        if sal > min_salary:
            return
        elif not rs:
            min_salary = sal
            return

        for i in range(len(rs)):
            sub_rs = tuple([r[:i] + r[i+1:] for r in rs[1:]])
            _assignment(sal + rs[0][i], sub_rs)

    _assignment(0, tuple(rows))
    return min_salary

if __name__ == '__main__':
    data = [((1, 2),
             (2, 1)
            ),
            ((1, 2),
             (3, 4)
            ),
           ]
    for t in data:
        print(assignment(t))
    '''
    rows = [tuple(map(int, input().split())) for i in range(int(input()))]
    print(assignment(rows))
    '''
