from collections import deque
T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = deque()
    for day in range(1, N+1):
        q.append([day, A[day-1]])
        need = B[day-1]
        while need > 0:
            if q[0][1] <= need:
                need -= q[0][1]
                q.popleft()
            else:
                q[0][1] -= need
                need = 0
        while q and q[0][0] <= day - D:
            q.popleft()
    ans = sum(x[1] for x in q)
    print(ans)