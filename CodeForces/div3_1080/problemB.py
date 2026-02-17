import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    can_sort = True
    for i in range(n):
        curr_val, curr_pos = a[i], i+1
        while curr_val % 2 == 0:
            curr_val //= 2
        while curr_pos % 2 == 0:
            curr_pos //= 2
        if curr_val != curr_pos:
            can_sort = False
            break
    if can_sort:
        print("YES")
    else:
        print("NO")