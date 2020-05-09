''' a21_03_e4004_is_there_a_cycle.py

https://www.e-olymp.com/uk/problems/4004

Задано орієентовний граф. Визначити, чи містить він цикл.

Вхідні дані:
Перший рядок містить кількість вершин n (n ≤ 50). Далі у n рядках йде
по n чисел, кожне з яких дорывнює "0" або "1". j-те число в i-му рядку
дорівнює "1" тоді і лише тоді, коли існує ребро, яке йде з i-ї вершини
у j-ту. Гарантується, що на діагоналі матриці будуть стояти нулі.

Вихідні дані:
Виведіть "0", якщо у заданому графі циклу немає, і "1", якщо він є.
'''

class Graph:
    ''' Орієнтовний граф зображено у вигляді матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def has_cycle(self):
        ''' Повертає True, якщо в графі є цикли, False інакше.'''
        # Використовуємо пошук в глибину

        # В remaining зберігатимемо вершини, які залишилось опрацювати
        # (на початку всі вершини в графі є неопрацьованими)
        remaining = set(range(len(self.matrix)))
        # В path зберігатимемо вершини, що були пройдені на поточному шляху
        path = set()
        # Оскільки в даній реалізації не використовується рекурсія,
        # знадобиться словник джерел (ключ - вершина, значення - з якої прийшли)
        # та стек (для додавання сусідів поточного вузла і опрацювання їх у майбутньому)
        sources = {}
        stack = []
        # Поки є неопрацьовані вершини
        while remaining:
            if stack:                     # Якщо стек не є пустим,
                current = stack.pop()     # беремо з нього наступну вершину
                remaining.remove(current) # та видаляємо її з множини неопрацьованих.
            else:                         # Якщо стек є пустим,
                current = remaining.pop() # беремо довільну вершину з множини неопрацьованих,
                path.clear()              # очищуємо шлях
                sources.clear()           # і словник джерел.
                sources[current] = None   # Встановлюємо джерело None для поточної вершини
            # Додаємо поточну вершину до поточного шляху
            path.add(current)
            # Змінна deadlock використовується для перевірки чи є у поточної вершини ребра,
            # по яким вона з'єднується з сусідами, або чи є сусіди опрацьованими
            # (якщо сусіди вже були опрацьовані, далі цикл відсутній)
            deadlock = True
            for neighbour, edge in enumerate(self.matrix[current]):
                # Якщо існує ребро між вершинами current та neighbour
                if edge == 1:
                    if neighbour in path:  # Якщо сусіда neighbour вершини current вже було пройдено
                        return True        # на поточному шляху, означає, що знайдено цикл
                    elif (neighbour in remaining and # Якщо сусіда ще неопрацьовано
                          neighbour not in sources): # та його ще немає в словнику джерел (та, відповідно, в стеці),
                        stack.append(neighbour)      # додаємо його до стеку
                        sources[neighbour] = current # та словника джерел
                        deadlock = False
            # Якщо потрапили в тупик, але в стеці ще є елементи, потрібно повернутися до вершини,
            # в якій відбулося розгалуження
            if deadlock and stack:
                while current != sources[stack[-1]]: # Поки не дійшли то вершини розгалуження,
                    path.remove(current)             # видаляємо вершину зі шляху
                    current = sources.pop(current)   # йдемо по словнику джерел
        # Повертає False, якщо закінчилися неопрацьовані вершини
        return False


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(1 if graph.has_cycle() else 0)
