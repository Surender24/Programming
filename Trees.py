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
        def min_value_node(node):
            while node.left:
                node = node.left
            return node
        
        def _delete(node,data):
            if not node:
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
                successor = min_value_node(node.right)
                node.data = successor.data
                node.right = _delete(node.right,successor.data)
            return node
        self.root = _delete(self.root,data)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data,end=' ')
                _inorder(node.right)
        _inorder(self.root)
        print()
            