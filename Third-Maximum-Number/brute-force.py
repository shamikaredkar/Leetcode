'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
    Input: nums = [3,2,1]
    Output: 1
    
Example 2:
    Input: nums = [1,2]
    Output: 2

Example 3:
    Input: nums = [2,2,3,1]
    Output: 1
'''

#O(N) - Time Complexity
#O(N) - Space Complexity
'''
1. We convert the nums into a set to remove duplicates
2. We check if the length of the set is less than 3, if it is then we immediately return the max
3. If length is less than 3, then we move forward in a loop that runs 3 times since we need to find the 3rd maximum number
4. We find the maximum and remove it, We do this 3 times to find the 3rd maximum
'''

class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        for num in range(0,3):
            maximum = max(nums)
            nums.remove(maximum)
        return maximum