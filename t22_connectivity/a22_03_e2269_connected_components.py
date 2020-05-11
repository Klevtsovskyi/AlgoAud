''' a22_03_e2269_connected_components.py

https://www.e-olymp.com/uk/problems/2269

Дано неорієнтований незважений граф.
Необхідно підрахувати кількість його компонент зв'язності.

Вхідні дані:
У першому рядку міститься кількість вершин n (n ≤ 100) у графі. Далі
в n рядках задається по n чисел — матриця суміжності графа: в i-ому рядку
на j-ому місці знаходиться 1, якщо вершини i та j з'єднані ребром, та 0,
якщо ребра між ними немає. На головній діагоналі матриці знаходяться нулі.
Матриця симетрична відносно головної діагоналі.

Вихідні дані:
Вивести кількість компонент зв'язності графа.
'''

class Graph:
    ''' Неорієнтовний граф має структуру матриці суміжності.
    '''
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_components_count(self):
        ''' Повертає кількість компонент зв'язності у графі'''
        # Використовуємо пошук в глибину за допомогою стека

        remaining = set(range(len(self.matrix))) # Множина всіх вершин в графі
        stack = [] # Вершини, які залишилося опрацювати
        count = 0  # Кількість компонент зв'язності
        # Цикл не завершиться поки є неопрацьовані вершини
        while remaining:
            if stack: # Якщо стек не пустий, то знаходимося в одній компоненті зв'язності
                current = stack.pop()
            else: # Якщо стек пустий, то перейшли до наступної компоненти зв'язності
                current = remaining.pop()
                count += 1
            # Пробігаємо по всім сусідам поточної вершини
            for neighbour, edge in enumerate(self.matrix[current]):
                if edge:
                    if neighbour in remaining:      # Якщо вершина ще не пройдена,
                        stack.append(neighbour)     # додаємо до стека
                        remaining.remove(neighbour) # і видаляємо з множини, що залишилось опрацювати
        return count


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        graph = Graph(matrix)
        print(graph.get_components_count())
