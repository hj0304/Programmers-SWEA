from collections import deque

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def solution(maps):
    len_y = len(maps)
    len_x = len(maps[0])
    
    visited = [[-1] * len_x for _ in range(len_y)]
    
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    while queue:
        sy, sx = queue.popleft()
        
        for i in range(4):
            ny, nx = sy + dy[i], sx + dx[i]
            if 0 <= ny < len_y and 0 <= nx < len_x and visited[ny][nx] == -1 and maps[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[sy][sx] + 1

    return visited[len_y-1][len_x-1]