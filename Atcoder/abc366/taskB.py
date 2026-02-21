# constructive problem

import sys
input = sys.stdin.readline
N = int(input())
S = [input().strip() for _ in range(N)]
S.reverse()
M = max(len(s) for s in S)
for j in range(M):
    curr_str = []
    for s in S:
        if j < len(s):
            curr_str.append(s[j])
        else:
            curr_str.append("*")
    while curr_str and curr_str[-1] == "*":
        curr_str.pop()
    print("".join(curr_str))