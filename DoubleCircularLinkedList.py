class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node

    def insert_at_position(self,index,data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_beg(data)
            return
        temp = self.head
        count = 0
        while temp.next != self.head and count < index - 1:
            temp = temp.next 
            count += 1
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beg(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def delete_at_end(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head.prev = tail.prev
            tail.prev.next = self.head

    def delete_by_position(self,index):
        if self.head is None:
            print("Empty")
            return
        if index == 0:
            self.delete_at_beg()
            return
        temp = self.head
        count = 0
        
        while temp.next != self.head and count < index:
            temp = temp.next
            count += 1
        if count < index:
            print("Out od bounds")
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def delete_by_value(self,data):
        if self.head is None:
            print("List is empty!")
            return
        
        if self.head.data == data:
            self.delete_at_beg()
            return
        
        temp = self.head
        prev = None
        while temp.next != self.head:

            prev = temp
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    
    def display(self):
        if self.head is None:
            print("Empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=' <-> ')
            temp = temp.next
            if temp == self.head:
                break
        print()


d = DoubleCircularLinkedList()
d.insert_at_beg(3)
d.insert_at_beg(4)
d.insert_at_beg(1)
d.insert_at_end('ily')
d.insert_at_end('❤')
d.display()
d.delete_by_value('❤')
d.display()