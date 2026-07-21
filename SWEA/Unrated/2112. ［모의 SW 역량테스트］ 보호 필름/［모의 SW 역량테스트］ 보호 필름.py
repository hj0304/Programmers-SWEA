def check():
    for x in range(W):
        cnt = 1
        passed = False
        for y in range(1, D):
            if grid[y-1][x] == grid[y][x]:
                cnt += 1
                if cnt == K:
                    passed = True
                    break
            else:
                cnt = 1
                
        if not passed:
            return False
    return True

def dfs(row, cnt, limit):
    global passed
    
    if passed:
        return
    
    if cnt == limit:
        if check():
            passed = True
        return
        
    if row == D:
        return
    
    # 1. 그냥 계속 진행
    dfs(row+1, cnt, limit)
    
    # 2. 0으로 투약
    origin_row = grid[row][:]
    grid[row] = [0] * W
    dfs(row+1, cnt+1, limit)
    
    # 3. 1로 투약
    grid[row] = [1] * W
    dfs(row+1, cnt+1, limit)
    
    grid[row] = origin_row
    



T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())     # D는 두께(y좌표), W는 가로길이 (x좌표), K는 검수 기준
    grid = [list(map(int, input().split())) for _ in range(D)]
    
    if K == 1 or check():
        print(f"#{tc} 0")
        continue
    
    passed = False
    
    for i in range(1, K+1):
        dfs(0, 0, i)
        if passed:
            print(f"#{tc} {i}")
            break
    
        
        
    