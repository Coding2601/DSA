S = input().strip()
T = input().strip()
n, m = len(S), len(T)
total = n * (n+1)//2
next_pos = [[n] * 26 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(26):
        next_pos[i][j] = next_pos[i+1][j]
    next_pos[i][ord(S[i]) - ord('a')] = i
count_occurence = 0
for l in range(n):
    pos = l
    found = True
    for ch in T:
        pos = next_pos[pos][ord(ch) - ord('a')]
        if pos == n:
            found = False
            break
        pos += 1
    if found:
        r = pos - 1
        count_occurence += (n - r)
print(total - count_occurence)