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

#O(logn) - Time Complexity
#O(1) - Space Complexity
'''
1. We are going to use binary search method for this solution
2. We create two pointers left=0 which starts at index 0 and right = len(nums) - 1 which starts at the last index of array nums
3. Then we enter a while loop
4. While loop will continue as long as left lesser than or equal to right meaning there are still elements to consider within the search range
5. Then we calculate the middle index
6. if mid is the target, we return
7. Else if mid is less than the target that means the search needs to be implemented to the right side of mid in the array
8. We relocate the pointer to start 1 + mid range and go back in the loop to calculate the mid again for this new search space
9. Else if mid is greater than the target that means the search needs to be implemented to the left side of mid and go back in the loop to calculate the mid again for this new search space
10. If the loop ends and we havent found the target, left will point to the target
'''
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = left+(right - left) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left