import sys
import bisect
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    string = input().strip()
    ans = 0
    if c == 'g':
        print(0)
        continue
    greens = []
    for i in range(n):
        if string[i] == 'g':
            greens.append(i)
    greens = greens + [x + n for x in greens]
    for i in range(n):
        if string[i] == c:
            next_green = bisect.bisect_left(greens, i)
            ans = max(ans, greens[next_green] - i)
    print(ans)