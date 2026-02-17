import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n > 45:
        print(-1)
    else:
        ans = ""
        for i in range(9, 0, -1):
            if n >= i:
                ans = str(i) + ans
                n -= i
        print(ans)