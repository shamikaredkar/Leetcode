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

#O(N) - Time Complexity
#O(N) - Space Complexity
'''
1. map() function takes 2 arguments - function(str in this case) and the iterable(digits in this case)
2. We iterate through each element in our list (digits) and convert them into a string.
3. We join the list of strings together as a single string
4. Then we convert the string back into an integer
5. We add 1 to the integer
6. We then convert our int result into a string (we do this because we need to iterate through the number to put each digit as a seperate element in the list, and int is not iterable)
7. Then we convert each of our digits back into an int


'''

class Solution(object):
    def plusOne(self, digits):
        result = int(''.join(map(str, digits))) 
        result+=1
        final = map(int, str(result))
        return final