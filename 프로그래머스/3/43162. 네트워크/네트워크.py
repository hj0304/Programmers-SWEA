from collections import deque

def solution(n, computers):
    
    parent = list(range(n))
    ans = n
    
    def find(x):
        if parent[x] == x:
            return parent[x]
        
        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        nonlocal  ans
        
        rootA = find(a)
        rootB = find(b)
        
        if rootA != rootB:
            parent[rootB] = rootA
            ans -= 1
        
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)            
    
                
    return ans