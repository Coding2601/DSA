import sys
input = sys.stdin.readline
N, T, A = map(int, input().split())
R = N - (T + A)
if T > (A + R) or A > (T + R):
    print("Yes")
else:
    print("No")