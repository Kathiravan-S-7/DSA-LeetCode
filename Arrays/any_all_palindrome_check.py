# Determine whether all elements are positive and any element is a palindrome
# Author: Kathiravan S
n = int(input())
arr = input().split()
print(all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr))
