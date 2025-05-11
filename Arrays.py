class Array:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def insert(self,data,index):
        if self.size == self.capacity:
            print("Array is Full")
            return
        if index < 0 or index > self.capacity:
            print("Invalid index")
            return
        for i in range(self.size,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = data
        self.size += 1

    def delete(self,index):
        if index < 0 or index > self.capacity:
            print("Invalid index")
            return
        for i in range(index,self.size-1):
            self.data[i] = self.data[i+1]
        self.data[self.size - 1] = None
        self.size -= 1

    def search(self,data):
        for i in range(self.size):
            if self.data[i] == data: return i
        return -1
    
    def update(self,index,data):
        if index < 0 or index > self.capacity:
            print("Invalid index")
            return
        self.data[index] = data


    def display(self):
        for i in range(self.size):
            print(self.data[i],end=' ')
        print()


a = Array(5)
a.insert(1,0)
a.insert(2,1)
a.insert(3,2)
a.insert(4,3)
a.display()
a.update(2,24)
a.display()
