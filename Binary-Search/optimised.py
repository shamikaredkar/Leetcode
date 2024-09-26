#Similar to Search-Insert-Position

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
'''

'''
1. Initialize the counter left with 0 to indicate a counter from the start of the array nums
2. Initialize the counter right with len(nums) - 1 to indicate the last number in the array
3. We calculate mid as the middle integer in the array
4. If we find the target we return the mid index
5. If we don't we compare the mid to see if it's lesser than the target, then the entire search space will go to the right of the array and the left pointer will update to mid + 1
6. if the mid is greater than the target, then the search space space will update to the left search space and the right pointer will update to mid - 1
'''

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return (-1)
        