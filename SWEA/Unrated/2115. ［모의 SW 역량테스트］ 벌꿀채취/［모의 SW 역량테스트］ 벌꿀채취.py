def get_max(arr):
    max_profit = 0
    
    def dfs(idx, cur_sum, cur_profit):
        nonlocal max_profit
        
        # 1. 꿀의 합이 C를 넘어가면 가지치기
        if cur_sum > C:
            return
        
        # 2. M개의 벌통을 모두 확인 완료한 경우 최댓값 업데이트
        if idx == M:
            max_profit = max(max_profit, cur_profit)
            return
        
        # 3-1. [선택지 1] 현재 벌통을 채취 함.
        dfs(idx + 1, cur_sum + arr[idx], cur_profit + arr[idx]**2)
        
        
        # 3-2. [선택지 2] 현재 벌통을 채취 안함
        dfs(idx + 1, cur_sum, cur_profit)
    
    # 0번 인덱스부터, 현재 합 0, 현재 수익 0으로 시작하기
    dfs(0, 0, 0)
    return max_profit
    

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # N은 벌통 크기(N*N), M은 선택할 벌통 개수, C는 채취 가능한 꿀 최대치
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 모든 위치의 최대 수익을 미리 계산
    profit = [[0] * (N - M + 1) for _ in range(N)]
    for y in range(N):
        for x in range(N - M + 1):
            bultong = grid[y][x : x + M]
            profit[y][x] = get_max(bultong)
            
    # 2. 두 일꾼의 위치가 겹치지 않게 골라 합산 최댓값 찾기
    ans = 0
    for y1 in range(N):
        for x1 in range(N - M + 1):
            p1 = profit[y1][x1]
            
            for y2 in range(y1, N):
                sx2 = x1 + M if y1 == y2 else 0
                
                for x2 in range(sx2, N - M + 1):
                    p2 = profit[y2][x2]
                    
                    ans = max(ans, p1 + p2)
    
    
    
    print(f"#{tc} {ans}") 
    