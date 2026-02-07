import sys
input = sys.stdin.readline

N, K = map(int, input().split())

N_str = str(N)
Len_N_str = len(N_str)

dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(Len_N_str + 1)]
dp[0][0][1] = 1

for position in range(Len_N_str):
    digit = int(N_str[position])
    for curr_sum in range(K+1):
        for is_less in range(2):
            if dp[position][curr_sum][is_less] == 0:
                continue
            max_digit = digit if is_less else 9
            for next_digit in range(max_digit + 1):
                if curr_sum + next_digit > K:
                    continue
                new_is_less = is_less and next_digit == digit
                dp[position + 1][curr_sum + next_digit][new_is_less] += dp[position][curr_sum][is_less]
print(dp[Len_N_str][K][0] + dp[Len_N_str][K][1])