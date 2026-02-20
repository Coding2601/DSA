import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k == 2:
        if any(x % 2 == 0 for x in a):
            print(0)
        else:
            print(1)

    elif k == 3:
        ans = float('inf')
        for x in a:
            r = x % 3
            if r == 0:
                ans = 0
                break
            ans = min(ans, 3 - r)
        print(ans)

    elif k == 4:
        cnt_even = 0
        has_div4 = False

        for x in a:
            if x % 2 == 0:
                cnt_even += 1
            if x % 4 == 0:
                has_div4 = True

        if has_div4 or cnt_even >= 2:
            print(0)
        else:
            cost_make_div4 = float('inf')
            for x in a:
                r = x % 4
                if r != 0:
                    cost_make_div4 = min(cost_make_div4, 4 - r)

            if cnt_even == 1:
                cost_make_two_even = 1
            else:
                cost_make_two_even = 2

            print(min(cost_make_div4, cost_make_two_even))

    elif k == 5:
        ans = float('inf')
        for x in a:
            r = x % 5
            if r == 0:
                ans = 0
                break
            ans = min(ans, 5 - r)
        print(ans)