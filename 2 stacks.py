class Twostacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push1(self,data):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.array[self.top1] = data
        else:
            print("Stack overflow")
            return
    
    def push2(self,data):
        if self.top1 + 1 < self.top2:
            self.top2 -= 1
            self.array[self.top2] = data
        else:
            print("Stack overflow")
            return
        
    def pop1(self):
        if self.top1 >= 0:
            popped = self.array[self.top1]
            self.top1 -= 1
            return popped
        else:
            print("satck is empty")
            return 
        
    def pop2(self):
        if self.top2 < self.capacity:
            popped = self.array[self.top2]
            self.top2 += 1
            return popped
        else:
            print("Stack is empty")
            return

    def display(self):
        print(f"Stack 1 : {self.array[:self.top1+1]}")
        print(f'Stack 2 : {self.array[self.top2:]}')
        

s = Twostacks(6)
s.push1(1)
s.push1(2)
s.push2(1)
s.push2(2)
s.push2(3)
s.push2(4)
s.display()

