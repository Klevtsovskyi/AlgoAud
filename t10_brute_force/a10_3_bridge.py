''' a10_3_bridge.py

https://www.e-olymp.com/uk/problems/1592

n людей вночі бажають перейти на інший берег річки по мосту.
У них є один ліхтар. Рухатися по мосту з ліхтарем можуть не
більше двох осіб. Рух по мосту без ліхтаря заборонено.
Для кожної людини відомий час, за який він перетинає міст.
Якщо по мосту рухаються двоє, то час їх пересування дорівнює
часу більш повільного.

Необхідно вивести мінімальний час, за який усі n людей перейдуть
на інший берег річки, а також послідовність переходів,
як зазначено у прикладі.

Вхідні дані:
Складається з декількох тестів. Перший рядок кожного тесту
містить кількість людей n (n ≤ 1000), а другий рядок містить
n чисел - час переходу людей через міст. Час переходу кожної
людини через міст не більше 10000 секунд.

Вихідні дані:
Для кожного тесту вивести наступну інформацію. Перший рядок
містить мінімальний час в секундах, за який можуть перетнути
міст n людей. Далі йде стратегія перетину мосту людьми. Кожний
рядок стратегії містить одне або два числа, що характеризують
швидкості людей, які з ліхтарем перетинають міст. При існуванні
декількох оптимальних стратегій перетину річки вивести будь-яку.
'''

from math import inf

def bridge(left_shore):
    ''' ...
    :param left_shore: список часів переходу для кожної людини
    :return: мінімальний час (int) і стратегія перетину мосту (list)
    '''

    if len(left_shore) == 1:
        return left_shore[0], [(left_shore[0],)]

    min_time = inf # мінімальний час переходу
    min_moves = None # список-стратегія перетину мосту

    def move(from_, to_, moves, time, *nums):
        ''' Перекидає елементи з номерами nums з одного берега на інший.
        :from_: список елементів на одному березі
        :to_: список елементів на іншому березі
        :moves: поточна стратегія
        :time: загальний час проходження
        :nums: індекси в спадаючому порядку
        :return: from_, to_, moves, time
        '''
        moves.append(tuple(sorted([from_[n] for n in nums])))
        time += max(moves[-1])
        [to_.append(from_.pop(n)) for n in nums]
        return from_, to_, moves, time

    def _bridge(left, right, moves, time):
        ''' Допоміжна функція.
        :left: список елементів на лівому березі
        :right: список елементів на правому березі
        :moves: поточна стратегія
        :time: поточний час
        '''
        nonlocal min_time, min_moves

        for i in range(1, len(left)):
            for j in range(i):
                # Перекидаємо два елементи на правий берег
                sleft, sright, smoves, stime = move(left[:], right[:], moves[:], time, i, j)
                if sleft:
                    for k in range(len(sright)):
                        # Повертаємо один елемент на лівий берег
                        ssright, ssleft, ssmoves, sstime = move(sright[:], sleft[:], smoves[:], stime, k)
                        _bridge(ssleft, ssright, ssmoves, sstime)
                # Якщо на лівому березі не залишилося елементів, то перевіряємо
                elif stime < min_time: # чи є поточна стратегія кращою
                    min_time = stime
                    min_moves = smoves

    _bridge(list(left_shore), [], [], 0)
    return min_time, min_moves


if __name__ == '__main__':
    data = [(1, 2, 5, 10),
            (1, 2, 3),
            (1, 3, 6, 7, 13),
            (1, 3, 6, 7, 11, 13),
            (1,),
           ]
    for t in data:
        print(bridge(t))
    '''
    with open('input.txt') as f:
        data = list(map(int, f.read().split()))
        result = []
        i = 0
        while i < len(data):
            n = data[i]
            i += 1
            time, moves = bridge(sorted(data[i:i+n]))
            result.append((time, moves))
            i += n
            
    with open('output.txt', 'w') as f:
        for time, moves in result:
            print(time, file=f)
            [print(*move, file=f) for move in moves]
    '''
