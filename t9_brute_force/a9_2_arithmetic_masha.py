''' a9_2_arithmetic_masha.py

https://www.e-olymp.com/uk/problems/1296

Мишко записує 2 числа: n і m, а Маша повинна розділити число n на m
частин, не змінюючи порядок цифр, при цьому Мишко ще й вимагає, щоб
добуток отриманих m чисел був максимальним. допоможіть Маші.

Вхідні дані:
Вхідні дані містять декілька тестових випадків. Кожен тестовий
випадок розміщено у окремому рядку і містить 2 числа, відокремлених
пропуском: спочатку n (1 ≤ n ≤ 1015), а потім m (1 ≤ m ≤ [lg(n)]).

Вихідні дані:
Для кожного тестового прикладу у окремому рядку виведіть
шуканий максимальний добуток.
'''

def am(n: int, m: int):
    ''' 
    :param n: натуральне число 
    :param m: кількість частин, на яке розбивається число n
    :return: максимальний добуток
    '''

    max_value = 0

    def _am(sub_num: str, mult: int, m: int):
        ''' 
        :param sub_num: підрядок цифр
        :param mult: добуток
        :param m: кількість шматків, на які залишилося розділити sub_num
        '''
        nonlocal max_value

        value = mult * int(sub_num)
        if value < max_value:
            return
        elif m == 1:
            max_value = value
            return
             
        for i in range(1, len(sub_num) - m + 2):
            _am(sub_num[i:], mult * int(sub_num[:i]), m - 1)
            
    _am(str(n), 1, m)
    return max_value
    
if __name__ == '__main__':
    data = [(12345, 2),
            (12345, 3),
            (987654321, 4),
            (111, 3),]
    for n, m in data:
        print(am(n, m))
    '''
    result = []
    with open('input.txt') as f:
        for line in f:
            n, m = [int(s) for s in line.split()]
            result.append(am(n, m))

    with open('output.txt', 'w') as f:
        print(*result, sep='\n', file=f)
    '''
