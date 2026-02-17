import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()  # empty line before each test case
    
    grid = [input().strip() for _ in range(8)]
    
    red_last = False
    
    for row in grid:
        if row == "RRRRRRRR":
            red_last = True
            break
    
    if red_last:
        print("R")
    else:
        print("B")
