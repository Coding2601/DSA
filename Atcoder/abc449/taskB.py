H, W, Q = map(int, input().split())

rows = H
cols = W

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        R = query[1]
        print(R * cols)
        rows -= R
    else:
        C = query[1]
        print(C * rows)
        cols -= C