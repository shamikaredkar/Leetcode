'''
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

Example 1:
    Input: words = ["alice","bob","charlie"], s = "abc"
    Output: true

Example 2:
    Input: words = ["an","apple"], s = "a"
    Output: false

Example 3:
    Input: words = ["never","gonna","give","up","on","you"], s = "ngguoy"
    Output: true
'''

#O(N+M) - Time Complexity
#O(N) - Space Complexity
'''
1. We start by creating a list where we will store the 0th index of each word.
2. We use a for loop to iterate over the words
3. We use a second for loop to iterate over each character of the string
4. We append the 0th index of word 
5. Now our list looks something like ['a','b','c']
6. We map over this list and convert each element into a string and join that string together
7. We then compare strings together
'''
class Solution(object):
    def isAcronym(self, words, s):
        list1 = []
        for i in words:
            for c in range(0,1):
                list1.append(i[0])
        result = ''.join(map(str, list1))
        if result == s:
            return True

#Shorter version of
class Solution(object):
    def isAcronym(self, words, s):
        word = ''
        for i in words:
            word += i[0]
        # result = ''.join(map(str, list1))
        return word == s
    
#OR

#ans = ''.join([i[0] for i in words])
