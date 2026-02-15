import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    suff_max, suff_pos = [0] * n, [0] * n
    suff_max[-1], suff_pos[-1] = array[-1], n - 1
    for i in range(n-2, -1, -1):
        if array[i] > suff_max[i+1]:
            suff_max[i], suff_pos[i] = array[i], i
        else:
            suff_max[i], suff_pos[i] = suff_max[i+1], suff_pos[i+1]
    for left in range(n):
        if suff_max[left] > array[left]:
            right = suff_pos[left]
            array[left:right+1] = array[left:right+1][::-1]
            break
    print(*array)