t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    stack = []
    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        print('YES')
    else:
        print("NO")