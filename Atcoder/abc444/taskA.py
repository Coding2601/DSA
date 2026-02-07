import sys
input = sys.stdin.readline

N = int(input())
A = N // 100
B = (N // 10) % 10
C = N % 10

if A == B == C:
    print("Yes")
else:
    print("No")