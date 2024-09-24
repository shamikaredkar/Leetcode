'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
Example 2:
    Input: nums = [1,2,3,4]
    Output: false
Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
'''

#O(N) - Time
#O(N) - Space (We created a set)
#This is an optimal solution
'''
1. We create a new set
2. So for every num in nums, we check if the num exists in the set
3. if not, we add that number to the set
4. if yes, we return True
'''
class Solution(object):
    def containsDuplicate(self, nums):
        new_set = set()
        for num in nums:
            if num not in new_set:
                new_set.add(num)
            else:
                return True 