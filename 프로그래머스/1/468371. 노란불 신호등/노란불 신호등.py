def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a*b) // gcd(a, b)

def solution(signals):
    cycles = []
    
    for sig in signals:
        cycles.append(sum(sig))
    
    max_times = cycles[0]
    for i in range(len(cycles)):
        max_times = lcm(max_times, cycles[i])
        
    
    for t in range(1, max_times+1):
        all_yellows = True
        
        for G, Y, R in signals:
            cycle = G + Y + R
            
            pos = (t-1) % cycle + 1
            
            if not G < pos <= G + Y:
                all_yellows = False
                break
        
        if all_yellows:
            return t
    
    return -1
            
        
    
            
    