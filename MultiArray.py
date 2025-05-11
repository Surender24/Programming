class MultiArray:
    def __init__(self,rows,columns,default_value=0):
        self.rows = rows
        self.columns = columns
        self.data = [[default_value for _ in range(columns)] for _ in range(rows)]

    def insert(self,row,col,data):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = data
        else:
            print("invlaid index")

    def delete(self,row,col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = 0
        else:
            print("invlaid index")