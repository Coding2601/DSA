import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
reachable = [False] * (N+1)
q = deque([1])
reachable[1] = True
while q:
    u = q.popleft()
    for v in adj[u]:
        if not reachable[v]:
            reachable[v] = True
            q.append(v)
total_reachable = sum(reachable)
visited = [False] * (N+1)
q = deque()
count = 0
ans = []

for k in range(1, N+1):
    if k == 1:
        visited[k] = True
        q.append(k)
        count = 1
    else:
        for u in range(1, k):
            if visited[u]:
                for v in adj[u]:
                    if v == k:
                        visited[k] = True
                        q.append(k)
                        count += 1
                        break
                if visited[k]:
                    break
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v <= k and not visited[v]:
                visited[v] = True
                q.append(v)
                count += 1
    if count != k:
        print(-1)
    else:
        ans.append(total_reachable - count)
for a in ans:
    print(a)