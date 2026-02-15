import sys
input = sys.stdin.readline
from collections import defaultdict

H, W, N = map(int, input().split())
pieces, vis, ans = [], [False]*N, [None]*N
rem_h, rem_w, curr_x, curr_y = H, W, 1, 1
heights, widths = defaultdict(list), defaultdict(list)

for i in range(N):
    h, w = map(int, input().split())
    pieces.append((h, w))
    heights[h].append(i)
    widths[w].append(i)

for _ in range(N):
    placed = False
    while heights[rem_h]:
        idx = heights[rem_h].pop()
        if not vis[idx]:
            h, w = pieces[idx]
            ans[idx] = (curr_x, curr_y)
            vis[idx] = True
            rem_w -= w
            curr_y += w
            placed = True
            break
    if placed:
        continue
    while widths[rem_w]:
        idx = widths[rem_w].pop()
        if not vis[idx]:
            h, w = pieces[idx]
            ans[idx] = (curr_x, curr_y)
            vis[idx] = True
            rem_h -= h
            curr_x += h
            break
for x, y in ans:
    print(x, y)