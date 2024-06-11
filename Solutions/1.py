# 1. Two Sum    --> (https://leetcode.com/problems/two-sum/) 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Time Complexity: O(n) and Space Complexity: O(n)

# This Problem is solved with the help of hashmaps.
class Solution:
    def twoSum(self , nums: list[int] , target: int) -> list[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            
            if y in h and h[y] != i:
                return [ i , h[y]]
