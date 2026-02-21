import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        total = n*n
        ans = []
        for i in range(1, total+1, 2):
            ans.append(i)
        for i in range(2, total+1, 2):
            ans.append(i)
        for i in range(n):
            print(*ans[i*n:(i+1)*n])
