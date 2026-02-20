import sys
input = sys.stdin.readline

N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
ans = [0] * N
for i in range(N-1, -1, -1):
    if A[i] == i:
        ans[i] = i
    else:
        ans[i] = ans[A[i]]
print(*(x +1 for x in ans))