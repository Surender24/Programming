class Doublehashing:
    def __init__(self,size):
        self.size = size
        self.table = [None] * size

    def h1(self,key):
        return sum(ord(i) for i in key) % self.size
    
    def h2(self,key):
        return self.size - (sum(ord(i) for i in key) % self.size)
    
    def insert(self,key,value):
        index1 = self.h1(key)
        index2 = self.h2(key)
        for i in range(self.size):
            new_index = (index1 + i*index2) % self.size
            if self.table[new_index] is None or self.table[new_index][0] == key:
                self.table[new_index] = (key, value)
                return
        print("Hash table is full")

    def display(self):
        for i,bucket in enumerate(self.table):
            print(f'Index {i} : {bucket}')

d = Doublehashing(10)
d.insert("Alice", 85)
d.insert("Bob", 92)
d.insert("Charlie", 78)
d.insert("David", 67)
d.display()