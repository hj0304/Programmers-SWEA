# y 좌표를 타고 내려가면서 안정성 여부 검사
def check():
    if K == 1:
        return True
    
    for x in range(W):
        cnt = 1
        passed = False
        for y in range(1, D):
            if grid[y-1][x] == grid[y][x]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt == K:
                passed = True
                break
            
        if not passed:
            return False
        
    return True

def solve(row, cnt):
    global ans
    
    # 가지치기
    if cnt >= ans:
        return
    
    if check():
        ans = min(ans, cnt)
        return
    
    # 끝까지 갔을 때 pass가 안된 경우
    if row == D:
        return
    
    # 3가지 분기
    # 1. 그대로 계속 진행 
    # 2. 0으로 색칠
    # 3. 1로 색칠
    
    
    
    # 1. 그대로 진행
    solve(row+1, cnt)
    
    # 2. 0으로 색칠
    origin_row = grid[row][:]
    grid[row] = [0] * W
    solve(row+1, cnt+1)
    
    # 3. 1로 색칠
    grid[row] = [1] * W
    solve(row+1, cnt+1)
    
    grid[row] = origin_row
    

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())     # D는 두께(세로, Y좌표), W는 가로 크기(X좌표), K는 검수 통과 기준
    grid = [list(map(int, input().split())) for _ in range(D)]
    
    ans = float('inf')
    
    solve(0, 0)
    
    print(f"#{tc} {ans}")