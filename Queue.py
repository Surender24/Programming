class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        self.length += 1

    def dequeue(self):
        if self.isempty():
            return 'Queue is empty'
        data = self.front.data
        self.front = self.front.next
        self.rear.next = self.front
        if self.front is None:
            self.rear = None
        self.length -= 1
        return data
    
    def peek(self):
        return self.front.data
    
    def isempty(self):
        return self.front == None
    
    def size(self):
        return self.length
    
    def display(self):
        if self.front is None:
            print("Empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
            if temp == self.front:
                break
        print()
    
class stack:
    def __init__(self):
        self.queue = Queue()

    def push(self,data):
        self.queue.enqueue(data)
        for _ in range(self.queue.size()-1):
            temp = self.queue.dequeue()
            self.queue.enqueue(temp)

    def pop(self):
        if self.queue.isempty():
            return "Stack is Empty"
        return self.queue.dequeue()

    def peek(self):
        return self.queue.peek()
    
    def is_empty(self):
        return self.queue.isempty()
    
    def size(self):
        return self.queue.size()
    
    def display(self):
        self.queue.display()


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()