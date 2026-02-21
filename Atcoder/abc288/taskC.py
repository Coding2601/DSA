# DSU + counting the number of connected components (tough question)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = list(range(N))
rank = [0] * N

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
for _ in range(M):
    a, b = map(int, input().split())
    union(a-1, b-1)
components = len(set(find(i) for i in range(N)))
print(M - N + components)