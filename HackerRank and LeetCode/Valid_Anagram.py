	# Given two strings s and t , write a function to determine if t is an anagram of s.

	# Example 1:

	# Input: s = "anagram", t = "nagaram"
	# Output: true
	# Example 2:

	# Input: s = "rat", t = "car"
	# Output: false
	# Note:
	# You may assume the string contains only lowercase alphabets.

	# Follow up:
	# What if the inputs contain unicode characters? How would you adapt your solution to such case?

	class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = {}
        for letter in s:
            if letter in smap.keys():
                smap[letter] += 1      
            else:
                smap[letter] = 1
                
        for letter in t:
            if letter in smap.keys():
                smap[letter] -=1
            else:
                return False
            if smap[letter] < 0:
                return False
        return True

        