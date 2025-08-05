def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j] , arr[j-1] = arr[j-1] , arr[j]
            else:
                break
    return arr

print(insertionsort([4,2,9,6,5,1,3]))