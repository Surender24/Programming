class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self,index,data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_beg(data)
            return
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
        return
    
    def get_index(self,index):
        if self.head is None:
            print("Empty")
            return
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            temp = temp.next
            count += 1
        return 'Out of Bounds'
    
    def update_at_index(self,index,data):
        if self.head is None:
            print("Empty")
            return
        temp = self.head
        count = 0
        while temp:
            if count == index:
                temp.data = data
                return
            temp = temp.next
            count += 1
        return 'Out Of Bounds'
    
    
    def search(self,data):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    
    def delete(self,data):
        if self.head is None:
            print("Empty list")
            return
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            return
        prev = None
        while temp.next and temp.data != data:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        return
    
    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def display(self):
        temp = self.head 
        while temp:
            print(temp.data,end=' -> ')
            temp = temp.next
        print("None")


s = SingleLinkedList()
while True:
    print("\n1. Insertion at Beginning\n2. Insertion at End\n3. Insertion at Position\n4. Get Index\n5. Update at Index\n"
    "6. Search\n7. Delete\n8. Display\n9. Exit")
    user_choice = int(input("Enter ypur Operation: "))
    if user_choice == 1:
        data = input("Enter Data: ")
        s.insert_at_beg(data)
    elif user_choice == 2:
        data = input("Enter Data: ")
        s.insert_at_end(data)
    elif user_choice == 3:
        data = input("Enter Data: ")
        index = int(input("Enter Index: "))
        s.insert_at_position(index,data)
    elif user_choice == 4:
        index = int(input("Enter index: "))
        print(s.get_index(index))
    elif user_choice == 5:
        data = input("Enter Data: ")
        index = int(input("Enter Index: "))
        s.update_at_index(index,data)
    elif user_choice == 6:
        data = input("Enter Data: ")
        s.search(data)
    elif user_choice == 7:
        data = input("Enter Data: ")
        s.delete(data)
    elif user_choice == 8:
        s.display()
    elif user_choice == 9:
        break
    else:
        print("Invalid Operation")
    
    

    