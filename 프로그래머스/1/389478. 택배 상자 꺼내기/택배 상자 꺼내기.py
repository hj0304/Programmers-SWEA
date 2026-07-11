# 우 하 좌 하 우
dx = [1, 0, -1, 0, 1]
dy = [0, 1, 0, 1, 0]


def solution(n, w, num):
    y_len = n // w + 1 if n % w != 0 else n // w
    x_len = w
    
    grid = [[0] * x_len for _ in range(y_len)]
    
    curr = 1
    
    for y in range(y_len):
        # 0층부터 시작, 짝수층
        if y % 2 != 0:
            for x in range(x_len):
                if curr > n:
                    break
                grid[y][x] = curr
                curr += 1
                
        # 홀수 층
        else:
            for x in range(x_len-1, -1, -1):
                if curr > n:
                    break
                grid[y][x] = curr
                curr += 1
    
    target_y, target_x = -1, -1
    
    for y in range(y_len):
        for x in range(x_len):
            if grid[y][x] == num:
                target_y, target_x = y, x
                break
                
    ans = 0
    for y in range(target_y, y_len):
        if grid[y][target_x] != 0:
            ans += 1
        
    
    return ans