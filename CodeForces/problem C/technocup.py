import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = True
    for i in range(n):
        if (b[i] - a[i]) not in (0, 1):
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")