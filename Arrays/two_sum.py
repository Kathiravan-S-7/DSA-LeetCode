// Targeted Element is found using Index of the List
// Author: Kathiravan S


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]
       
