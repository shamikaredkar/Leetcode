'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
'''

#O(N) - Time Complexity
#O(N) - Space Complexity (We're creating an additional data structure)
'''
1. We need indices so we use a dictionary
2. We use enumerate since we need the indices and values to calculate the required value
3. After getting the required value we chekc if it exists in our dictionary
4. If it does, we return the value of the key (required is the key) and the index
5. If it doesnt exist we add to the dictionary the "value" variable as the key as the "index" variable as the value
'''

class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for index, value in enumerate(nums):
            required = target - value
            if required in dictionary:
                return [dictionary[required], index]
            dictionary.update({value: index})

        