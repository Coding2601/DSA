N, M = map(int, input().split())
taken = set()
for _ in range(N):
    L_N = int(input())
    wishlist = list(map(int, input().split()))
    ans = 0
    for w in wishlist:
        if w not in taken:
            taken.add(w)
            ans = w
            break
    print(ans)