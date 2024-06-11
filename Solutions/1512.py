# 1512. Number of Good Pairs   -->  (https://leetcode.com/problems/number-of-good-pairs)

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Time Complexity: O(n) and Space Complexity: O(n)
# This Problem is solved with the help of hashmaps.

from typing import Counter, List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums) #n -> c
        result = 0
        for n , c in count.items() :
            result += c * (c - 1) // 2
        return result
