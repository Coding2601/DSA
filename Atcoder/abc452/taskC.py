N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b-1)
M = int(input())
S = [input().strip() for _ in range(M)]
valid = set()
for s in S:
    length = len(s)
    for i, ch in enumerate(s):
        valid.add((length, i, ch))
for s in S:
    if len(s) != N:
        print("No")
        continue
    ok = True
    for i in range(N):
        if (A[i], B[i], s[i]) not in valid:
            ok = False
            break
    print("Yes" if ok else "No")