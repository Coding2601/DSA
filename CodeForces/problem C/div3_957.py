import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    result = []    
    for i in range(n, k-1, -1):
        result.append(i)        
    for i in range(m + 1, k):
        result.append(i)
    for i in range(1, m + 1):
        result.append(i)
    print(*result)