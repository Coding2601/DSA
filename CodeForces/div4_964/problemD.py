t = int(input())
for _ in range(t):
    a = list(input().strip())
    t = input().strip()
    j = 0
    for i in range(len(a)):
        if j < len(t) and (a[i] == t[j] or a[i] == '?'):
            a[i] = t[j]
            j += 1
    if j < len(t):
        print("NO")
    else:
        for i in range(len(a)):
            if a[i] == '?':
                a[i] = 'a'
        print("YES")
        print(''.join(a))