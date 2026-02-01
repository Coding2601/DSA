# interval merging

import sys
input = sys.stdin.readline

N, T = map(int, input().split())
A = list(map(int, input().split())) if N else []

open_time = 0
total = 0

for a in A:
    if a < open_time:
        continue
    total += a - open_time
    open_time = a + 100

if open_time < T:
    total += T - open_time

print(total)