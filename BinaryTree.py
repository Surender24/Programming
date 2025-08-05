from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root_value):
        self.root = TreeNode(root_value)

    def insert(self,data):
        new_node = TreeNode(data)
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)


    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=' ')
            self.inorder(node.right)


    def preorder(self,node):
        if node:
            print(node.data,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data,end=' ')
        

    def delete(self,data):
        if self.root == None:
            return None
        if self.root.data == data and not self.root.left and not self.root.right:
            self.root = None
            return
        key_node = None
        last_node = None
        parent_of_last = None
        queue = deque([self.root])

        while queue:
            last_node = queue.popleft()
            if last_node.data == data:
                key_node = last_node
            if last_node.left:
                parent_of_last = last_node
                queue.append(last_node.left)
            if last_node.right:
                parent_of_last = last_node
                queue.append(last_node.right)

        if key_node:
            key_node.data = last_node.data
            if parent_of_last.right == last_node:
                parent_of_last.right = None
            else:
                parent_of_last.left = None

    def bfs(self):
        if not self.root:
            return None
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    
    def count_leaf_nodes(self,node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    
    def level_order(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self,data):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.data == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    
    def height(self,node): 
        if not node:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))
    
    def dfs_preorder(self):
        if not self.root:
            return None
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.data,end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        

    def dfs_in_order(self):
        if not self.root:
            return None
        current = self.root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data,end=' ')
                current = current.right

    def dfs_postorder(self):
        if self.root == None:
            return None
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().data,end=' ')

        
        

bt = BinaryTree(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(6)
bt.preorder(bt.root)

