class AVLnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVlTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else -1

    def balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotation(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotation(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, node, data):
        if not node:
            return AVLnode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.balance_factor(node)
        # LL Case
        if balance > 1 and data < node.left.data:
            return self.right_rotation(node)
        # RR Case
        if balance < -1 and data > node.right.data:
            return self.left_rotation(node)
        # LR Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        # RL Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node

    def min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def deletion(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self.deletion(node.left, data)
        elif data > node.data:
            node.right = self.deletion(node.right, data)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self.min_value(node.right)
            node.data = temp.data
            node.right = self.deletion(node.right, temp.data)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.balance_factor(node)

        # LL
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotation(node)
        # RR
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotation(node)
        # LR
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        # RL
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node

    def search(self, node, data):
        if not node or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

avl = AVlTree()
for i in [10, 20, 30]:
    avl.root = avl.insert(avl.root, i)

avl.inorder(avl.root)
print()
avl.root = avl.deletion(avl.root, 20)
avl.inorder(avl.root)


