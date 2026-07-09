def solution(name, yearning, photo):
    dct = {}
    
    for i in range(len(name)):
        dct[name[i]] = yearning[i]
    
    ans = []
    for p in photo:
        score = 0
        for n in p:
            if n in name:
                score += dct[n]
        ans.append(score)
    
    return ans 