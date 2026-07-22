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


def dfs(y_index, cnt, limit):
    global passed
    
    # 검수 기준 통과 시 종료
    if passed:
        return
    
    # 정해놓은 한도에 색칠 횟수가 도달 했을 때 check하고 합격 시 종료
    if cnt == limit:
        if check():
            passed = True
        return
        
    # 검수에 합격하지 못한 채로 y 인덱스의 끝까지 도달했을 때 종료(실패)
    if y_index == D:
        return
    
    # 3가지 분기
    
    # 1. 그냥 다음 진행
    dfs(y_index+1, cnt, limit)
    
    # 2. 0으로 색칠
    origin_row = grid[y_index][:]
    grid[y_index] = [0] * W
    dfs(y_index+1, cnt+1, limit)
    
    # 3. 1로 색칠
    grid[y_index] = [1] * W
    dfs(y_index+1, cnt+1, limit)
    
    # 원상복구
    grid[y_index] = origin_row

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())     # D는 두께 (y좌표), W는 가로 크기(x좌표), K는 검수 기준
    grid = [list(map(int, input().split())) for _ in range(D)]
    
    if K == 1 or check():
        print(f"#{tc} {0}")
        continue
    
    passed = False
    
    for i in range(1, K+1):
        dfs(0, 0, i)
        if passed:
            print(f"#{tc} {i}")
            break
        
    