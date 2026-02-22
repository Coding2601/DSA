# combinatorics + dp (tough question)
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    v_x, v_z = 0, 0
    for x in range(n):
        flag = True
        for y in range(n):
            if a[y] >= b[(y + x) % n]:
                flag = False
                break
        if flag:
            v_x += 1
    for z in range(n):
        flag = True
        for u in range(n):
            if b[u] >= c[(u + z) % n]:
                flag = False
                break
        if flag:
            v_z += 1
    print(n * v_x * v_z)