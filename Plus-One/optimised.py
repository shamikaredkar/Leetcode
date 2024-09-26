'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1: 
    Input: digits = [1,2,3]
    Output: [1,2,4]

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

Example 3:
    Input: digits = [9]
    Output: [1,0]
'''

'''
1. We reverse the list  of digits to get the last digit first and it's easy to handle edge cases
2. one represents the carry and i is the index which helps us traverse the array
3. We check if i is within bounds of the digits
4. If the digit is 9, we set this digit to 0
5. If the current digit is less than 9, we simply add 1 and set one = 0 to stop the loop
6. If we reach the end of the list and the carry still exists, we append 1 to the number
5. We reverse the list again
'''

#O(N) - Time Complexity
class Solution(object):
    def plusOne(self, digits):
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
        