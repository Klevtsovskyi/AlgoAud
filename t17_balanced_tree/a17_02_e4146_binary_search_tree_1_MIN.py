''' Теж саме, але займає менше місця (для E-Olymp)'''
class AVLNode:
    def __init__(self,key):self.key=key;self.parent=None;self.left=None;self.right=None;self.balance=0
    def has_left(self):return self.left is not None
    def has_right(self):return self.right is not None
    def has_no_children(self):return not (self.has_left() or self.has_right())
    def is_root(self):return isinstance(self.parent,AVLTree)
    def is_left(self):return self is self.parent.left
    def is_right(self):return self is self.parent.right
    def is_unbalanced(self):return abs(self.balance)>1
    def set_left(self,key):self.left=AVLNode(key);self.left.parent=self;self.left.update_balance()
    def set_right(self,key):self.right=AVLNode(key);self.right.parent=self;self.right.update_balance()
    def update_balance(self):
        if self.is_unbalanced():return self.rebalance()
        if not self.is_root():
            parent = self.parent
            if self.is_left():parent.balance += 1
            elif self.is_right():parent.balance -= 1
            if parent.balance != 0:parent.update_balance()
    def rebalance(self):
        if self.balance < 0:
            if self.right.balance > 0:self.right.rotate_right();self.rotate_left()
            else:self.rotate_left()
        elif self.balance > 0:
            if self.left.balance < 0:self.left.rotate_left();self.rotate_right()
            else:self.rotate_right()
    def rotate_left(self):
        parent = self.parent
        if self.is_root():parent.root = self.__rotate_left()
        elif self.is_left():parent.left = self.__rotate_left()
        elif self.is_right():parent.right = self.__rotate_left()
    def __rotate_left(self):
        pivot = self.right;self.right = pivot.left
        if pivot.has_left():pivot.left.parent = self
        pivot.left = self;parent = self.parent;self.parent = pivot;pivot.parent = parent;self.balance = self.balance + 1 - min(0, pivot.balance);pivot.balance = pivot.balance + 1 + max(0, self.balance);return pivot
    def rotate_right(self):
        parent = self.parent
        if self.is_root():parent.root = self.__rotate_right()
        elif self.is_left():parent.left = self.__rotate_right()
        elif self.is_right():parent.right = self.__rotate_right()
    def __rotate_right(self):
        pivot = self.left;self.left = pivot.right
        if pivot.has_right():pivot.right.parent = self
        pivot.right = self;parent = self.parent;self.parent = pivot;pivot.parent = parent;self.balance = self.balance - 1 - max(0, pivot.balance);pivot.balance = pivot.balance - 1 + min(0, self.balance);return pivot
    def search(self, key):
        node = self
        while True:
            if key == node.key:return node
            elif key < node.key:
                if node.has_left():node = node.left
                else:break
            else:
                if node.has_right():node = node.right
                else:break
    def search_max(self):
        node = self
        while node.has_right():node = node.right
        return node
    def update_balance_on_delete(self, came_from_left):
        if came_from_left:self.balance -= 1
        else:self.balance += 1
        if self.is_unbalanced():
            self.rebalance()
            if not self.is_root():
                if self.parent.balance == 0 and not self.parent.is_root():self.parent.parent.update_balance_on_delete(self.parent.is_left())
        elif self.balance == 0 and not self.is_root():self.parent.update_balance_on_delete(self.is_left())
    def delete(self, node_or_key):
        if isinstance(node_or_key, AVLNode):node = node_or_key
        else:node = self.search(node_or_key)
        if node is None:return
        parent = node.parent
        if node.has_no_children():
            if node.is_root():parent.root = None
            elif node.is_left():parent.left = None;parent.update_balance_on_delete(True)
            elif node.is_right():parent.right = None;parent.update_balance_on_delete(False)
        elif node.has_left() and not node.has_right():
            if node.is_root():parent.root = node.left;node.left.parent = parent
            elif node.is_left():parent.left = node.left;node.left.parent = parent;parent.update_balance_on_delete(True)
            elif node.is_right():parent.right = node.left;node.left.parent = parent;parent.update_balance_on_delete(False)
        elif node.has_right() and not node.has_left():
            if node.is_root():parent.root = node.right;node.right.parent = parent
            elif node.is_left():parent.left = node.right;node.right.parent = parent;parent.update_balance_on_delete(True)
            elif node.is_right():parent.right = node.right;node.right.parent = parent;parent.update_balance_on_delete(False)
        else:left_max = node.left.search_max();node.key = left_max.key;node.left.delete(left_max)
    def exists(self, key):return bool(self.search(key))
    def insert(self, key):
        node = self
        while True:
            if key == node.key:break
            elif key < node.key:
                if node.has_left():node = node.left
                else:node.set_left(key);break
            else:
                if node.has_right():node = node.right
                else:node.set_right(key);break
class AVLTree:
    def __init__(self):self.root = None
    def is_empty(self):return self.root is None
    def insert(self, key):
        if self.is_empty():self.root = AVLNode(key);self.root.parent = self
        else:self.root.insert(key)
    def exists(self, key):
        if self.is_empty():return 'false'
        else:return 'true' if self.root.exists(key) else 'false'
    def search(self, key):
        if not self.is_empty():return self.root.search(key)
    def delete(self, key):
        if not self.is_empty():self.root.delete(key)
    def execute(self, command):name, arg = command.split();arg = int(arg);return getattr(self, name)(arg)
if __name__ == '__main__':
    with open('input.txt') as inp:
        with open('output.txt', 'w') as out:
            tree = AVLTree()
            for line in inp:
                result = tree.execute(line)
                if result:print(result, file=out)
