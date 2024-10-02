'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
Example1:
    Input: nums = [-1,1,2,3,1], target = 2
    Output: 3

Example2:
    Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
    Output: 10
'''

#O(N^2) - Time complexity
#O(N) - Space complexity
'''
1. We create an array where we want to store the pairs
2. We use enumerate to get the index and value of the iteration
3. In the second for loop we start the from index+1 till the end (index+1:)
4. We get the addition of the two numbers
5. Compare it to the target
6. If it is less we append the list of these two integers into our result list
'''

class Solution(object):
    def countPairs(self, nums, target):
        result = []
        for index, value in enumerate(nums):
            for value2 in nums[index+1:]:
                addition = value + value2
                if addition < target:
                    result.append([value, value2])
        return len(result)