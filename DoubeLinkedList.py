class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublelinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node.prev = temp.next
        temp.next = new_node

    def insert_at_position(self,index,data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_beg(data)
            return
        temp = self.head
        count = 0 
        while temp.next and count < index - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next.prev = new_node
        new_node.prev = temp
        temp.next = new_node

    def delete(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next
            

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data,end= ' <-> ')
            temp = temp.next
        print("None")


d = DoublelinkedList()
d.insert_at_beg(3)
d.insert_at_beg(4)
d.insert_at_beg(1)
d.insert_at_end('❤')
d.display_forward()
d.insert_at_position(3,'ily')
d.display_forward()
    