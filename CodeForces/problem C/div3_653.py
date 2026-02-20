import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    brackets = input().strip()
    balance, ans = 0, 0
    for b in brackets:
        if b == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            ans += 1
            balance = 0
    print(ans)