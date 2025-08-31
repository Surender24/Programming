class HashTable:
    def  __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self,key):
        return sum(ord(i) for i in key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key,value])

    def delete(self,key):
        index = self.hash_function(key)
        for i,pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
            return False
        
    def display(self):
        for i,bucket in enumerate(self.table):
            print(f'Index {i} : {bucket}')


h = HashTable(10)
h.insert('surender',96)
h.insert("ekalavya",99)
h.insert("pratap",19)
h.display()
