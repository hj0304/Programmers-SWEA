from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    cnt = defaultdict(int)
    
    for p in participant:
        cnt[p] += 1
    
    for c in completion:
        cnt[c] -= 1
    
    for name, c in cnt.items():
        if c == 1:
            answer = name
            break
    
    
    return answer