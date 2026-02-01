# greedy + prefix

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    H, ans = [0]*N, 0
    H[0] = R[0]

    for i in range(1, N):
        H[i] = min(R[i], H[i-1] + 1)
    for i in range(N-2, -1, -1):
        H[i] = min(H[i], H[i+1] + 1)
    for i in range(N):
        ans += R[i] - H[i]

    print(ans)