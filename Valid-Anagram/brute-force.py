'''
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false
'''

#Anagram : Words that have the same letters

'''
The solution below wouldnt work for test case where s = "aa" and t = "a"
'''
# #O(N+M) : Time Complexity - Where N & M are lengths of s & t respectively
# #O(N+M) : Space Complexity 
# class Solution(object):
#     def isAnagram(self, s, t):
#         first = set(s)
#         second = set(t)
#         if first == second:
#             return True
#         else: 
#             return False

#O(N) - Time Complexity
#O(N) - Space Complexity
'''
1. Check if the lengths of s & t are equal if not immediately return false
2. Create a dictionary for each list where the character is the key and the occurence is the value
3. we iterate through the length of s since s&t are equal lengths
4. we add as a key to countS the value of s[i]
5. if s[i] already exists in the dictionary, we try to return its value and add 1 to it
6. if s[i] doesnt exist in the dictionary we initialize it by 0
'''
class Solution(object):
    def isAnagram(self, s, t):
        countS, countT ={},{} #{letter: occurences}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT