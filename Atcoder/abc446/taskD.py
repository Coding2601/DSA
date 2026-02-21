import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp, ans = {}, 0
for a in A:
    dp[a] = dp.get(a-1, 0) + 1
    ans = max(ans, dp[a])
print(ans)