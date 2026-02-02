# 2D DP + reachability

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    C -= 1
    MAZE = [input().strip() for _ in range(N)]
    
    low = [-1] * N
    for i in range(N):
        row = MAZE[i]
        for j, ch in enumerate(row):
            if ch == '#':
                low[j] = i
    dp = [bytearray(N) for _ in range(N)]
    for i in range(N):
        dp[i][C] = 1
    
    for i in range(N-2, -1, -1):
        next_row, curr_row, row_str = dp[i+1], dp[i], MAZE[i]
        for j in range(N):
            if curr_row[j]:
                continue
            is_reachable = (next_row[j] or (j > 0 and next_row[j-1]) or j+1 < N and next_row[j+1])
            if not is_reachable:
                continue
            if row_str[j] == '.':
                curr_row[j] = 1
            else:
                if low[j] == i:
                    for k in range(i+1):
                        dp[k][j] = 1
    ans = ''.join('1' if dp[0][j] else '0' for j in range(N))
    print(ans)