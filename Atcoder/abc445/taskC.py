import sys
input = sys.stdin.readline

N = int(input())
array = [0] + list(map(int, input().split()))
ans, K = [], 10**100

for s in range(1, N+1):
    slow, fast = s, s
    while True:
        slow = array[slow]
        fast = array[array[fast]]
        if slow == fast:
            break
    cycle_start, meeting_points = s, slow
    while cycle_start != meeting_points:
        cycle_start = array[cycle_start]
        meeting_points = array[meeting_points]
    cycle_len, curr_point = 1, array[cycle_start]
    while curr_point != cycle_start:
        curr_point = array[curr_point]
        cycle_len += 1
    req_steps, curr_point = 0, s
    while curr_point != cycle_start:
        curr_point = array[curr_point]
        req_steps += 1
    if K < req_steps:
        curr_point = s
        for _ in range(K):
            curr_point = array[curr_point]
        ans.append(curr_point)
    else:
        remaining = K - req_steps
        pos_in_cycle = remaining % cycle_len
        curr_point = cycle_start
        for _ in range(pos_in_cycle):
            curr_point = array[curr_point]
        ans.append(curr_point)

print(" ".join(map(str, ans)))