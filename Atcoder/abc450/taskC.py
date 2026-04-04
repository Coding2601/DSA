from collections import deque

H, W = map(int, input().split(" "))
grid = [list(input().strip()) for _ in range(H)]
vis = [[False]*W for _ in range(H)]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    vis[si][sj] = True
    flag = False
    
    while q:
        i, j = q.popleft()
        if i == 0 or i == H-1 or j == 0 or j == W-1:
            flag = True
        for di, dj in dirs:
            ni, nj = di + i, dj + j
            if 0 <= ni < H and 0 <= nj < W:
                if not vis[ni][nj] and grid[ni][nj] == '.':
                    vis[ni][nj] = True
                    q.append((ni, nj))

    return flag

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.' and not vis[i][j]:
            if not bfs(i, j):
                ans += 1
print(ans)