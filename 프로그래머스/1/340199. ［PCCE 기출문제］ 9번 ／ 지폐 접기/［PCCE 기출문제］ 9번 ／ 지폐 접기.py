def solution(wallet, bill):
    answer = 0
    
    while True:
        wallet.sort()
        bill.sort()
        
        # wallet보다 bill이 작으면 break
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
        
        # wallet보다 bill이 크면 bill의 큰 면을 반으로 접기
        else:
            bill[1] = bill[1] // 2
            answer += 1

        
        
    return answer