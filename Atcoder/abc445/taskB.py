import sys
input = sys.stdin.readline

N = int(input())
strs = [input().rstrip() for _ in range(N)]

m = max((len(string)) for string in strs)

for string in strs:
    k = (m - len(string)) // 2
    print("."*k + string + "."*k)