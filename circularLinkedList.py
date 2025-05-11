class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node

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
        temp.next = new_node

    def delete(self,data):
        temp = self.head
        prev = None
        if self.head.data == data:
            while temp.next != self.head:
                temp = temp.next
            if self.head == self.head.next:
                self.head = None
            else:
                temp.next = self.head.next
                self.head = self.head.next
            return
        
        while temp.next != self.head and temp.data != data:
            prev = temp
            temp = temp.next
        if temp.data == data:
            prev.next = temp.next
        else:
            print("Nokey Found")
            return

        
    def display(self):
        temp = self.head
        if self.head == None:
            print("Empty")
            return
        else:
            while temp:
                print(temp.data,end= ' -> ')
                temp = temp.next
                if temp == self.head:
                    break
            print()


c = CircularLinkedList()
c.insert_at_beg(3)
c.insert_at_beg(4)
c.insert_at_beg(1)
c.insert_at_end('❤')
c.display()
c.delete(8)
c.display()