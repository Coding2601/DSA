import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k == 0:
    if a[0] > 1:
        print(1)
    else:
        print(-1)
else:
    if k == n:
        print(a[-1])
    else:
        if a[k] == a[k-1]:
            print(-1)
        else:
            print(a[k-1])