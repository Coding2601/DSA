t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    obj = {}
    for i in a:
        obj[i] = obj.get(i, 0) + 1
    distinct, maxF = len(obj), max(obj.values())
    ans = max(min(distinct, maxF-1), min(distinct-1, maxF))
    print(ans)