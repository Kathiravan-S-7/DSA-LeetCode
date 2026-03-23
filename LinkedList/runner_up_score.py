# Find the second highest (runner-up) score by ignoring the maximum value and tracking the next largest

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)

runner_up = -100000  

for num in arr:
    if num != max_val and num > runner_up:
        runner_up = num

print(runner_up)
