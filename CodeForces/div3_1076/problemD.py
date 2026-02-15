import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        a.sort()
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + b[i]
        
        ans = 0
        j = 0 

        for k in range(1, n + 1):
            while j + 1 <= n and prefix[j + 1] <= k:
                j += 1
            
            x = a[n - k]
            ans = max(ans, x * j)
        
        print(ans)

if __name__ == "__main__":
    solve()
