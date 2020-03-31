''' a13_5_(971)_josephus_problem.py

Існує легенда, що Іосиф Флавій - відомий історик першого століття - вижив
і став відомим завдяки математичній обдарованості. У ході іудейської війны
він у складі загону з 41 іудейського воїна був загнаний римлянами у печеру.
Віддаючи перевагу самовбивство полону, воїни вирішили вишукуватись у коло і
послідовно вбивати кожного третього з живих до тих пір, доки не залишиться
жодної людини. Проте Іосиф розом з одним зі своїх еднодумців вважав подібний
кінець безглуздим - він швидко вирахував спасительні місця у порочному колі,
на які поставив себе і свого товариша. І лише тому ми знаємо його історію.

У нашому варіанті ми почнемо з того, що вшукуємо у коло N чоловік,
пронумерованих числами від 1 до N, і будемо виключати кожного k-ого до тих
пір, доки не вціліє лише одна людина. (Наприклад, якщо N=10, k=3, то
спочатку помре 3-й, потім 6-й, потім 9-й, потім 2-й, потім 7-й, потім 1-й,
потім 8-й, за ним - 5-й, і потім 10-й. Таким чином, вціліє 4-й.)

Вхідні дані:
У вхідному файлі задано натуральні числа N і k. 1 ≤ N ≤ 500, 1 ≤ k ≤ 100.

Вихідні дані:
Вихідний файл повинен містити єдине число - номер людини,
що залижиласьв живих.
'''

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._len = 0

    def push(self, item):
        node = Node(item)
        if self._back:
            self._back.next = node
        else:
            self._front = node
        self._back = node
        self._len += 1
        return 'ok'
    
    def pop(self):
        if self._front:
            node = self._front
            self._front = node.next
            if not self._front:
                self._back = None
            self._len -= 1
            return node.item
        return 'error'
    
    def front(self):
        return self._front.item if self._front else 'error'
    
    def size(self):
        return self._len
    
    def clear(self):
        self.__init__()
        return 'ok'


def josephus(n, k):
    
    queue = Queue()
    for i in range(1, n + 1):
        queue.push(i)

    while queue.size() != 1:
        for j in range(1, k):
            queue.push(queue.pop())
        queue.pop()
    
    return queue.front()


if __name__ == '__main__':
    print(josephus(*map(int, input().split())))
