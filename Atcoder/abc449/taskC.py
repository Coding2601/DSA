import sys
import bisect

input = sys.stdin.readline

N, L, R = map(int, input().split())
S = input().strip()
ans = 0
prefix = [[0]*(N+1) for _ in range(26)]
for i in range(N):
    for c in range(26):
        prefix[c][i+1] = prefix[c][i]
    prefix[ord(S[i]) - 97][i+1] += 1
for i in range(N):
    left, right = i+L, min(N-1, i+R)
    if left > right:
        continue
    c = ord(S[i]) - 97
    ans += prefix[c][right+1] - prefix[c][left]
print(ans)