''' a23_01_area_of_the_room.py

https://www.e-olymp.com/uk/problems/4001

Обчислити площу кімнати у квадратному лабіринті.

Вхідні дані:
У першому рядку знаходиться число n - розмір лабіринту (3 ≤ n ≤ 10). У наступних
n рядках, кожен з яких містить по n символів, задано лабіринт (символ "."
позначає порожню клітинку, а "*" - стінку). Останній рядок містить два числа -
номер рядка та стовбця клітинки, яка знаходиться у кімнаті, площу якої
необхідно обчислити. Гарантується, що ця клітинка порожня і що лабіринт оточено
стінками з усіх сторін. Рядки та стовбці лабіринту нумеруються з одиниці.

Вихідні дані:
Вивести кількість порожніх клітинок у даній кімнаті.
'''


class Labyrinth:
    ''' Клас для моделювання лабіринту'''

    # Можливі напрямки руху
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self, matrix, wall, cell):
        '''
        :param matrix: матриця лабіринту
        :param wall: об'єкт (рядок), який позначає стінку лабіринту
        :param cell: об'єкт (рядок), який позначає пусту клітинку лабіринту
        '''
        self.matrix = matrix
        self.wall = wall
        self.cell = cell

    def get_area(self, i, j):
        ''' Повертає кількість пустих клітинок,
        до яких можна дістатися з клітинки (i, j) включно
        '''
        # Матриця не відвіданих клітинок
        visited = [[0 for __ in range(len(matrix))]
                   for _ in range(len(matrix))]
        visited[i][j] = 1
        count = 0 # Кількість клітинок, до яких можемо дістатися

        queue = [(i, j)] # Черга, згідно пошуку в ширину
        while queue:
            i, j = queue.pop(0)
            count += 1 # Якщо дістаємо клітинку з черги, до неї можна дістатися

            for di, dj in Labyrinth.directions:
                ii, jj = i + di, j + dj # Сусідні клітинки
                if (self.matrix[ii][jj] == self.cell and # Якщо до сусідньої клітинки можливий рух
                    not visited[ii][jj]):                # і вона ще не була пройдена,
                    queue.append((ii, jj))               # додаємо до черги її номери
                    visited[ii][jj] = 1                  # та відмічаємо, що вона відвідана
        return count


if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(inp.readline()))
        i, j = map(int, inp.readline().split())
        print(Labyrinth(matrix, '*', '.').get_area(i - 1, j - 1))
