# 3D prefix sum (tough to understand, but not hard to implement)

import sys
input = sys.stdin.readline

N = int(input())
A = [[[0]*(N+1) for _ in range(N+1)] for __ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, N+1):
        row = list(map(int, input().split()))
        for z in range(1, N+1):
            A[x][y][z] = row[z-1]

P = [[[0]*(N+1) for _ in range(N+1)] for __ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, N+1):
        for z in range(1, N+1):
            P[x][y][z] = (
                A[x][y][z]
                + P[x-1][y][z]
                + P[x][y-1][z]
                + P[x][y][z-1]
                - P[x-1][y-1][z]
                - P[x-1][y][z-1]
                - P[x][y-1][z-1]
                + P[x-1][y-1][z-1]
            )

Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())    
    ans = (
        P[Rx][Ry][Rz]
        - P[Lx-1][Ry][Rz]
        - P[Rx][Ly-1][Rz]
        - P[Rx][Ry][Lz-1]
        + P[Lx-1][Ly-1][Rz]
        + P[Lx-1][Ry][Lz-1]
        + P[Rx][Ly-1][Lz-1]
        - P[Lx-1][Ly-1][Lz-1]
    )
    print(ans)