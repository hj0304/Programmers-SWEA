def solution(mats, park):
    
    y_len = len(park)
    x_len = len(park[0])
    
    mats.sort(reverse=True)
    
    def check_around(y_len, x_len, met_size):
        
        for y in range(y_len, y_len + met_size):
            for x in range(x_len, x_len + met_size):
                if park[y][x] != '-1':
                    return False
        return True
    
    for m in mats:
        for y in range(y_len - m + 1):
            for x in range(x_len - m + 1):
                if check_around(y, x, m):
                    return m
                
    return -1