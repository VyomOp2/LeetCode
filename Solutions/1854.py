# 1854. Maximum Population Year    --> (https://leetcode.com/problems/maximum-population-year)

# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

# Return the earliest year with the maximum population.

# Example 1:

# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
# Example 2:

# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.

# Time Complexity: O(n) and Space Complexity: O(n)

# We create a hashmap where the keys are the years and the values are the number of people born


# array = [0] * 101: Creates an array a of size 101, initialized with zeros. 
# n = len(logs): Stores the number of logs (i.e., the number of birth-death records).
# current_year keeps track of the current population.
# maximum stores the maximum population found so far.
# year stores the earliest year with the maximum population.

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        array , n = [0] * 101 , len(logs)
        for birth , death in logs :
            array[birth - 1950] += 1
            array[death - 1950] -= 1
        current_year = maximum = year = 0
        for i in range(101) :
            current_year += array[i]
            if current_year > maximum :
                maximum = current_year
                year = i + 1950
        return year
