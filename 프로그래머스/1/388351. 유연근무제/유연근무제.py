def solution(schedules, timelogs, startday):
    ans = 0
    
    for i in range(len(schedules)):
        limit = schedules[i] + 10
        hour = limit // 100
        minute = limit % 100
        
        if minute >= 60:
            hour += 1
            minute -= 60
            limit = hour * 100 + minute
        
        now = startday
        
        for log in timelogs[i]:
            if limit < log and now != 6 and now != 7:
                now = startday
                break
            
            now = now + 1 if now < 7 else 1
            
        else:
            now = startday
            ans += 1
        
                
    return ans
        