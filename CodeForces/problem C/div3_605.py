# combinatorics + two pointers

n, k = map(int, input().split())
s = input().strip()
allowed, ans, curr_len = set(input().split()), 0, 0
for char in s:
    if char in allowed:
        curr_len += 1
    else:
        ans += curr_len * (curr_len + 1) // 2
        curr_len = 0
ans += curr_len * (curr_len + 1) // 2
print(ans)