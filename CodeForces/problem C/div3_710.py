# longest common substring

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    max_sub_len, n, m = 0, len(a), len(b)
    for i in range(n):
        for j in range(i, n):
            sub_str = a[i:j+1]
            if sub_str in b:
                max_sub_len = max(max_sub_len, j-i+1)
    print(n + m - 2 * max_sub_len)