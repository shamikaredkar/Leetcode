'''
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3: 
    Input: strs = ["a"]
    Output: [["a"]]
'''

'''
1. We initialize our result with a defaultdict(list) where if we try to access values that do not exist we get a default value (empty list)
2. Then we loop through out strs list
3. We initialize a counter count with [0] * 26 so we get 26 zeroes [0,0,0...]
4. Then for each letter in s element of strs
5. We access the letter by index in the count list by subtracting the ascii of 'a' from ascii of c 
    Eg. in ate: the first letter is a.
        so ascii of a-a = 0
        count[0] = 1
        for t ascii of t=84
        so 84-65
        count[19] = 1
        final count list for ate might be [1,0,0,0,1,0,0,..]
6. We convert this count list into a tuple
7. We use this tuple as a key in result and add the word ate to the list for this key 
    We convert this list into a tuple because Python dictionaries use immutable types like tuples as keys. Lists are mutable so we wouldn't have been able to use them as keys.
Eg: result[(1, 0, 0, 0, 1, ...)] = ["eat", "tea"]

'''

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list) #mapping character count to list of Anagrams
        for s in strs:
            count = [0] * 26 #Having 26 0's from a-z
            for c in s:
                count[ord(c) - ord('a')] +=1
                #ascii value of a - a = 0
                #ascii value of z - a = 25
            #defaultdict tries to find the key result[tuple(count)] but since it doesnt exist it creates the key and initializes it with an empty list and then appends the word to it
            result[tuple(count)].append(s)
        return result.values()