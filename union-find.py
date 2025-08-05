n = 5
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_of_x = find(x)
    root_of_y = find(y)
    if root_of_x != root_of_y:
        if rank[root_of_x] < rank[root_of_y]:
            parent[root_of_x] = root_of_y
        elif rank[root_of_x] > rank[root_of_y]:
            parent[root_of_y] = root_of_x
        else:
            parent[root_of_y] = root_of_x
            rank[root_of_x] += 1