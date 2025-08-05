def countingsort(arr):
    if not arr:
        return arr
    
    max_value = max(arr)
    count = [0] * (max_value+1)
    for i in arr:
        count[i] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

print(countingsort([4,2,9,6,5,1,3]))