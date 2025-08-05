from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        def _insert(node,data):
            if not node:
                return TreeNode(data)
            if data < node.data:
                node.left = _insert(node.left,data)
            else:
                node.right = _insert(node.right,data)
            return node
        self.root = _insert(self.root,data)

    def delete(self,data):
        def min_value(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        def _delete(node,data):
            if node is None:
                return None
            if data < node.data:
                node.left = _delete(node.left,data)
            elif data > node.data:
                node.right = _delete(node.right,data)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                temp = min_value(node.right)
                node.data = temp.data
                node.right = _delete(node.right,temp.data)
            return node
        self.root = _delete(self.root,data)

    def search(self,data):
        def _search(node,data):
            if not node or node.data == data:
                return node
            if data < node.data:
                return _search(node.left,data)
            else:
                return _search(node.right,data)

        return _search(self.root,data)
    
    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            print(node.data, end='')
            _inorder(node.right)
        _inorder(self.root)
        print()

    def preorder(self):
        def _preorder(node):
            print(node.data,end='')
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        print()

    def postorder(self):
        def _postorder(node):
            _postorder(node.left)
            _postorder(node.right)
            print(node.data,end='')
        _postorder(self.root)
        print()


    def height(self):
        def _height(root):
            if not root:
                return -1 
            return 1 + max(_height(root.left),_height(root.right))
        return _height(self.root)


    def level_order(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
    def is_balanced(self):
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left,right)
        return check(self.root) != -1
    
    
    def find_min(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.data
    
    def bst_to_sorted_array(self):
        result = []
        def _inorder(node):
            _inorder(node.left)
            result.append(node.data)
            _inorder(node.right)
        _inorder(self.root)
        return result
    
    def lowest_common_ancestor(self, node, p, q):
        if not node:
            return None
        if p.data < node.data and q.data < node.data:
            return self.lowest_common_ancestor(node.left, p, q)
        if p.data > node.data and q.data > node.data:
            return self.lowest_common_ancestor(node.right, p, q)
        return node
    
    def inorder_successor(self, root, p):
        successor = None
        while root:
            if p.data < root.data:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
    
    def inorder_predecessor(self, root, p):
        predecessor = None
        while root:
            if p.data > root.data:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor
    
    def is_valid_bst(self):
        def validation(node,min_value,max_value):
            if not node:
                return True
            if not (min_value < node.data < max_value):
                return False
            return (validation(node.left,min_value,node.data) and validation(node.right,node.data,max_value))
        return validation(self.root,float('-inf'),float('inf'))

bst = BinarySearchTree()
for i in [5,3,7,10]:
    bst.insert(i)

print(bst.level_order())
p = bst.search(3)
q = bst.search(7)
print(bst.lowest_common_ancestor(bst.root, p, q).data)