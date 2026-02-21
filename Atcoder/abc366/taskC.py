# hashing

import sys
input = sys.stdin.readline
Q = int(input())
obj, count = {}, 0
for _ in range(Q):
    query = input().strip().split()
    if query[0] == '1':
        x = int(query[1])
        if obj.get(x, 0) == 0:
            count += 1
        obj[x] = obj.get(x, 0) + 1
    elif query[0] == '2':
        x = int(query[1])
        obj[x] -= 1
        if obj[x] == 0:
            count -= 1
    else:
        print(count)