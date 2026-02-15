import  sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s, x = map(int, input().split())
    array = list(map(int, input().split()))
    if s >= sum(array) and (s - sum(array)) % x == 0:
        print("YES")
    else:
        print("NO")