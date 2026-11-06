def solution(a, b):
    
    length = len(a)
    
    ans = 0
    
    for i in range(length):
        ans += (a[i] * b[i])
        
    return ans