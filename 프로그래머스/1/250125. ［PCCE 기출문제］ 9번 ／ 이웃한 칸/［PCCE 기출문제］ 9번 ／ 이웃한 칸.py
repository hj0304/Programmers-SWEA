#    우 하 좌 상
dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]

def solution(board, h, w):
    answer = 0
    ans_color = board[h][w]
    leng = len(board)
    
    for i in range(4):
        sy, sx = h, w
        ny, nx = sy + dy[i], sx + dx[i]
        
        if 0 <= ny < leng and 0 <= nx < leng:
            if board[ny][nx] == ans_color:
                answer += 1
    
    return answer