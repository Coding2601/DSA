import sys
input = sys.stdin.readline

S = input().rstrip()
print("Yes" if S[0] == S[-1] else "No")