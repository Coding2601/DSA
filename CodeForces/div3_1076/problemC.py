import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * (n+1)
    A[-1] = max(A[-1], B[-1])
    for i in range(n-2, -1, -1):
        A[i] = max(A[i], max(A[i+1], B[i]))
    for i in range(n):
        C[i+1] = C[i] + A[i]
    for _ in range(q):
        l, r = map(int, input().split())
        print(C[r] - C[l-1], end=" ")
    print()