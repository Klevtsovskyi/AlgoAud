''' a15_01_(2303)_phone_list.py

https://www.e-olymp.com/uk/problems/2303

За заданим списком телефонних номерів визначіть, чи є він сумісним у тому
сенсі, що жоден номер не є префіксом іншого. Нехай, наприклад, телефонний
каталог містить наступні номери:
 - Екстрена служба 911
 - Аліса 97 625 999
 - Боб 91 12 54 26
У цьому випадку не представляється можливим зателефонувати Бобу, тому що
після набору трьох цифр телефону Боба Ви відразу ж потрапите в Екстрену службу.
Наведений список є несумісним.

Вхідні дані:
Перший рядок містить кілбкість тестів t (1 ≤ t ≤ 40). Кожний тест починається
рядком, що містить кілбкість телефонних номерів n (1 ≤ n ≤ 1000000).
Кожний з наступних n рядків містить один телефонний номер.
Телефонний номер містить не більше десяти цифр.

Вихідні дані:
Для кожного тесту вивести "YES", якщо список телефонних номерів є сумісним,
та "NO" інакше.
'''

class Tree:
    ''' Дерево має ієрархічну рекурсивну структуру.
    Кожен вузол співставляється з цифрою в номері, але поле для ключа відсутнє.
    Навантаження у вузла також відсутнє.
    Список дітей кожного вузла - це словник (хеш-таблиця)
    з ключем - цифрою та значенням - піддеревом.
    '''

    def __init__(self): self.children = {}
    def has_children(self): return bool(self.children)
    def add_child(self, digit): self.children[digit] = Tree()
    def has_child(self, digit): return bool(self.children.get(digit))
    def get_child(self, digit): return self.children[digit]
    def clear(self): self.children.clear()

    def add_phone(self, phone: str):
        ''' Якщо номер сумісний з існуючими, додає його до довідника і повертає True, інакше False.'''
        node = self
        i = 0
        while i < len(phone) and node.has_child(phone[i]): # Пробігаємо по ланцюжку існуючих дітей
            node = node.get_child(phone[i])
            i += 1
        if i == len(phone): # Якщо всі цифри номера вже є в довіднику, то даний номер є несумісним
            return False
        if i != 0 and not node.has_children(): # Якщо в існуючому ланцюжку не залишилось дітей, то даний номер несумісний
                return False
        while i < len(phone): # Створюємо ланцюжок
            node.add_child(phone[i])
            node = node.get_child(phone[i])
            i += 1
        return True


if __name__ == '__main__':
    tree = Tree()
    with open('input.txt') as inp:
        with open('output.txt', 'w') as out:
            t = int(inp.readline())
            for _ in range(t):
                n = int(inp.readline())
                consistent = True
                for __ in range(n):
                    phone = inp.readline().rstrip()
                    if consistent: # Якщо знайшли хоча б один несумісний номер, немає смислу перевіряти далі
                        consistent = tree.add_phone(phone)
                print('YES', file=out) if consistent else print('NO', file=out)
                #print('YES') if consistent else print('NO')
                tree.clear()

