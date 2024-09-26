'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1: 
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
'''

#O(N) - Time Complexity
#O(1) -Space Complexity
'''
1. We use enumerate to track the value and index while iterating through the list 
2. If we find the value in the list, we return its index, otherwise we keep iterating
3. Until we find a value which is greater than target - this is where the index would've been inserted
4. We return its index 
'''

class Solution(object):
    def searchInsert(self, nums, target):
        for index, value in enumerate(nums):
            if value == target:
                return index  
            elif value > target:
                return index  
        return len(nums)