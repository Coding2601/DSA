N = int(input())

C = [[0]*N for _ in range(N)]

for i in range(N-1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        C[i][i+j+1] = row[j]

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if C[a][b] + C[b][c] < C[a][c]:
                print("Yes")
                exit()
                
print("No")