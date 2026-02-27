from itertools import permutations

t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    
    suneet = [a1, a2]
    slavic = [b1, b2]
    
    count = 0
    
    for ps in permutations(suneet):
        for pb in permutations(slavic):
            
            suneet_score = 0
            slavic_score = 0
            
            # round 1
            if ps[0] > pb[0]:
                suneet_score += 1
            elif ps[0] < pb[0]:
                slavic_score += 1
            
            # round 2
            if ps[1] > pb[1]:
                suneet_score += 1
            elif ps[1] < pb[1]:
                slavic_score += 1
            
            if suneet_score > slavic_score:
                count += 1
    
    print(count)