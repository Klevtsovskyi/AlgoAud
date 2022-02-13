"""
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

Вхідні дані #1
4
1 2 5 10
3
1 2 3
Вихідні дані #1
17
1 2
1
5 10
2
1 2
6
1 2
1
1 3
"""


def bridge(left: list):
    """ ...
    :param left: список часів переходу для кожної людини
    :return: мінімальний час (int) і стратегія перетину мосту (list)
    """

    if len(left) == 1:
        return left[0], [(left[0],)]

    min_time = float("inf")       # мінімальний час переходу
    min_strategy = None           # список-стратегія перетину мосту

    def _move(from_, to_, strategy, time, *indexes):
        """ Перекидає елементи з номерами nums з одного берега на інший.

        :param from_: список елементів на одному березі
        :param to_: список елементів на іншому березі
        :param strategy: поточна стратегія
        :param time: загальний час проходження
        :param indexes: індекси в спадаючому порядку
        :return: from_, to_, strategy, time
        """
        strategy.append(tuple(sorted(from_[i] for i in indexes)))
        time += strategy[-1][-1]
        for i in indexes:
            to_.append(from_.pop(i))
        return from_, to_, strategy, time

    def _bridge(left, right, strategy, time):
        """ Допоміжна функція.

        :param left: список елементів на лівому березі
        :param right: список елементів на правому березі
        :param strategy: поточна стратегія
        :param time: поточний час
        """
        nonlocal min_time, min_strategy

        for i in range(1, len(left)):
            for j in range(i):
                # Перекидаємо два елементи на правий берег
                s_left, s_right, s_strategy, s_time = _move(left[:], right[:], strategy[:], time, i, j)
                if s_left:
                    for k in range(len(s_right)):
                        # Повертаємо один елемент на лівий берег
                        ss_right, ss_left, ss_moves, ss_time = _move(s_right[:], s_left[:], s_strategy[:], s_time, k)
                        _bridge(ss_left, ss_right, ss_moves, ss_time)
                # Якщо на лівому березі не залишилося елементів,
                # то перевіряємо чи є поточна стратегія кращою
                elif s_time < min_time:
                    min_time = s_time
                    min_strategy = s_strategy

    _bridge(left, [], [], 0)
    return min_time, min_strategy


if __name__ == "__main__":
    with open("input.txt") as inp:
        while True:
            n = inp.readline().rstrip()
            if n == "":
                break
            left_shore = list(map(int, inp.readline().split()))
            best_time, best_strategy = bridge(left_shore)
            print(best_time)
            for move in best_strategy:
                print(*move)
