def solution(message, spoiler_ranges):
    word_list = []
    
    start = 0
    
    for i in range(len(message)):
        if message[i] == " ":
            word = message[start:i]
            word_list.append((word, start, i-1))
            start = i + 1

        elif i == len(message) - 1:
            word = message[start:i+1]
            word_list.append((word, start, i))
            
    word_unique = set()
    word_normal = set()
    
    # 보통 단어 찾기
    for word, _start, _end in word_list:
        for s, e in spoiler_ranges:
            # 스포일러 방지 범위라면
            if _start <= e and _end >= s:
                break
        else: 
            word_normal.add(word)
            
    print(word_normal)
    
    # 중요 단어 찾기
    for word, _start, _end in word_list:
        for s, e in spoiler_ranges:
            if _start <= e and _end >= s:
                if word not in word_normal:
                    word_unique.add(word)
                    break
                    
    return len(word_unique)