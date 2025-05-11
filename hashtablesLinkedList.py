class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,key,value):
        temp = self.head 
        while temp:
            if temp.key == key:
                temp.value = value
                return
            temp = temp.next
        new_node = Node(key,value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(f'({temp.key},{temp.value})',end=' -> ')
            temp = temp.next
        print('None')


class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self,key):
        return sum(ord(i) for i in key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        self.table[index].insert(key,value)

    def display(self):
        for i ,linked_list in enumerate(self.table):
            print(f'Index {i} :',end=' ')
            linked_list.display()


h = HashTable(10)
h.insert('surender',96)
h.display()
