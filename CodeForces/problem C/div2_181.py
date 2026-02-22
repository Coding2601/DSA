# math + includion-exclusion principle + combinatorics (tough question)

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    def count_good(x):
        if x <= 0:
            return 0
        A = x//2 + x//3 + x//5 + x//7
        A -= x//6 + x//10 + x//14 + x//15 + x//21 + x//35
        A += x//30 + x//42 + x//70 + x//105
        A -= x//210
        return x - A
    l, r = map(int, input().split())
    print(count_good(r) - count_good(l - 1))