N, K = map(int, input().split())
S = [input() for _ in range(N)]
arr = sorted(S[:K+1])
for _ in range(K+1):
    print(arr[_])