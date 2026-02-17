import sys
input = sys.stdin.readline

t = int(input())
INF = 10**9

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [INF] * 7
    for v in range(1, 7):
        dp[v] = 0 if a[0] == v else 1
    for i in range(1, n):
        ndp = [INF] * 7
        for v in range(1, 7):
            cost = 0 if a[i] == v else 1
            for u in range(1, 7):
                if v != u and v != 7-u:
                    ndp[v] = min(ndp[v], dp[u] + cost)
        dp = ndp
    print(min(dp[1:7]))