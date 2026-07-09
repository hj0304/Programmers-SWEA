from collections import deque

def solution(bandage, health, attacks):
    total_time = bandage[0]
    heal_per_sec = bandage[1]
    extra_bonus_heal = bandage[2]

    sec = 0
    attacks = deque(attacks)

    attack_time, damage = attacks.popleft()
    
    seq = 0
    
    max_hp = health
    
    while True: 
        sec += 1
        # 공격당할 시간이라면
        if sec == attack_time:
            seq = 0
            health -= damage
            
            if health <= 0:
                return -1
            
            if not attacks:
                return health
            
            attack_time, damage = attacks.popleft()
            
            
        # 공격 없는 시간이라면
        else:
            health += heal_per_sec
            seq += 1
            
            # 보너스 조건 달성 시
            if seq == total_time:
                health += extra_bonus_heal
                seq = 0
            # 풀피 넘어설 경우 이월 막기
            if health >= max_hp:
                health = max_hp
                