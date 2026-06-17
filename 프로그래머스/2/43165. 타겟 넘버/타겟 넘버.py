def solution(numbers, target):
    answer = 0
    def backtrack(index, now_value):
        nonlocal answer
        if index == len(numbers):
            if now_value == target:
                answer += 1
            return
        
        now_value += numbers[index]
        backtrack(index+1, now_value)
        now_value -= numbers[index]

        now_value -= numbers[index]
        backtrack(index+1, now_value)
        now_value += numbers[index]
            
            
    
    backtrack(0, 0)
    
    
    
    return answer