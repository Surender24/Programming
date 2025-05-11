class Node:
    def __init__(self,data : int):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self,data : int) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self) -> int:
        if self.top is None:
            print("Stack is empty")
            return
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped
    
    def isempty(self) -> bool:
        return self.top == None
    
    def size(self) -> int:
        return self.count 
    
    def peek(self) -> int:
        return self.top.data
    
    def __str__(self):
        elements = []
        temp = self.top
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return ' '.join(elements) if elements else "Stack is Empty"
    
    def reversed(self):
        prev = None
        temp = self.top
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.top = prev

    
    
s = Stack()

s.push("hello")
s.push(2)
s.push(3)
s.push(4)
print(s)
