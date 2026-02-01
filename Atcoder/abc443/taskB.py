# AP series + Binary search

n, k = map(int, input().split())
low, high = 0, 2*10**9

def bean_count(x):
    return ((x + 1)*(2*n + x) // 2)

while low < high:
    mid = (low + high) // 2
    if bean_count(mid) >= k:
        high = mid
    else:
        low = mid + 1
print(low)