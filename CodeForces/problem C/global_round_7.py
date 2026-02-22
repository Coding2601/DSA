# combinatorics (serious problem)
n, k = map(int, input().split())
p = list(map(int, input().split()))
MOD = 998244353
max_sum = k * (2*n - k + 1) // 2
threshold = n - k + 1
positions = [i for i, x in enumerate(p) if x >= threshold]
ways = 1
for i in range(k-1):
    ways = (ways * (positions[i+1] - positions[i])) % MOD
print(max_sum, ways)