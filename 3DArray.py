class Array3D:
    def __init__(self,depth,rows,columns,defualt_values=0):
        self.depth = depth
        self.rows = rows
        self.columns = columns
        self.data = [[[defualt_values for _ in range(columns)] for _ in range(rows)] for _ in range(depth)]

    def insert(self,d,r,c,data):
        if 0 <= d < self.depth and 0 <= r < self.rows and 0 <= c < self.columns:
            self.data[d][r][c] = data
        else:
            print("Error")

    def delete(self,d,r,c):
        if 0 <= d < self.depth and 0 <= r < self.rows and 0 <= c < self.columns:
            self.data[d][r][c] = 0
        else:
            print("Error")

    def get(self,d,r,c):
        if 0 <= d < self.depth and 0 <= r < self.rows and 0 <= c < self.columns:
            return self.data[d][r][c]
        else:
            print("Error")
            return None

    def display(self):
        for d in range(self.depth):
            print(f"Depth {d}:")
            for r in range(self.rows):
                print(self.data[d][r])
            print()

a = Array3D(2,3,4)
a.insert(0,0,0,1)
a.insert(0,1,1,2)
a.insert(1,2,3,3)
a.insert(1,0,0,4)
a.insert(1,1,2,5)
a.insert(1,2,1,6)
a.insert(0,2,3,7)
a.display()
    