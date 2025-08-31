class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None] * size

    def hashing(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hashing(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] == None or self.table[new_index][0] == key:
                self.table[new_index] = (key,value)
                return
        print("Hash table is full")

    def delete(self,key):
        index = self.hashing(key)
        for i in range(self.table):
            new_index = (index + i) % self.size
            if self.table[index] == None:
                return False
            if self.table[index][0] == key:
                self.table[index] = None
                return
        return True
    
    def get(self,key):
        index = self.hashing(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                return None
            if self.table[new_index][0] == key:
                return self.table[new_index][1]
        return None

    
    def display(self):
        for i,bucket in enumerate(self.table):
            print(f'Index {i} : {bucket}')


l = HashTable(10)
l.insert('surender',96)
l.insert('19',19)
l.display()
print(l.get('surender'))
